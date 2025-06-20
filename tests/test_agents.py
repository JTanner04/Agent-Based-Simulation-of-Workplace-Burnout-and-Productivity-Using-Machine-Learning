import pytest
from simulation.agents.employee import EmployeeAgent
from simulation.agents.manager import ManagerAgent
from mesa import Model

class DummyModel(Model):
    pass


def test_employee_agent():
    model = DummyModel()
    emp = EmployeeAgent(1, model)
    assert emp.stress == 0.0
    assert emp.productivity == 1.0
    # Give tasks and step
    emp.task_queue = [1, 2, 3]
    emp.step()
    assert emp.stress == 3
    assert emp.productivity == max(0.0, 1.0 - emp.stress / 10.0)
    assert emp.task_queue == []


def test_manager_agent_assigns_tasks():
    from simulation.main import WorkplaceModel
    from simulation.agents.manager import ManagerAgent
    from simulation.agents.employee import EmployeeAgent

    model = WorkplaceModel(num_employees=1)
    manager = next(a for a in model.schedule.agents if isinstance(a, ManagerAgent))
    emp = next(a for a in model.schedule.agents if isinstance(a, EmployeeAgent))
    manager.step()
    assert len(emp.task_queue) >= 1

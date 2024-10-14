from datetime import datetime
from typing import Dict

from fastapi import APIRouter, HTTPException

from to_do_list.database import Tasks, TasksManager
from to_do_list.enums import TASK_PRIORITYS, TASK_STATES

ROUTER = APIRouter()


class BaseViewSet:
    """Base ViewSet class mimicking Django's ViewSet, customized for FastAPI."""

    model = None
    manager = None

    def __init__(self):
        if not self.model or not self.manager:
            raise ValueError("ViewSet requires a model and manager.")

    async def list(self):
        """GET /: List all instances."""
        return self.manager.all()

    async def retrieve(self, obj_id: int):
        """GET /{id}: Retrieve a specific instance by ID."""
        return self.manager.get(obj_id)

    async def create(self, item_data: Dict):
        """POST /: Create a new instance."""
        try:
            max_task = max([x.get("order") for x in self.manager.all()]) + 1
        except ValueError:
            max_task = 1 + 1
        item_data.update({"created_at": datetime.now(),
                          "order": max([x.get("order") for x in self.manager.all()]) + 1,
                          "status": 0})
        return self.manager.create(**item_data)

    async def update(self, obj_id: int, item_data: Dict):
        """PUT /{id}: Update an existing instance by ID."""
        return self.manager.update(obj_id, **item_data)

    async def delete(self, obj_id: int):
        """DELETE /{id}: Delete an instance by ID."""
        result = self.manager.delete(obj_id)
        if not result:
            raise HTTPException(status_code=404)
        return {"message": result['message']}

    @staticmethod
    async def states():
        """GET /: List task states."""
        return TASK_STATES

    @staticmethod
    async def priorities():
        """GET /: List task prioritys."""
        return TASK_PRIORITYS


# Exemplo de ViewSet para Tasks
class TaskViewSet(BaseViewSet):
    model = Tasks
    manager = TasksManager


task_viewset = TaskViewSet()
ROUTER.add_api_route("/tasks", task_viewset.list, methods=["GET"], tags=["task"])
ROUTER.add_api_route("/tasks/{obj_id}", task_viewset.retrieve, methods=["GET"], tags=["task"])
ROUTER.add_api_route("/tasks", task_viewset.create, methods=["POST"], tags=["task"])
ROUTER.add_api_route("/tasks/{obj_id}", task_viewset.update, methods=["PUT"], tags=["task"])
ROUTER.add_api_route("/tasks/{obj_id}", task_viewset.delete, methods=["DELETE"], tags=["task"])

ROUTER.add_api_route("/states", task_viewset.states, methods=["GET"], tags=["constraints"])
ROUTER.add_api_route("/priorities", task_viewset.priorities, methods=["GET"], tags=["constraints"])

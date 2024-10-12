from typing import Dict

from fastapi import APIRouter, HTTPException

from to_do_list.database import Tasks, TasksManager

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
        result = self.manager.all()
        print(result)
        if not result:
            raise HTTPException(status_code=400)
        return result

    async def retrieve(self, obj_id: int):
        """GET /{id}: Retrieve a specific instance by ID."""
        result = self.manager.get(obj_id)
        if not result:
            raise HTTPException(status_code=404)
        return result

    async def create(self, item_data: Dict):
        """POST /: Create a new instance."""
        result = self.manager.create(**item_data)
        if not result:
            raise HTTPException(status_code=400)
        return result

    async def update(self, obj_id: int, item_data: Dict):
        """PUT /{id}: Update an existing instance by ID."""
        result = self.manager.update(obj_id, **item_data)
        if not result:
            raise HTTPException(status_code=400)
        return result

    async def delete(self, obj_id: int):
        """DELETE /{id}: Delete an instance by ID."""
        result = self.manager.delete(obj_id)
        if not result:
            raise HTTPException(status_code=404)
        return {"message": result['message']}


# Exemplo de ViewSet para Tasks
class TaskViewSet(BaseViewSet):
    model = Tasks
    manager = TasksManager


task_viewset = TaskViewSet()
ROUTER.add_api_route("/tasks", task_viewset.list, methods=["GET"])
ROUTER.add_api_route("/tasks/{obj_id}", task_viewset.retrieve, methods=["GET"])
ROUTER.add_api_route("/tasks", task_viewset.create, methods=["POST"])
ROUTER.add_api_route("/tasks/{obj_id}", task_viewset.update, methods=["PUT"])
ROUTER.add_api_route("/tasks/{obj_id}", task_viewset.delete, methods=["DELETE"])

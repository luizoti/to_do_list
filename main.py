"""The main FastApi module."""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from to_do_list.api.v1 import ROUTER
from to_do_list.database import TasksManager
from to_do_list.faked import faked_tasks

# from to_to_list.database import ImageHistoryManager, session_clear

ports = [
    "8000",
]

hosts = [
    {"host": "localhost", "ports": ports, "https": False},
]


def generate_origins():
    """Function with objective to create a list of allowed origins."""
    for host in hosts:
        host_name = host.get("host")
        https = "https://" if host.get("https") else "http://"  # noqa
        if host.get("ports"):
            for port in ports:
                yield f"{https}{host_name}:{port}"
        yield f"{https}{host_name}"


origins = list(generate_origins())

FAST_API_APP = FastAPI()
# FAST_API_APP = FastAPI(dependencies=[Depends(session_clear)])

FAST_API_APP.add_middleware(
    CORSMiddleware,  # noqa
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FAST_API_APP.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@FAST_API_APP.get("/")
async def index(request: Request):
    """Application index page."""
    return templates.TemplateResponse(
        request=request, name="index.html"
    )


@FAST_API_APP.get("/include_faked")
async def include_faked_tasks(request: Request):
    """Application index page."""
    task_manager = TasksManager
    for item in faked_tasks:
        task_manager.create(**item)
    return task_manager.all()


FAST_API_APP.include_router(ROUTER)

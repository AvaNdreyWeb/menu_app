from fastapi import FastAPI

from . import database
from .routers import dishes, menus, submenus

BASE_PATH = "/api/v1"
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(menus.router, prefix=BASE_PATH)
app.include_router(submenus.router, prefix=BASE_PATH)
app.include_router(dishes.router, prefix=BASE_PATH)

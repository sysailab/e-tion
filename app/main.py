from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
import os
from pathlib import Path

from fastapi.staticfiles import StaticFiles

from .dependencies import get_query_token, get_token_header
from .routers import items, users, unsplash
from .internal import admin
from .library.helpers import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()
app.mount("/static", StaticFiles(directory=str(Path(BASE_DIR, 'static'))), name="static")


templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
        tags=["admin"],
        dependencies=[Depends(get_token_header)],
        responses={418: {"description": "I'm a teapot"}},
        )

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    data = openfile("home.md")
    print(data)
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.get("/page/{page_name}", response_class=HTMLResponse)
async def show_page(request: Request, page_name: str):
    data = openfile(page_name+".md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

app.include_router(unsplash.router)

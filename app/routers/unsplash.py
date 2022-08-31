from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import os
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


templates = Jinja2Templates(directory=str(Path(BASE_DIR, '../templates')))

router = APIRouter()

@router.get("/unsplash", response_class=HTMLResponse)
async def unsplash_home(request: Request):

    return templates.TemplateResponse("unsplash.html", {"request": request})
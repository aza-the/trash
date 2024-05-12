from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.api.utils import templates

router = APIRouter()


@router.get('/', response_class=HTMLResponse)
def get_flats_page(request: Request):
    return templates.TemplateResponse('index.html',
                                      context={'request': request})

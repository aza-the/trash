from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.api.utils import templates

router = APIRouter()


@router.get('/', response_class=HTMLResponse)
def get_sample_page(request: Request):
    return templates.TemplateResponse('chat.html',
                                      context={'request': request})

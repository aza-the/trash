from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from app.api.main import api_router
from app.api.utils import templates

app = FastAPI()
app.mount(
    '/static', StaticFiles(directory='app/static'), name='static')

app.include_router(api_router)


@app.exception_handler(404)
def custom_404_handler(request: Request, __):
    return templates.TemplateResponse(
        'error_404.html', context={'request': request}
    )

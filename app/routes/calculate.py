from fastapi import APIRouter, Query, Request
from fastapi.templating import Jinja2Templates
from starlette import status

router = APIRouter()

templates = Jinja2Templates(directory='app/templates')

@router.get('/')
async def render_calculate_page(request: Request):
    return templates.TemplateResponse('calculate.html', {'request': request})

@router.post('/add/', status_code=status.HTTP_200_OK)
async def add(a: int=Query(gt=0), b: int=Query(gt=0)):
    return {'result': a + b}


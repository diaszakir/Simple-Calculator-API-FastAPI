from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette import status

router = APIRouter(
    tags=['Calculation']
)

templates = Jinja2Templates(directory='app/templates')

@router.get('/')
async def render_calculate_page(request: Request):
    return templates.TemplateResponse('calculate.html', {'request': request})

@router.post('/add/', status_code=status.HTTP_200_OK)
async def add(a: int, b: int):
    return {'result': a + b}

@router.post('/sub/', status_code=status.HTTP_200_OK)
async def sub(a: int, b: int):
    return {'result': a - b}

@router.post('/multiply', status_code=status.HTTP_200_OK)
async def multiply(a: int, b: int):
    return {'result': a * b}
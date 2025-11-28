from fastapi import APIRouter, Query
from starlette import status

router = APIRouter()

@router.post('/add/', status_code=status.HTTP_200_OK)
async def add(a: int=Query(gt=0), b: int=Query(gt=0)):
    return {'result': a + b}


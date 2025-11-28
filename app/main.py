from fastapi import FastAPI
from starlette import status
from app.routes import calculate

app = FastAPI()

@app.get("/test", status_code=status.HTTP_200_OK)
async def test_api():
    return {"message": "OK"}

app.include_router(calculate.router)
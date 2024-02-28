from fastapi import FastAPI
from contextlib import asynccontextmanager
from loguru import logger

from sqlmodel import SQLModel
from database import engine
from dependency import load_model
from config import config
from api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # DB 테이블 생성
    logger.info("Creating database table")
    SQLModel.metadata.create_all(engine)
    
    # 모델 로드
    logger.info("Loading model")
    load_model(config.model_path)

    
    yield
    

app = FastAPI(lifespan=lifespan)
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Hello World"}



if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
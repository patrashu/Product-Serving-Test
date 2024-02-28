from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger
from sqlmodel import SQLModel
from fastapi.middleware.cors import CORSMiddleware

from api import router
from config import config
from database import engine
from dependencies import load_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 데이터베이스 테이블 생성
    logger.info("Creating database tables")
    SQLModel.metadata.create_all(engine)

    # 모델 로드
    logger.info("Loading model")
    load_model(config.model_path)

    yield





app = FastAPI(lifespan=lifespan)
origins = ["*"]  # 또는 필요한 도메인 리스트
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

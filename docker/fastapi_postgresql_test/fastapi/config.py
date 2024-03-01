import os
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


load_dotenv()

class Config(BaseSettings):
    db_url: str = Field(default=os.getenv("POSTGRES_DB_URL"), env="DB_URL")

config = Config()
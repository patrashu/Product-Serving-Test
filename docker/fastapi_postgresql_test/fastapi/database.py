import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

from config import config


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    created_at: Optional[str] = Field(default_factory=datetime.datetime.now)


engine = create_engine(config.db_url)
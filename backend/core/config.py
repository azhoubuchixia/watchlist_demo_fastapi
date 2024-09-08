from typing import Optional

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):

    DESC: Optional[str] = """
    - 电影项目列表，基于Hello Flask一书中的实战项目
    - 实现,FastAPI
    """


settings = Settings()

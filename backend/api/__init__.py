from fastapi import FastAPI
from .v1 import v1
from tortoise.contrib.fastapi import register_tortoise
from backend.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from backend.core.configs import ORIGINS

app = FastAPI(description=settings.DESC)

app.include_router(v1, prefix="/api")

# 配置跨域cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(
    app,
    db_url="sqlite:///watch.db",
    modules={"models": ["backend.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# 启动redis
# @app.on_event("startup")
# async def startup():
#     """
#     start redis
#     :return:
#     """
#     app.state.redis:Redis=await aioredis.from_url("redis://127.0.0.1:6379",decode_response=True)
#
# @app.on_event("shutdown")
# async def shutdown():
#     """
#     close redis
#     :return:
#     """
#     await app.state.redis.close()

from typing import List

from fastapi import FastAPI, APIRouter, Depends

from backend.models import Movie
from backend.schemas import Movie_Pydantic, MovieIn_Pydantic
from backend.core import get_current_user

movie = APIRouter(tags=['电影相关'], dependencies=[Depends(get_current_user)])


@movie.get("/check_movie", summary="查看", response_model=List[Movie_Pydantic])
async def check_movie(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit  # 分页？
    return await Movie_Pydantic.from_queryset(Movie.all().offset(skip).limit(limit))


@movie.post("/add_movie", summary="新增", response_model=Movie_Pydantic)
async def add_movie(movie_form: MovieIn_Pydantic):
    movie_obj = await Movie.create(**movie_form.dict())
    # 确保从 ORM 对象转换为 Pydantic 模型
    return await Movie_Pydantic.from_tortoise_orm(movie_obj)


@movie.put("/update_movie/{pk}", summary="编辑")
async def update_movie(pk: int, movie_form: MovieIn_Pydantic):
    # pk为主键
    if await Movie.filter(pk=pk).update(**movie_form.dict()):
        return {
            "msg": "更新成功"
        }

    return {
        "msg": "更新失败"
    }


@movie.delete("/delete_movie/{pk}", summary="删除")
async def delete_movie(pk: int):
    if await Movie.filter(pk=pk).delete():
        return {
            "msg": "删除成功"
        }

    return {
        "msg": "删除失败"
    }

from typing import List

from fastapi import FastAPI, APIRouter, Depends

from backend.core import get_current_user
from backend.schemas import User_Pydantic, UserIn_Pydantic
from backend.models import User

user = APIRouter(tags=['用户'], dependencies=[Depends(get_current_user)])


@user.get("/user", summary="查询", response_model=List[User_Pydantic])
async def check_user():
    return await User_Pydantic.from_queryset(User.all())


@user.put("/update user", summary="修改")
async def update_user(user_form: UserIn_Pydantic):
    if await User.filter(username=user_form.username).update(**user_form.dict()):
        return {
            "msg": "修改成功"
        }
    return {
        "msg": "更新失败"
    }

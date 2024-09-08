from fastapi import FastAPI, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from backend.models import *
from backend.core import *
from backend.schemas import User_Pydantic, UserIn_Pydantic
from backend.core.basic_return import *

login = APIRouter(tags=['登录'])


@login.post("/login", summary="登录")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if users := await User.get(username=form_data.username):
        if pwd_context.verify(form_data.password, users.password):
            # return {
            #     "msg": "登录成功",
            #     "access_token": create_access_token({"sub": users.username}),
            #     "token_type": "bearer"}
            data = create_access_token({"sub": users.username})
            return ResponseToken(data={"token": f"bearer {data}"}, access_token=data)
    return Response400(msg="请求失败")
    # return {
    #     "msg": "账号或密码错误"
    # }


@login.post("/register", summary="注册", response_model=User_Pydantic)
async def user_register(user_form: UserIn_Pydantic):
    # 加密密码
    hashed_password = pwd_context.hash(user_form.password)

    # 创建用户对象，使用加密后的密码
    # 从 user_form.dict() 中移除原始密码
    user_data = user_form.dict()
    user_data['password'] = hashed_password

    user_obj = await User.create(**user_data)

    # 返回用户信息
    return User_Pydantic.from_tortoise_orm(user_obj)

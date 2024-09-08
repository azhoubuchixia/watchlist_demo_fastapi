from tortoise.models import Model
from tortoise import fields


class User(Model):
    username = fields.CharField(max_length=20, null=False, description='账号')
    password = fields.CharField(max_length=255, null=False, description='密码')
    nickname = fields.CharField(max_length=20, null=False, description='昵称', default='你好')

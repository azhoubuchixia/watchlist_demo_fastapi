from tortoise.models import Model
from tortoise import fields


class Movie(Model):
    moviename = fields.CharField(max_length=50, null=False, description='电影名字')
    year = fields.CharField(max_length=20, null=False, description='年份')

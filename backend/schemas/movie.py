from tortoise.contrib.pydantic import pydantic_model_creator
from backend.models import Movie

Movie_Pydantic = pydantic_model_creator(Movie, name="Movie")
# exclude_readonly=True 排除只读字段，比如主键id
MovieIn_Pydantic = pydantic_model_creator(Movie, name="MovieIn", exclude_readonly=True)

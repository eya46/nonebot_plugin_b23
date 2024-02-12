from typing import Set

from nonebot import get_driver
from pydantic import BaseModel, Field


class Config(BaseModel):
    b23_default_command: str = Field(default='B站热搜')
    b23_commands: Set[str] = Field(default={'b23', })
    b23_block: bool = Field(default=False)
    b23_priority: int = Field(default=99)
    b23_max_length: int = Field(default=20, gt=0, lt=101)

config = Config(**get_driver().config.dict())

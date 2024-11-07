from typing import Set

from nonebot import get_plugin_config
from pydantic import BaseModel, Field


class Config(BaseModel):
    b23_default_command: str = Field(default="B站热搜")
    b23_commands: Set[str] = Field(
        default_factory=lambda: {
            "b23",
        }
    )
    b23_block: bool = Field(default=False)
    b23_priority: int = Field(default=99)
    b23_max_length: int = Field(default=20, gt=0, lt=101)
    b23_user_agent: str = Field(default="Chrome/130.0.0.0")


config = get_plugin_config(Config)

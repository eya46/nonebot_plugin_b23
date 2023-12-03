from typing import Set

from nonebot import get_driver
from pydantic import BaseModel, Field, Extra, __version__


class Config(BaseModel, extra=Extra.ignore):
    b23_default_command: str = Field(default='B站热搜')
    b23_commands: Set[str] = Field(default={'b23', })
    b23_block: bool = Field(default=False)
    b23_priority: int = Field(default=99)
    b23_max_length: int = Field(default=20, gt=0, lt=101)


if __version__[0] == "1":
    config = Config.parse_obj(get_driver().config)
elif __version__[0] == "2":
    config = Config.model_validate(get_driver().config)
else:
    raise Exception(f"不支持的pydantic版本:{__version__}")

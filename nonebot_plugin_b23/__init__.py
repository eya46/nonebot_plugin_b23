from httpx import AsyncClient
from nonebot import on_command, get_driver
from nonebot.params import RawCommand
from nonebot.plugin import PluginMetadata

from .config import Config

config = Config.parse_obj(get_driver().config)

__plugin_meta__ = PluginMetadata(
    name="B站热搜",
    description="获取B站热搜(移动端)",
    usage=(
        "发送指令获取B站热搜(移动端)\n"
        f"指令:{','.join(config.b23_commands)}"
    ),
    homepage="https://github.com/eya46/nonebot_plugin_b23",
    config=Config,
    supported_adapters=None,
)

b23_command = on_command(
    "b站热搜",
    aliases=config.b23_commands,
    block=config.b23_block,
    priority=config.b23_priority
)


@b23_command.handle()
async def b23_handler(command: str = RawCommand()):
    try:
        async with AsyncClient() as client:
            res = await client.get(
                "https://app.bilibili.com/x/v2/search/trending/ranking"
            )
            msg = f"{command}:\n"
            b23_list = res.json().get("data", {}).get("list", [])
            for i in range(min(len(b23_list), config.b23_max_length)):
                msg += f"{i + 1}.{b23_list[i]['show_name']}\n"
            await b23_command.send(msg.strip())
    except Exception as e:
        await b23_command.send(f"获取B站热搜失败,error:{e}")

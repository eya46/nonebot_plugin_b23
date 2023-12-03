from httpx import AsyncClient
from nonebot import on_command
from nonebot.internal.adapter import Message
from nonebot.params import RawCommand, CommandArg
from nonebot.plugin import PluginMetadata

from .config import config, Config

__plugin_meta__ = PluginMetadata(
    name="B站热搜",
    description="获取B站热搜(移动端)",
    usage=(
        "发送指令获取B站热搜(移动端)\n"
        f"指令:{','.join(config.b23_commands | {config.b23_default_command, })}\n"
        f"参数(可选):热搜数量\n"
        f"例:/{config.b23_default_command} 10\n"
    ),
    type="application",
    homepage="https://github.com/eya46/nonebot_plugin_b23",
    config=Config,
    supported_adapters=None,
)

b23_command = on_command(
    config.b23_default_command,
    aliases=config.b23_commands,
    block=config.b23_block,
    priority=config.b23_priority
)


@b23_command.handle()
async def b23_handler(command: str = RawCommand(), arg: Message = CommandArg()):
    arg = arg.extract_plain_text().strip()
    if arg.isdigit():
        try:
            arg = int(arg)
            if arg < 1 or arg > 100:
                raise ValueError("热搜数量必须在1-100之间")
            limit = arg
        except Exception as e:
            return await b23_command.send(f"参数错误[{arg}]:{e}")
    else:
        limit = config.b23_max_length
    try:
        async with AsyncClient() as client:
            res = await client.get(
                f"https://app.bilibili.com/x/v2/search/trending/ranking?limit={limit}"
            )
            msg = f"{command}:\n"
            b23_list = res.json().get("data", {}).get("list", [])
            for index, i in enumerate(b23_list):
                msg += f"{index + 1}.{i['show_name']}\n"
            await b23_command.send(msg.strip())
    except Exception as e:
        await b23_command.send(f"获取<{command}>失败,error:\n{e}")

from nonebot import on_command
from nonebot.internal.matcher import Matcher
import httpx

b23_command = on_command(
    "b站热搜",
    aliases={
        "B站热搜",
        "b23"
    },
    block=True
)


@b23_command.handle()
async def b23_handler(matcher: Matcher):
    try:
        async with httpx.AsyncClient() as r:
            r: httpx.AsyncClient
            res = await r.get(
                "https://app.bilibili.com/x/v2/search/trending/ranking"
            )
            msg = ""
            for index, i in enumerate(res.json().get("data", {}).get("list", [])):
                msg += f"{index + 1}.{i['show_name']}\n"
            if msg.endswith("\n"):
                msg = msg[:-1]
            await matcher.send(msg)
    except Exception as e:
        await matcher.send(f"获取B站热搜失败,error:{e}")

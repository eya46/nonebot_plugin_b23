<p align="center">
  <a href="https://nonebot.dev/"><img src="https://nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# NoneBot Plugin B23

# Bilibili热搜

![License](https://img.shields.io/github/license/eya46/nonebot_plugin_b23)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![NoneBot](https://img.shields.io/badge/nonebot-2.3.0+-red.svg)
</div>

## 默认命令

* B站热搜
* b23

## 使用

获取B站热搜(默认20条)
> /b23

获取10条B站热搜
> /b23 10

## 作用

获取B站热搜

## 安装

- `pip install nonebot-plugin-b23`
- `poetry add nonebot-plugin-b23`
- `pdm add nonebot-plugin-b23`

## 配置

|         名称          |        默认值         |           描述            |
|:-------------------:|:------------------:|:-----------------------:|
| b23_default_command |       'B站热搜'       |          默认命令           |
|    b23_commands     |     {'b23', }      |           命令名           |
|      b23_block      |       False        |        是否阻止向下传播         |
|    b23_priority     |         99         |           优先级           |
|   b23_max_length    |         20         | 热搜数量(1~100)<br />推荐别设太高 |
|   b23_user_agent    | "Chrome/130.0.0.0" |      请求头User-Agent      |

## [依赖](pyproject.toml)

* nonebot2[httpx]^2.3.0
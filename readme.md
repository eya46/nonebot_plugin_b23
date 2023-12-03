# Bilibili热搜

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

* nonebot2 2.0.0rc版本👇

> pip install nonebot-plugin-b23==0.0.9

* nonebot2 2.0.0+正式版本👇

> pip install nonebot-plugin-b23==0.1.2

* nonebot2 pydantic<3.0.0,>=1.10.0

> pip install nonebot-plugin-b23>=0.2.0

## 配置

|         名称          |    默认值    |           描述            |
|:-------------------:|:---------:|:-----------------------:|
| b23_default_command |  'B站热搜'   |          默认命令           |
|    b23_commands     | {'b23', } |           命令名           |
|      b23_block      |   False   |        是否阻止向下传播         |
|    b23_priority     |    99     |           优先级           |
|   b23_max_length    |    20     | 热搜数量(1~100)<br />推荐别设太高 |

## [依赖](requirements.txt)

* nonebot2[httpx]>=2.0.0
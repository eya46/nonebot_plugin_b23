# Bilibili热搜

## 默认命令

* b站热搜
* B站热搜
* b23

## 作用

获取B站热搜

## 安装

* nonebot2 2.0.0rc版本👇

> pip install nonebot-plugin-b23==0.0.8

* nonebot2 2.0.0正式版本👇

> pip install nonebot-plugin-b23==0.1.0

## 配置

|       名称       |       默认值       |    描述    |
|:--------------:|:---------------:|:--------:|
|  b23_commands  | {'b23', 'B站热搜'} |   命令名    |
|   b23_block    |      False      | 是否阻止向下传播 |
|  b23_priority  |       99        |   优先级    |
| b23_max_length |       21        |  最多热搜数量  |

## [依赖](requirements.txt)

* httpx~=0.23.0
* nonebot2~=2.0.0
* pydantic~=1.10.4
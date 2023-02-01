# Bilibili热搜

## 默认命令

* b站热搜
* B站热搜
* b23

## 作用

获取B站热搜

## 安装

pip install nonebot-plugin-b23==0.0.6

## 配置

|      名称      |       默认值       |    描述    |
|:------------:|:---------------:|:--------:|
| b23_commands | {'b23', 'B站热搜'} |   命令名    |
|  b23_block   |      False      | 是否阻止向下传播 |
| b23_priority |       99        |   优先级    |

## [依赖](requirements.txt)

* httpx~=0.23.0
* nonebot2>=2.0.0-beta.1
* pydantic~=1.10.4
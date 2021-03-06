import setuptools  # 导入setuptools打包工具

setuptools.setup(
    name="nonebot-plugin-b23",
    version="0.0.2",
    author="eya46",
    install_requires=[
        'httpx',
    ],
    author_email="eya46@qq.com",  # 作者联系方式，可写自己的邮箱地址
    description="nonebot2 plugin B站热搜",  # 包的简述
    long_description_content_type="text/markdown",
    url="https://github.com/eya46/nonebot_plugin_b23",  # 自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 对python的最低版本要求
)

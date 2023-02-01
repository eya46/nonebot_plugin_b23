import setuptools

setuptools.setup(
    name="nonebot-plugin-b23",
    version="0.0.6",
    author="eya46",
    install_requires=[
        'httpx~=0.23.0',
        'nonebot2>=2.0.0-beta.1',
        'pydantic~=1.10.4'
    ],
    author_email="eya46@qq.com",
    description="nonebot2 plugin B站热搜",  # 包的简述
    long_description_content_type="text/markdown",
    url="https://github.com/eya46/nonebot_plugin_b23",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)

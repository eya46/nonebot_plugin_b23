import setuptools

setuptools.setup(
    install_requires=[
        'httpx~=0.23.0',
        'nonebot2~=2.0.0',
        'pydantic~=1.10.4'
    ],
    author_email="eya46@qq.com",
    url="https://github.com/eya46/nonebot_plugin_b23",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)

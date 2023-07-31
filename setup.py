import setuptools

setuptools.setup(
    install_requires=[
        'nonebot2[httpx]>=2.0.0',
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

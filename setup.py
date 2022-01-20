import setuptools
with open("README.md", "r",encoding="utf-8",errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_weather_lite",
    version="0.0.1",
    author="zjkwdy",
    author_email="3377911508@qq.com",
    keywords=["pip", "nonebot2", "nonebot", "weather", "nonebot_plugin"],
    description="""使用wttr.in的天气查询 ，支持大部分wttr.in的用法。""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zjkwdy/nonebot_plugin_weather_lite",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=[
        "nonebot2 >= 2.0.0b1",
        "nonebot-adapter-onebot >= 2.0.0b1"
    ]
)
from setuptools import setup, find_packages

setup(
    name="yt_thumbnail_downloader",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="Pritam Kumar",
    author_email="pritamofficial7010@gmail.com",
    description="A library to download YouTube thumbnails by scraping video pages",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iconic1009/yt_thumbnail_downloader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

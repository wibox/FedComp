import os

from setuptools import find_packages, setup

if os.path.exists("./requirements.txt"):
    with open("./requirements.txt") as f:
        install_requires = f.read().splitlines()
else:
    install_requires = list()

setup(
    name="FedComp",
    version="0.0.1",
    author="Francesco Pagano",
    description="",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    python_requires="==3.13.*",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "fedcomp = fedcomp.__main__:main",
        ]
    },
)

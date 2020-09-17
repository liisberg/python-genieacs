from setuptools import setup

setup(
    name="python-genieacs",
    version="1.0",
    description="A Python API to interact with the GenieACS REST API",
    author="Oliver Kraitschy",
    packages=['python_genieacs'],
    url="https://github.com/TDT-AG/python-genieacs",
    license="GPL",
    install_requires=["requests"]
)


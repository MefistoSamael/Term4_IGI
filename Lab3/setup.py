# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="sir_Bychko_serializer",
    version="0.1.0",
    description="somme serialization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sir Bychko Vassiliy",
    author_email="vasa060504@mail.ru",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["sir_Bychko_serializer"],
    include_package_data=True,
    install_requires=["regex"]
)
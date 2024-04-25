import pathlib
from setuptools import setup, find_packages
from distutils.spawn import find_executable
import platform


def readme():
    with open('README.md') as f:
        return f.read()

dependencies = ['pyperclip', 'click', 'appdirs', 'daemonize']

if find_executable("fswatch") is None:
    if platform.system() == "Linux":
        dependencies.append("inotify")
    else:
        raise ValueError(
                "inkscape-figures needs fswatch to run on MacOS. You "
                "can install it using `brew install fswatch`"
                )

setup(
    name="inkscape-figures-wayland",
    version="1.0",
    description="Inkscape Figures for Wayland (Based on Gilles Castel\'s Inkscape Figures)",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/Zekkinity/Inkscape-Figures-Wayland',
    author="Zekk",
    author_email="zeth1316@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['inkscapefigures'],
    scripts=['bin/inkscape-figures'],
    install_requires=dependencies,
    include_package_data=True
)

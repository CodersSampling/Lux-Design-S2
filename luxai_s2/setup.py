import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="luxai_s2",
    version="2.0.0",
    author="Lux AI Challenge",
    description="The Lux AI Challenge Season 2",
    license="MIT",
    keywords="reinforcement-learning machine-learning ai",
    url="https://github.com/Lux-AI-Challenge/Lux-Design-S2",
    packages=find_packages(exclude="kits"),
    long_description=read("../README.md"),
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["luxai_s2 = luxai_runner.cli:main"]},
    install_requires=[
        "numpy",
        "pygame",
        "termcolor",
        "matplotlib",
        "pettingzoo",
        "vec_noise",
        "omegaconf",
        "gym==0.19",
        "scipy",
    ],
)

#!/usr/bin/env python3
from setuptools import find_packages, setup


dist = dict(
    name="adventofcode",
    use_scm_version=True,
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    url="https://github.com/QuicketSolutions/quicket_utils",
    license="All Rights Reserved",
    author="bchance",
    author_email="bhchance@gmail.com",
    description="Code used to solve https://adventofcode.com/",

)

if __name__ == "__main__":
    setup(**dist)

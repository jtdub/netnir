#!/usr/bin/env python3


import setuptools


setuptools.setup(
    name="netnir",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=[
        "pytest-runner",
        "nornir==2.4.0",
        "netmiko==2.4.2",
        "hier_config==v1.6.1",
        "keyring>=21.2.1",
        "keyrings.alt>=3.4.0",
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pytest-pep8",
        "pytest-black",
    ],
    python_requires=">=3.6",
    scripts = ["bin/netnir"],
)

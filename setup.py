# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="OpenFisca-Extension-Template",
    version="1.1.1",
    description="An OpenFisca extension that adds some variables to an already-existing tax and benefit system",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    author="",
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'OpenFisca-Country-Template >= 1.2.5,  < 2.0',
        ],
    extras_require = {
        'test': [
            'nose',
            ]
        },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)

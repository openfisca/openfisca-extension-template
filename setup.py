# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = "OpenFisca-Extension-Template",
    version = "1.3.4",
    author = "OpenFisca Team",
    author_email = 'contact@openfisca.org',
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Information Analysis",
        ],
    description = "An OpenFisca extension that adds some variables to an already-existing tax and benefit system",
    keywords = 'benefit microsimulation social tax',
    license = "http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    url = "https://github.com/openfisca/extension-template",
    include_package_data = True,  # Will read MANIFEST.in
    data_files = [
        ("share/openfisca/openfisca-extension-template", ["CHANGELOG.md", "LICENSE", "README.md"]),
        ],
    install_requires = [
        "OpenFisca-Country-Template >= 3.8.0,  < 4",
        ],
    extras_require = {
        "dev": [
            "autopep8 >= 1.5.4, < 2.0.0",
            "flake8 >= 3.8.0, < 4.0.0",
            "flake8-print >= 3.1.0, < 5.0.0",
            "pycodestyle >= 2.6.0, < 3.0.0",
            ]
        },
    packages = find_packages(),
    )

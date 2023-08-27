# -*- coding: utf-8 -*-
import pathlib
from setuptools import find_packages, setup

# packages = \
# ['jsonmask_ng', 'jsonmask_ng.tests']

# package_data = \
# {'': ['*']}

# setup_kwargs = {
#     'packages': packages,
#     'package_data': package_data,
#     'python_requires': '>=3.7, <3.12',
# }


HERE = pathlib.Path(__file__).parent

VERSION = '0.4.1'
PACKAGE_NAME = 'jsonmask_ng'
AUTHOR = 'Juan Garcia Longaron'
AUTHOR_EMAIL = 'juan.mobilife@gmail.com'
URL = 'https://github.com/juanyque/jsonmask_ng'

LICENSE = 'MIT'
DESCRIPTION = 'Implements the Google Partial Response protocol in Python'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'sys'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)

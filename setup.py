from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    requirements_list = []
    return requirements_list

setup (
name='sensor',
version="0.0.1",
author="vipul",
author_email="jainv9088@gmail.com",
packages=find_packages(),
install_requires = get_requirements(),

)
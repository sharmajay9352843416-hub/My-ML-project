from setuptools import find_packages, setup
from typing import List

hypen_E_Dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hypen_E_Dot in requirements:
            requirements.remove(hypen_E_Dot)

    return requirements

setup(
name = 'MY WEBSITE',
version = '0.0.1',
Author = 'Ajay',
Author_email = 'sharmajay9352843416@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    get_requirements=[]
    with open(file_path) as file_obj:
       requirements=file_obj.readline()
       requirements= [req.replace("\n","")for req in requirements]
       
       return requirements

setup(
    name="Diamond_price_prediction",
    version="0.0.1",
    author="Aryan",
    author_email="aryanprasadannonymous@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_required_packages(file_path:str)->List[str]:
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='marks prediction',
    version='0.0.1',
    author='Mohit',
    author_email='mohitmehndiratta.mm@gmail.com',
    packages=find_packages(),
    install_requires=get_required_packages('requirements.txt')
)
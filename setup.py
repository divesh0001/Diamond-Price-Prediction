from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_a:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name='Diamond Price Prediction',
    version='0.0.1',
    author='divesh',
    author_email='sainidivesh259@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)
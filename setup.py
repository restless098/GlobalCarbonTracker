# this file helps in setuping the package.....it make our model as  a package which can be downloadable from pypi
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .' # This is used to identify editable installs in requirements.txt
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='GlobalCarbonTracker',
    version='0.0.1',# Version of the package
    author='Mohammed Abdul Hafeez',
    author_email='abdulhafeezmohammed18@gmail.com',
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=get_requirements('requirements.txt'),  # Read dependencies from requirements.txt
    description='A package for tracking global carbon emissions and analyzing climate data.',
    long_description=open('README.md').read(),  # Read the long description from README file
)

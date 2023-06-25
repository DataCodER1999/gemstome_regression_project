from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath:str) -> List[str]:
    """
        This method will give list of all the 
        packages which are required to be installed 

    """
    requirements = []

    with open(filepath,"r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace("\n","") for r in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
        return requirements

setup(
    name="Gemstone_price_prediction",
    version="0.0.1",
    author="Nitin",
    author_email="malhotranitin771@gmail.com",
    install_requires = get_requirements('requirements.txt')
)
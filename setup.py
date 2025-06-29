from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements_list : List[str] = []
    try:
        with open("requirements.txt") as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt is not found")
    
    return requirements_list

print(get_requirements())
setup(
    name = "AI-Travel-Planner",
    version = "0.0.1",
    author = "Harish Narasimhan K",
    author_email = "harishnarasimhan0135@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
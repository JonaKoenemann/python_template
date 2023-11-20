from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.project_name }}',
    packages=find_packages(),
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_description }}',
    author='{{ cookiecutter.author }}',
    license='',
)

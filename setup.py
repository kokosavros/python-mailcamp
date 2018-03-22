from setuptools import setup, find_packages


setup(
    name='mailcamp',
    version='0.0.1',
    description='A python client for Mailcamp API',
    url='https://github.com/kokosavros/python-mailcamp',
    author='Mr Kokosavros',
    packages=find_packages(),
    install_requires=['requests'],
)
from setuptools import find_packages, setup

setup ( 
    name = 'FakeNewsTextCollections', 
    packages = find_packages(), 
    version = '1.1.0', 
    description = 'Library to use fakenews text collectins', 
    author = 'Marcos P. S. Gôlo',  
    install_requires = ['gdown', 'pandas', 'os', 'pathlib']
)

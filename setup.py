from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='This library was created to store recursion and sorting functions',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<RogatorM>/<my_package>',
    author='<Rogator Monama>',
    author_email='<rogator.monama1144@gmail.com>'
)

from setuptools import setup

with open('README-PyPi.txt', 'r') as README_file:
    long_description = README_file.read()

setup(
    name='PySliders',
    version='0.1',
    description='A sliders add-on for PyGame',
    license='MIT',
    long_description=long_description,
    author='Steven Shrewsbury',
    author_email='',
    url='https://github.com/stshrewsburyDev/PySliders',
    packages=['PySliders'],
    install_requires=['pygame']
)

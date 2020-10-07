import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()


setup(
    name='bitrix24-rest',
    version='0.1',
    packages=['client_bitrix',],
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    author_email='dimasbo.work@gmail.com',
    author='dimasbo',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python 3',
    ],

    )
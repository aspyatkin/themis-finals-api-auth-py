# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
import os


about = {}
about_filename = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'themis', 'finals', 'api', 'auth', '__about__.py')
with io.open(about_filename, 'rb') as fp:
    exec(fp.read(), about)


setup(
    name='themis.finals.api.auth',
    version=about['__version__'],
    description='Themis Finals API authentication helpers',
    author='Alexander Pyatkin',
    author_email='aspyatkin@gmail.com',
    url='https://github.com/aspyatkin/themis-finals-api-auth-py',
    license='MIT',
    packages=find_packages('.'),
    install_requires=[
        'setuptools>=0.8'
    ],
    namespace_packages=[
        'themis',
        'themis.finals',
        'themis.finals.api'
    ]
)

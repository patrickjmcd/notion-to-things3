# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='notion-things3',
    version='0.1.0',
    install_requires=['notion>=0.0.21', 'python-dotenv>=0.10.1'],
    description='Syncs Notion tasks to Things3',
    long_description=readme,
    author='Patrick McDonagh',
    author_email='patrickjmcd@gmail.com',
    url='https://github.com/patrickjmcd/notion-things3',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': ['notion-things3=notion_to_things:main'],
    }
)

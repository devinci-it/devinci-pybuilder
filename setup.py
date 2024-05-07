from setuptools import setup, find_packages
from setuptools.command.install import install
import os
from typing import Type
from devinci_pybuilder.build_chores.custom_install_command import CustomInstallCommand

setup(
    name='devinci-pybuilder',
    version='0.0.3',
    description='devinci_pybuilder is a Python package builder for managing project setup and generating setup.py files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    author='devinci-it',
    packages=find_packages(),
    scripts=['devinci_pybuilder/builder.py', 'devinci_pybuilder/file_utils.py', 'devinci_pybuilder/main.py'],
    entry_points={'console_scripts': ['devinci_pybuild=devinci_pybuilder.main:main']},
    setup_requires=['setuptools', 'wheel'],
    install_requires=[
        'devinci_pyutils'
        ],
    package_data={
        'devinci_pybuilder': ['stub/*']
    },
    dependency_links=[
        'file://./devinci_pybuilder/build_chores'
    ],
    cmdclass={
        'install': CustomInstallCommand
    }

)

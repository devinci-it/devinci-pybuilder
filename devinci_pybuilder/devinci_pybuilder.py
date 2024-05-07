
"""
devinci_pybuilder: A Python package builder for managing project setup and generation of setup.py files.

This module provides utilities for managing project setup and generating setup.py files for Python packages. It allows developers to define project configurations in a `config.ini` file and generate setup.py files based on these configurations.

The module includes the following functionalities:

1. Parsing of configurations from a `config.ini` file:
   - Basic build information such as name, version, description, license, and author.
   - Scripts to be included in the package.
   - Entry points for console scripts.
   - Requirements from a `requirements.txt` file.

2. Generation of a setup.py file based on the parsed configurations.

Usage:
1. Define project configurations in the `config.ini` file.
2. Use the provided functions to parse these configurations and generate setup.py files.

Example:
    ```
    # Read project configurations from config.ini and generate setup.py
    setup_py_content = generate_setup_py()
    ```

Note:
- Ensure that the `config.ini` file and `requirements.txt` file are present in the project directory.
- Customize the configurations in the `config.ini` file according to the project requirements.
"""


import configparser
from typing import List, Dict
from devinci_pyutils import banner
def _read_config_section(config_file: str = 'config.ini', section: str = 'General') -> Dict[str, str]:
    """
    Read a specific section from the configuration file and return it as a dictionary.

    Args:
        config_file (str): Path to the configuration file. Default is 'config.ini'.
        section (str): Name of the section to read from the configuration file. Default is 'General'.

    Returns:
        Dictionary containing the key-value pairs from the specified section.
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    if section in config:
        return dict(config[section])
    else:
        return {}

def _parse_scripts_from_config(config_file: str = 'config.ini') -> List[str]:
    """
    Parse scripts from the configuration file.

    Args:
        config_file (str): Path to the configuration file. Default is 'config.ini'.

    Returns:
        List of script paths.
    """
    config = _read_config_section(config_file, 'Scripts')
    return list(config.values())


def _parse_entry_points_from_config(config_file: str) -> Dict[str, List[str]]:
    """
    Parse entry points from the specified section of the configuration.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        Dictionary of entry points.
    """
    config = configparser.ConfigParser()
    config.read(config_file)

    entry_points = {}
    if 'ConsoleScripts' in config:
        entry_points['console_scripts'] = []
        for name in config['ConsoleScripts']:
            command = config['ConsoleScripts'][name]
            mod_rel_path, function = command.split(':')
            entry_points['console_scripts'].append(f"{name}={mod_rel_path}:{function}")

    return entry_points



def _parse_requirements_from_file(requirements_file: str = 'requirements.txt') -> List[str]:
    """
    Parse requirements from the requirements file.

    Args:
        requirements_file (str): Path to the requirements file. Default is 'requirements.txt'.

    Returns:
        List of requirement strings.
    """
    with open(requirements_file, 'r') as f:
        requirements = f.readlines()
    return [req.strip() for req in requirements]

def _parse_build_info(config_file: str = 'config.ini') -> Dict[str, str]:
    """
    Parse basic build information from the configuration.

    Args:
        config_file (str): Path to the configuration file. Default is 'config.ini'.

    Returns:
        Dictionary containing the basic build information.
    """
    return _read_config_section(config_file, 'Build')

def generate_setup_py(config_file: str = 'config.ini') -> str:
    """
    Generate a setup.py file based on the configuration.

    Args:
        config_file (str): Path to the configuration file. Default is 'config.ini'.

    Returns:
        String containing the content of the setup.py file.
    """
    build_info: Dict[str, str] = _parse_build_info(config_file)
    scripts: List[str] = _parse_scripts_from_config(config_file)
    entry_points: Dict[str, str] = _parse_entry_points_from_config(config_file)
    requirements: List[str] = _parse_requirements_from_file()

    setup_py_content = f'''
from setuptools import setup, find_packages

setup(
    name='{build_info.get('name', 'homepip_server')}',
    version='{build_info.get('version', '1.0')}',
    description='{build_info.get('description', '')}',
    long_description=open('{build_info.get('long_description', 'README.md')}').read(),
    license='{build_info.get('license', 'MIT')}',
    author='{build_info.get('author', '')}',
    packages=find_packages(),
    scripts={scripts},
    entry_points={entry_points},
    install_requires={requirements},
    setup_requires=['setuptools', 'wheel'],

)
'''
    return setup_py_content.strip()


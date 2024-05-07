"""
Devinci-PyBuilder

Devinci-PyBuilder is a Python package designed to simplify the setup and building process of Python projects. It provides a set of modular functions for generating setup.py files, building distributions, and installing packages, streamlining the workflow for developers.

Features:
- Automatically generate setup.py files based on provided configuration data.
- Build source distributions (sdist) and wheel distributions (bdist_wheel) with a single command.
- Optionally install the built package using pip or pipenv.

Usage:
1. Configure your project settings in the config.ini file.
2. Run the build.py script to generate setup.py and build distributions.
3. Optionally install the built package using pip or pipenv.

Module Documentation:
- build.py: Main script for generating setup.py and building distributions.
- config.ini: Configuration file for project settings.
- setup.py: Generated setup.py file based on config.ini.
- README.md: README file containing project documentation.

For detailed usage instructions and examples, refer to the README.md file.

Dependencies:
- Python 3.6+
- setuptools

License:
This project is licensed under the MIT License. See the LICENSE file for details.
"""
import os
import subprocess

def check_setup_py_exists():
    """
    Check if a setup.py file already exists.

    Returns:
        bool: True if setup.py exists, False otherwise.
    """
    return os.path.exists('setup.py')

def prompt_overwrite_setup_py():
    """
    Prompt the user whether to overwrite an existing setup.py file.

    Returns:
        bool: True if the user wants to overwrite, False otherwise.
    """
    overwrite_choice = input("A setup.py file already exists. Do you want to overwrite it? (y/n): ").lower()
    return overwrite_choice == 'y'

def generate_setup_py(config_data):
    """
    Generate a setup.py file based on the provided configuration data.

    Args:
        config_data (str): Configuration data to include in the setup.py file.
    """
    setup_template = f"""
from setuptools import setup, find_packages

setup(
{config_data}
)
"""
    with open('setup.py', 'w') as f:
        f.write(setup_template)

def run_build_commands():
    """Run commands to build distributions."""
    subprocess.run(['python', 'setup.py', 'sdist', 'bdist_wheel'])

def prompt_install_package():
    """Prompt the user whether to install the package."""
    install_choice = input("Package built successfully. Do you want to install it now? (y/n): ").lower()
    return install_choice == 'y'

def install_package(install_type):
    """
    Install the package using pip or pipenv.

    Args:
        install_type (str): The package manager to use ('pip' or 'pipenv').
    """
    if install_type == 'pip':
        subprocess.run(['pip', 'install', '-e', '.'])
    elif install_type == 'pipenv':
        subprocess.run(['pipenv', 'install', '-e', '.'])
    else:
        print("Invalid choice. Package not installed.")

def build(config_file='config.ini'):
    """
    Build the package using the provided configuration file.

    Args:
        config_file (str): Path to the configuration file. Default is 'config.ini'.
    """
    if check_setup_py_exists():
        if not prompt_overwrite_setup_py():
            print("Skipping setup.py generation.")
            run_build_commands()  # Attempt to run build using existing setup.py
            return

    # Read configuration from config file
    with open(config_file, 'r') as f:
        config_data = f.read()

    # Generate setup.py
    generate_setup_py(config_data)

    # Run build commands
    run_build_commands()

    # Prompt to install package
    if prompt_install_package():
        install_type = input("Do you want to install with pip or pipenv? (pip/pipenv): ").lower()
        install_package(install_type)

if __name__ == "__main__":
    build()

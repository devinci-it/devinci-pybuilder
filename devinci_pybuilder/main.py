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

import os
import shutil
import argparse
from devinci_pyutils import banner,write_cautious,copy
from devinci_pybuilder import generate_setup_py

# Default path for the global template configuration file
DEFAULT_GLOBAL_TEMPLATE_CONFIG = os.path.expanduser("~/.devinci_pybuilder/templates/global_config.ini")
TEMPLATE_DIR = os.path.expanduser("~/.devinci_pybuilder/templates/")

def generate_setup(config_file: str = 'config.ini', output_file: str = None) -> str:
    """
    Generate a setup.py file based on the configuration.

    Args:
        config_file (str): Path to the configuration file. Default is 'config.ini'.
        output_file (str): Path to the output file. If None, the setup.py content is returned as a string.

    Returns:
        str: If output_file is None, returns the content of the setup.py file as a string. Otherwise, returns None.
    """
    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Config file '{config_file}' does not exist.")

    # Generate setup.py content
    setup_py_content = generate_setup_py(config_file)

    # If output_file is specified, write the content to the file
    if output_file:
        write_cautious(os.getcwd(),setup_py_content)
    else:
        return setup_py_content

def create_config_template(args):
    """
    Create a sample config.ini template.

    Args:
        args (argparse.Namespace): Parsed arguments from the command-line.
    """
    output_file = args.output_file or 'config.ini'  # Default to 'config.ini' if output_file is not specified
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Construct the path to the example-config.ini file
    stub_dir = os.path.join(script_dir, 'stub')
    example_config_path = os.path.join(stub_dir, 'example-config.ini')

    if not os.path.isfile(example_config_path):
        raise FileNotFoundError(f"Example config file '{example_config_path}' not found.")

    # Copy the contents of the example-config.ini file to the output file

    copy(example_config_path, output_file)


def integration_task(config_file: str):
    """
    Integration task to check existence of README.md and requirements.txt,
    create them if not present, call generate_setup_py, and then delete them if newly created.

    Args:
        config_file (str): Path to the configuration file (config.ini).
    """
    # Check if README.md exists, if not, create it
    print('')
    if not os.path.isfile('README.md'):
        with open('README.md', 'w'):
            pass

    # Check if requirements.txt exists, if not, create it
    if not os.path.isfile('requirements.txt'):
        with open('requirements.txt', 'w'):
            pass

    # Call generate_setup_py
    generate_setup_py(config_file)

    # Delete README.md and requirements.txt if newly created
    if not os.path.isfile(os.path.join(os.getcwd(), 'README.md')):
        os.remove('README.md')
    if not os.path.isfile(os.path.join(os.getcwd(), 'requirements.txt')):
        os.remove('requirements.txt')

def main():
    """
    Main function to handle command-line arguments and execute corresponding actions.
    """
    parser = argparse.ArgumentParser(description="Utility for generating setup.py using Devinci PyBuilder.")

    # Subcommand for generating setup.py
    subparsers = parser.add_subparsers(title='Subcommands', dest='subcommand')
    parser_generate = subparsers.add_parser('generate', help='Generate setup.py from config.ini')
    parser_generate.add_argument("config_file", help="Path to the configuration file (config.ini)")
    parser_generate.add_argument("--integration-task", action='store_true', help="Perform integration task to check existence of README.md and requirements.txt, create them if not present, call generate_setup_py, and then delete them if newly created.")
    parser_generate.add_argument("--output-file", help="Path to the output file for the generated setup.py")
    parser_generate.set_defaults(func=generate_setup)

    # Subcommand for creating config.ini template
    parser_template = subparsers.add_parser('template', help='Create a sample config.ini template')
    parser_template.add_argument("--output-file", help="Path to the output file for the generated config.ini")
    parser_template.set_defaults(func=create_config_template)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        if args.subcommand == 'generate':
            if args.integration_task:
                integration_task(args.config_file)
            else:
                args.func(args.config_file, args.output_file)
        elif args.subcommand == 'template':
            args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

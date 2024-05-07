# Devinci-PyBuilder

Devinci-PyBuilder is a Python package designed to simplify the setup and building process of Python projects. It provides a set of modular functions for generating setup.py files, building distributions, and installing packages, streamlining the workflow for developers.

## Features

- Automatically generate setup.py files based on provided configuration data.
- Build source distributions (sdist) and wheel distributions (bdist_wheel) with a single command.
- Optionally install the built package using pip or pipenv.

## Usage

1. **Configuration**: Configure your project settings in the `config.ini` file.
2. **Build**: Run the `build.py` script to generate `setup.py` and build distributions.
3. **Installation** (Optional): Install the built package using pip or pipenv.

## Module Documentation

- **build.py**: Main script for generating `setup.py` and building distributions.
- **config.ini**: Configuration file for project settings.
- **setup.py**: Generated `setup.py` file based on `config.ini`.
- **README.md**: README file containing project documentation.

For detailed usage instructions and examples, refer to the README.md file.

## Dependencies

- Python 3.6+
- setuptools

## License

This project is licensed under the MIT License. See the LICENSE file for details.

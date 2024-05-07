import os
import shutil
from setuptools.command.install import install


def create_banner(text: str) -> str:
    """
    Create a  banner with a given text.

    Args:
        text (str): The text to display in the banner.

    Returns:
        str: The generated banner as a string.
    """
    border = "_" * 70  # Adjust the number of underscores to change the length of the banner
    banner = f"{border}\n|{' ' * 68}|\n|{text.center(68)}|\n|{' ' * 68}|\n{border}"
    return banner



class CustomInstallCommand(install):

    """
    Custom installation command for Devinci PyBuilder.

    This command extends the setuptools 'install' command to perform additional tasks
    during the installation process. It creates necessary directories and copies
    configuration files to the appropriate locations.

    Attributes:
        home_dir (str): The user's home directory.
        devinci_pybuilder_dir (str): The directory path for Devinci PyBuilder configuration.
        templates_dir (str): The directory path for storing templates.
        globals_dir (str): The directory path for storing global configurations.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the CustomInstallCommand with necessary directory paths.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.home_dir = os.path.expanduser("~")
        self.devinci_pybuilder_dir = os.path.join(self.home_dir, ".devinci_pybuilder")
        self.templates_dir = os.path.join(self.devinci_pybuilder_dir, "templates")
        self.globals_dir = os.path.join(self.devinci_pybuilder_dir, "globals")

    def run(self):
        """
        Overrides the run method of the install command.

        Performs the standard installation and then executes the custom tasks.
        """
        install.run(self)
        print(create_banner("Performing custom tasks during installation"))
        self.perform_custom_task()

    def perform_custom_task(self):
        """
        Performs custom tasks during installation.

        This method creates necessary directories and copies configuration files.
        """
        print(create_banner("Creating directories and copying configuration files"))
        self.create_directories([self.templates_dir, self.globals_dir])
        self.copy_config_file()

    def create_directories(self, directories):
        """
        Creates directories if they don't exist.

        Args:
            directories (list): List of directory paths to create.
        """
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)

    def copy_config_file(self):
        """
        Copies the example-config.ini file to the templates directory.
        """
        print(create_banner("Copies the example-config.ini file to the templates directory."))

        example_config_src = os.path.join(os.path.dirname(__file__), "stub", "example-config.ini")
        example_config_dest = os.path.join(self.templates_dir, "config.ini")
        if not os.path.exists(example_config_dest):
            shutil.copy(example_config_src, example_config_dest)




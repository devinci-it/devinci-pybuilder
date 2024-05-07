"""
Module for handling file and directory creation dynamically.
"""

import os
import argparse

def create_directory(directory):
    """
    Create a directory if it doesn't exist.

    Args:
        directory (str): Path to the directory.

    Returns:
        None
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")

def create_file(file_path, content=None):
    """
    Create a file if it doesn't exist.

    Args:
        file_path (str): Path to the file.
        content (str, optional): Content to write to the file. Defaults to None.

    Returns:
        None
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            if content:
                f.write(content)
        print(f"File '{file_path}' created.")

def main(args):
    """
    Main function to handle file and directory creation.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.
    """
    if args.dir:
        create_directory(args.dir)
    
    if args.file:
        create_file(args.file, args.content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utility for creating files and directories dynamically.")
    parser.add_argument("--dir", help="Path to the directory to create.")
    parser.add_argument("--file", help="Path to the file to create.")
    parser.add_argument("--content", help="Content to write to the file.")
    args = parser.parse_args()
    main(args)

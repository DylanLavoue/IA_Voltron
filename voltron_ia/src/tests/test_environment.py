"""
This module is a script that checks the Python version and virtual
environment for a project. It imports the `sys` module to get information
about the current Python environment.
"""
import sys


def main():
    """
    Check the Python version and virtual environment for this project.

    Raises:
        TypeError: If the Python version is not 3.9 or
            if the virtual environment is not 'zoidberg_env'.

    Returns:
        None
    """
    system_major = sys.version_info.major
    system_minor = sys.version_info.minor
    if system_major != 3 and system_minor != 9:
        raise TypeError(
            "This project requires Python 3.9. Found: Python {}".format(
                sys.version
                )
        )
    else:
        if "voltron_ia" not in sys.prefix:
            raise TypeError(
                "This project requires 'voltron_ia' environment. Activate it"
            )
        print(">>> Environment checked ")


if __name__ == '__main__':
    main()
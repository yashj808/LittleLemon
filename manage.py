#!/usr/bin/env python
# This shebang line indicates that the script should be executed using the python interpreter found in the user's environment.

"""Django's command-line utility for administrative tasks."""
# This is a command-line utility that lets you interact with your Django project.
# You can use it to do things like run the development server, create database tables, and more.

import os
import sys


def main():
    """Run administrative tasks."""
    # The DJANGO_SETTINGS_MODULE environment variable tells Django which settings file to use.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Littlelemon.settings')
    try:
        # The execute_from_command_line function is responsible for executing the command that was passed to the script.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # This error is raised if Django is not installed or not available on the Python path.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # The sys.argv list contains the command-line arguments that were passed to the script.
    # The first argument is the name of the script itself.
    # The rest of the arguments are the command and its arguments.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # This is a common Python construct that ensures that the main() function is only called when the script is executed directly.
    # If the script is imported as a module into another script, the main() function will not be called.
    main()
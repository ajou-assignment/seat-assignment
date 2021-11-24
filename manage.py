#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # React project 실행
    try:
        if len(sys.argv) > 2:
            if sys.argv[2] == 'react':
                project_root = os.getcwd()
                os.chdir(os.path.join(project_root, "frontend"))
                
                if len(sys.argv) > 3:
                    if sys.argv[3] == 'start':
                        os.system("npm start")
                    elif sys.argv[3] == 'build':
                        os.system("npm run build")
                    else:
                        print("wrong npm command, run on develop mode")
                        os.system("npm start")
                    sys.argv.pop(3)
                else:
                    os.system("npm run build")

                    os.chdir(project_root)
                    sys.argv.pop(2)
    except IndexError:
        execute_from_command_line(sys.argv)
    else:
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
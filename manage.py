#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    # Ensure the logs directory exists to avoid errors when Django logging
    # attempts to write to the file handler configured in settings.
    project_root = Path(__file__).resolve().parent
    logs_dir = project_root / 'logs'
    try:
        logs_dir.mkdir(parents=True, exist_ok=True)
    except Exception:
        # Best-effort: if directory creation fails, continue so manage.py remains usable
        pass

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

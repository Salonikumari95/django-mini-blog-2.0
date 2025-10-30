#!/usr/bin/env python3
import os
import sys

def main():
    """Project start hone ka entry point"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

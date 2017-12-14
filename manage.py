#!/usr/bin/env python
import os
import socket
import sys

if __name__ == "__main__":
    if socket.gethostname() == 'QAIMint':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'scorecard.settings.dev_heyden')
    elif socket.gethostname() == "mohan-HP-Compaq-6005-Pro-SFF-PC":
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecard.settings.dev_mohan')
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scorecard.settings.base")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

#!/usr/bin/python3
"""Fabric script to delete out-of-date archives"""

from fabric.api import *
from datetime import datetime

env.hosts = ['34.229.66.234', '54.242.158.33']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_clean(number=0):
    """Deletes out-of-date archives"""
    try:
        number = int(number)
        if number < 0:
            number = 0

        local_archives = sorted(local("ls -1 versions", capture=True).split())
        web_server_archives = sorted(run(
            "ls -1 /data/web_static/releases", capture=True).split())

        for archive in local_archives[:-number]:
            local("rm -f versions/{}".format(archive))

        for archive in web_server_archives[:-number]:
            run("rm -f /data/web_static/releases/{}".format(archive))

        return True
    except Exception:
        return False

#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from the contents of web_static"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of web_static"""
    try:
        local("mkdir -p versions")

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_filename = "web_static_{}.tgz".format(timestamp)

        local("tar -cvzf versions/{} web_static".format(archive_filename))

        return os.path.abspath("versions/{}".format(archive_filename))
    except Exception:
        return None

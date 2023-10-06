#!/usr/bin/python3
"""Fabric script to create and distribute an archive to web servers"""

from fabric.api import *
from os.path import exists
from os import makedirs
from datetime import datetime

env.hosts = ['34.229.66.234', '54.242.158.33']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """Generates a .tgz archive from the contents of web_static"""
    try:
        local("mkdir -p versions")

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_filename = "web_static_{}.tgz".format(timestamp)

        local("tar -cvzf versions/{} web_static".format(archive_filename))

        return "versions/{}".format(archive_filename)
    except Exception:
        return None


def do_deploy(archive_path):
    """Distributes and deploys an archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        archive_filename = archive_path.split("/")[-1]
        archive_folder = archive_filename.replace(".tgz", "")
        releases_folder = "/data/web_static/releases"
        new_release_path = "{}/{}".format(releases_folder, archive_folder)

        run("mkdir -p {}".format(new_release_path))
        run("tar -xzf /tmp/{} -C {}"
            .format(archive_filename, new_release_path))

        run("rm /tmp/{}".format(archive_filename))

        current_symlink = "/data/web_static/current"
        run("rm -rf {}".format(current_symlink))
        run("ln -s {} {}".format(new_release_path, current_symlink))

        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

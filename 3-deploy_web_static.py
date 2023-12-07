#!/usr/bin/python3
'''
    Fabric script that generates a .tgz archive from
    the contents of the web_static folder
'''
from fabric.api import local, run, put, env
from datetime import datetime
from os.path import exists, isdir
env.hosts = ["54.235.193.23", "	54.209.125.126"]


def do_pack():
    ''' pack the contents of web_static folder '''
    current_date = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = "web_static_" + current_date + ".tgz"

    local("mkdir -p versions")
    folder_path = f"versions/{archive_name}"
    try:
        local(f"tar -cvzf {folder_path} web_static")
        return folder_path
    except Exception:
        return None


def do_deploy(archive_path):
    ''' deploy archive to servers '''
    if exists(archive_path) is False:
        return False
    try:
        file_path = archive_path.split("/")[-1]
        file_name = file_path.split(".")[0]
        des_path = "/data/web_static/releases/"
        put(archive_path, f"/tmp/")
        run(f"mkdir -p {des_path}/{file_name}")
        run(f"tar -xzf /tmp/{file_path} -C {des_path}/{file_name}/")
        run(f"rm /tmp/{file_path}")
        run(f'mv {des_path}/{file_name}/web_static/* {des_path}/{file_name}/')
        run(f'rm -rf {des_path}/{file_name}/web_static')
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {des_path}/{file_name}/ /data/web_static/current")
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

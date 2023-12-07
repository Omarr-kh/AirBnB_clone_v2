#!/usr/bin/python3
'''
    Deploy web_static on Servers
'''
from fabric.api import run, put, env, local
import os
from datetime import datetime

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
    '''Distribute an archive to our web servers'''

    try:
        if not os.path.isfile(archive_path):
            return False
        file_path = archive_path.split('/')[-1]  # web_static_xxxxxx.tgz
        name = file_path.split('.')[0]  # web_static_xxxxxx
        r_path = '/data/web_static/releases'

        put(archive_path, f'/tmp/{file_path}')
        run(f'mkdir -p {r_path}/{name}/')
        run(f'tar -xzf /tmp/{file_path} -C {r_path}/{name}/')
        run(f'rm /tmp/{file_path}')
        run(f'mv {r_path}/{name}/web_static/* {r_path}/{name}/')
        run(f'rm -rf {r_path}/{name}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {r_path}/{name}/ /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception as e:
        return False

from fabric.api import *

env.use_ssh_config = False

# Hosts to deploy onto
env.hosts = ['kiwifoto.se']
env.user = 'ikiwi'
env.key_filename = '~/.ssh/kiwi/kiwi_rsa'

# Where your project code lives on the server
env.project_root = '/Library/WebServer/Documents/gbc.kiwifoto.se/gbc'

env.repo = 'https://github.com/kiwiholmberg/gbc.git'

def deploy():
    git_pull()
    collect_static()
    restart_server()

def collect_static():
    with cd(env.project_root):
        sudo('python gbc/manage.py collectstatic -v0 --noinput')

def restart_server():
    with cd(env.project_root):
        sudo('/opt/local/apache2/bin/apachectl restart')

def git_pull():
    with cd(env.project_root):
        run('git pull %s' % env.repo)

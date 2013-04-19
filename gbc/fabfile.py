from fabric.api import *

env.use_ssh_config = False

# Hosts to deploy onto
env.hosts = ['kiwifoto.se']
env.user = 'ikiwi'
env.key_filename = '~/.ssh/kiwi/kiwi_rsa'

# Where your project code lives on the server
env.project_root = '/Library/WebServer/Documents/gbc.kiwifoto.se/gbc'

env.repo = 'https://github.com/kiwiholmberg/gbc.git'

def deploy(sql='no'):
    git_pull()
    collect_static()
    if sql == 'yes':
        db_changes()
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

def db_changes():
    with cd(env.project_root):
        run('$NOW = date')
        run('cp db/gbc_db db/gbc_db_$NOW') #backup
        run('sqlite3 db/gbc_db < change.sql')


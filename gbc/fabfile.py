from fabric.api import *

env.use_ssh_config = False
import time

# Hosts to deploy onto
env.hosts = ['kiwifoto.se']
env.user = 'ikiwi'
env.key_filename = '~/.ssh/kiwi/kiwi_rsa'

# Where your project code lives on the server
env.project_root = '/Library/WebServer/Documents/gbc.kiwifoto.se/gbc'

env.repo = 'https://github.com/kiwiholmberg/gbc.git'

def deploy(sql='no'):
    remove_settings()
    git_pull()
    production_settings()
    collect_static()
    if sql == 'yes':
        print 'Running sql script'
        db_changes()
    restart_server()

def collect_static():
    with cd(env.project_root):
        sudo('python gbc/manage.py collectstatic -v0 --noinput')

def restart_server():
    with cd(env.project_root):
        sudo('/opt/local/apache2/bin/apachectl stop')
        sleep(4)
        sudo('/opt/local/apache2/bin/apachectl start')

def git_pull():
    with cd(env.project_root):
        run('git pull %s' % env.repo)

def db_changes():
    with cd(env.project_root):
        run('cp gbc/db/gbc_db gbc/db/gbc_db_'+str(time.time())) #backup
        run('sqlite3 gbc/db/gbc_db < gbc/change.sql')

def production_settings():
    with cd(env.project_root):
        run('rm gbc/gbc/settings.py')
        run('cp gbc/gbc/settings-production.py gbc/gbc/settings.py')

def remove_settings():
    with cd(env.project_root):
        run('mv gbc/gbc/settings.py gbc/gbc/settings'+ str(time.time()) + '.py')
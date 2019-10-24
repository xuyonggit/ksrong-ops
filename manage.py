from flask_script import Manager, Server
from utils.functions import create_app

app = create_app()

manage = Manager(app=app)
manage.add_command('run', Server(host='0.0.0.0', port=5000))

if __name__ == '__main__':
    manage.run()
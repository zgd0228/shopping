from App import create_app
from App.models import *
from flask_script import Manager,Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app()
migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    manager.run()
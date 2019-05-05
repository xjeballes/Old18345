import unittest, psycopg2
from sqlalchemy import func, exc
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import blueprint
from app.main import create_app, db
from app.main.setup_db import setup_petKindList
from app.main.models.specie import Specie
from app.main.models.breed import Breed

app = create_app("dev")
app.register_blueprint(blueprint)
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

@manager.command
def run():
    try:
        x = db.session.query(func.count(Specie.id)).scalar()
        y = db.session.query(func.count(Breed.id)).scalar()

        if x and y != 0:
            app.run()
        else:
            try:
                setup_petKindList()

                app.run()
                
            except ValueError:
                print("Read carefully and input what is required. Try again.")


    except exc.OperationalError:
        print("Create the databases first.")

    except exc.ProgrammingError:
        print("Please migrate your models to the databases.")

@manager.command
def test():
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0

    return 1

if __name__ == "__main__":
    manager.run()

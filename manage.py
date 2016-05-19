#!/usr/bin/env python3
import os

try:
    # This is redundant, we can use try catch to test
    # if a package's existence.
    # if os.environ.get('FLASK_COVERAGE', None):
    #     import coverage
    #
    #     COV = coverage.coverage(branch=True, include='apps/*')
    #     COV.start()
    import coverage
    COV = coverage.coverage(branch=True, include='apps/*')
except ImportError:
    coverage = COV = None

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from apps import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# This import must be put behind app initialization to avoid TypeError because
# `register_blueprints` function uses app logger which requires app to be
# created first.
from apps.common.utils.initialize import load_models, register_blueprints  # NOQA

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test(coverage=False):
    """Run the unit tests."""
    if coverage:
        import sys
        os.execvp(sys.executable, [sys.executable] + sys.argv)

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()


@manager.command
def profile(length=25, profile_dir=None):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                      profile_dir=profile_dir)
    app.run()


@manager.command
def deploy():
    """Run deployment tasks."""
    from flask.ext.migrate import upgrade
    from app.models import Role, User

    # migrate database to latest revision
    upgrade()

    # create user roles
    Role.insert_roles()

    # create self-follows for all users
    User.add_self_follows()


if __name__ == '__main__':
    load_models()
    register_blueprints()
    manager.run()

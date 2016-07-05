#!/usr/bin/env python3
import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand, upgrade
from apps.asset.models import Asset, AssetGroup, Tag, IDC

from apps import create_app, db

app = create_app('default')

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
    db.create_all()
    idc = IDC(name='chinanet')
    group = AssetGroup(name='group01')
    tag_rows = [Tag(key=u'设备类型', value=u'物理机'), Tag(key=u'设备类型', value=u'虚拟机'),
                Tag(key=u'系统类型', value='CentOS'), Tag(key=u'系统类型', value='Ubuntu'),
                Tag(key='环境', value='生产'), Tag(key=u'环境', value='测试'),
                Tag(key=u'品牌', value='Dell'), Tag(key=u'品牌', value='HP'),
                Tag(key=u'状态', value='上线'), Tag(key=u'状态', value='下线'), Tag(key=u'状态', value='报废'),
                Tag(key=u'平台', value='x86_64'), Tag(key=u'平台', value='x86'),
                Tag(key=u'数据库', value='数据库'), Tag(key=u'网站', value='网站')]
    db.session.add_all([idc, group])
    db.session.bulk_save_objects(tag_rows)
    db.session.commit()


if __name__ == '__main__':
    manager.run()

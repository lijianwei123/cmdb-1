# -*- coding:utf-8 -*-
import importlib
import os
import pkgutil

from flask import Blueprint

import config
from apps import app
from apps.common.logging import get_logger

root_app_dir = os.path.join(config.basedir, "apps")


def load_models(app_package_path=root_app_dir) -> list:
    """Auto load all database models named `models` in packages under apps.
       Use this function before calling db creation methods to avoid
       getting no table creations results.

       `Note`: I'm using function annotation for better type hint in IDE.

       :param app_package_path root app path for detecting SQLAlchemy models
       :type app_package_path str or unicode

       :return model list detected
       :rtype list
    """
    models = []
    models_modules = filter(lambda m: m[1].endswith('.models'),
                            pkgutil.walk_packages(app_package_path))

    for _, module_name, _ in models_modules:
        model_module = importlib.import_module(module_name)
        model_defs = map(lambda x: getattr(model_module, x),
                         [att for att in dir(model_module)
                          if type(getattr(model_module, att)) == type(db.Model)])  # NOQA
        models.extend(model_defs)

    return models


def register_blueprints(app_package_path=root_app_dir):
    app_package_path = "./" + app_package_path
    """Automatically register all blueprints in all `views.py` in packages under apps.

       :param app_package_path root app path for detecting SQLAlchemy models
       :type app_package_path str or unicode
    """
    view_modules = filter(lambda m: m[1].endswith('.views'),
                          pkgutil.walk_packages(app_package_path))

    for _, module_name, _ in view_modules:
        view_module = importlib.import_module(module_name)
        try:
            blueprint = view_module.blueprint
            assert isinstance(blueprint, Blueprint), "`blueprint` is not a Flask Blueprint object!"
            app.register_blueprint(blueprint)
        except AttributeError:
            logger = get_logger()
            logger.warning("No blueprint in view: {0}".format(module_name))
        except AssertionError as e:
            logger = get_logger()
            logger.error(e.message)

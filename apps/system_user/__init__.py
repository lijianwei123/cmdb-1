from flask import Blueprint

asset = Blueprint(name='system_user', import_name=__name__, url_prefix='/system_user')

from . import views, models

from flask import Blueprint
system_user = Blueprint(name='system_user', import_name=__name__, url_prefix='/system_user')

from . import views, models



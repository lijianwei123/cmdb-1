from flask import Blueprint

asset = Blueprint(name='asset', import_name=__name__, url_prefix='/asset')

from . import views, models

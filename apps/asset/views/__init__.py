from flask import Blueprint

blueprint = Blueprint(name='asset', import_name=__name__, url_prefix='/asset')

from . import asset

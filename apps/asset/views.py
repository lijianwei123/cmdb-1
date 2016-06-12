# -*- coding:utf-8 -*-
from . import blueprint


@blueprint.route('/add', methods=['GET'])
def asset_add():
    return 'asset add.'

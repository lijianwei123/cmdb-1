# -*- coding:utf-8 -*-
from . import blueprint


@blueprint.route('/add', methods=['GET'])
def asset_add():
    return 'asset add.'


@blueprint.route('/edit', methods=['GET'])
def asset_edit():
    return 'asset edit.'


@blueprint.route('/del', methods=['GET'])
def asset_del():
    return 'asset del.'


@blueprint.route('/list', methods=['GET'])
def asset_list():
    return 'asset list.'

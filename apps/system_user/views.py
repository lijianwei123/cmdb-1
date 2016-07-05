# -*- coding:utf-8 -*-

from flask import jsonify, abort, url_for, request
from . import system_user


@system_user.route('/add', methods=['POST'])
def system_user_add():
    """
    增加系统用户
    :return:
    """
    pass

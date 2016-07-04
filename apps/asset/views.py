# -*- coding:utf-8 -*-

from flask import jsonify, abort, url_for, request
# from flask.ext import restful
from . import asset
from .models import db, Asset, AssetGroup, IDC, Tag


# Asset CRUD
@asset.route('/add', methods=['POST'])
def asset_add():
    """
    This is asset add api, please post data like this
        {"ip": "172.16.1.1", "hostname": "asset01", "idc": "chinanet", "group": ["group01", "group02"], ...}
    """
    json_data = request.get_json(force=True)

    ip = json_data.get('ip', '')
    hostname = json_data.get('hostname', '')
    port = json_data.get('port', '')
    idc_name = json_data.get('idc', '')
    group_all = json_data.get('group', '')
    device_types = json_data.get('device_type', '')
    system_types = json_data.get('system_type', '')
    tag_all = json_data.get('tag', '')
    asset = Asset(ip=ip, hostname=hostname)
    if idc_name:
        idc = IDC.query.filter_by(name=idc_name).first_or_404()
        asset.idc = idc
    for group_name in group_all:
        group = AssetGroup.query.filter_by(name=group_name).first_or_404()
        asset.group.append(group)
    for tag_name in tag_all:
        tag = Tag.query.filter_by(name=tag_name).first_or_404()
        asset.tags.append(tag)
    device_type = Tag.query.filter_by(value=device_types).first_or_404()
    system_type = Tag.query.filter_by(value=system_types).first_or_404()

    asset.device_type = device_type
    asset.system_type = system_type
    db.session.add(asset)
    db.session.commit()
    return jsonify({"code": 200, "message": "success"})


@asset.route('/edit/<int:asset_id>', methods=['POST'])
def asset_edit(asset_id):
    form = request.form
    asset = Asset.query.get_or_404(asset_id)
    ip = form.get('ip', '')
    hostname = form.get('hostname', '')
    asset.ip = ip
    asset.hostname = hostname
    db.session.add(asset)
    db.session.commit()
    return jsonify({"code": 200, "message": "success"})


@asset.route('/del/<int:asset_id>', methods=['GET'])
def asset_del(asset_id):
    asset = Asset.query.get_or_404(asset_id)
    db.session.delete(asset)
    db.session.commit()
    return jsonify({"code": 200, "message": "success"})


@asset.route('/detail/<int:asset_id>', methods=['GET'])
def asset_detail(asset_id):
    asset = Asset.query.get_or_404(asset_id)
    return jsonify({"code": 200, "message": "success", "data": asset.to_json()})


@asset.route('/list', methods=['GET'])
def asset_list():
    try:
        assets = Asset.query.order_by('hostname')
        message = 'success'
    except Exception as e:
        message = e
    return jsonify({"code": 200, "message": message, "data": [{asset.hostname: asset.to_json()} for asset in assets]})


# AssetGroup CRUD
@asset.route('/group/add', methods=['POST'])
def group_add():
    form = request.form
    name = form.get('name', '')
    group = AssetGroup(name=name)
    db.session.add(group)
    db.session.commit()
    return jsonify({"code": 200, "message": "success"})


@asset.route('/group/del/<int:group_id>', methods=['POST'])
def group_del(group_id):
    pass


@asset.route('/group/edit/<int:group_id>', methods=['POST'])
def group_edit():
    pass


@asset.route('/group/detail/<int:group_id>', methods=['GET'])
def group_detail(group_id):
    pass


@asset.route('/group/list', methods=['GET'])
def group_list():
    pass


# IDC CRUD
@asset.route('/idc/add', methods=['POST'])
def idc_add():
    form = request.form
    name = form.get('name', '')
    idc = IDC(name=name)
    db.session.add(idc)
    db.session.commit()
    return jsonify({"code": 200, "message": "success"})


@asset.route('/idc/del/<int:idc_id>', methods=['POST'])
def idc_del(idc_id):
    pass


@asset.route('/idc/edit/<int:idc_id>', methods=['POST'])
def idc_edit(idc_id):
    pass


@asset.route('/idc/detail/<int:idc_id>', methods=['GET'])
def idc_detail(idc_id):
    pass


@asset.route('/idc/list', methods=['GET'])
def idc_list():
    pass


# Tag CRUD
@asset.route('/tag/add', methods=['POST'])
def tag_add():
    form = request.form
    key = form.get('key', '')
    value = form.get('value', '')
    tag = Tag(key=key, value=value)
    db.session.add(tag)
    db.session.commit()
    return jsonify({"code": 200, "message": "success"})


@asset.route('/tag/del/<int:tag_id>', methods=['POST'])
def tag_del(tag_id):
    pass


@asset.route('/tag/edit/<int:tag_id>', methods=['POST'])
def tag_edit(tag_id):
    pass


@asset.route('/tag/detail/<int:tag_id>', methods=['GET'])
def tag_detail(tag_id):
    pass


@asset.route('/tag/list', methods=['GET'])
def tag_list():
    pass




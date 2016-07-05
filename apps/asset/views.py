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
    remote_ip = json_data.get('remote_ip', '')
    other_ip = json_data.get('remote_ip', '')
    group_list = json_data.get('group', [])
    idc_name = json_data.get('idc', '')
    mac = json_data.get('mac', '')
    cpu = json_data.get('cpu', '')
    memory = json_data.get('memory', '')
    disk = json_data.get('disk', '')
    sn = json_data.get('sn', '')
    number = json_data.get('number', '')
    cabinet = json_data.get('cabinet', '')
    position = json_data.get('postion', '')
    system_type = json_data.get('system_type', '')
    device_type = json_data.get('device_type', '')
    env = json_data.get('env', '')
    status = json_data.get('status', '')
    brand = json_data.get('brand', '')
    system_arch = json_data.get('system_arch', '')
    system_version = json_data.get('system_version', '')
    tags_list = json_data.get('tags', [])
    is_active = json_data.get('is_active', 1)
    comment = json_data.get('comment', '')
    if Asset.query.filter_by(ip=ip, port=port).count() != 0:
        db.session.rollback()
        return jsonify({"code": 400, "message": "host {0} and port {1} is exist.".format(ip, port)})
    try:
        asset = Asset(ip=ip, port=port, hostname=hostname,
                      other_ip=other_ip, remote_ip=remote_ip,
                      mac=mac, memory=memory,
                      disk=disk, sn=sn,
                      number=number, cabinet=cabinet,
                      position=position, system_version=system_version,
                      is_active=int(is_active), comment=comment)
        if idc_name:
            idc = IDC.query.filter_by(name=idc_name).first_or_404()
            asset.idc = idc

        # for field in ['system_type', 'device_type', 'env', 'status', 'brand', 'system_arch']:
        #     field_instance = Tag.query.filter_by(value=json_data.get(field, ''))
        #     setattr(asset, field, field_instance)
        # if system_type:
        #     system_type = Tag.query.filter_by(value=system_type).first_or_404()
        #     asset.system_type = system_type
        # if device_type:
        #     device_type = Tag.query.filter_by(value=device_type).first_or_404()
        #     asset.device_type = device_type
        #
        # if env:
        #     env = Tag.query.filter_by(value=env).first_or_404()
        #     asset.env = env

        for group_name in group_list:
            group = AssetGroup.query.filter_by(name=group_name).first_or_404()
            asset.group.append(group)
        for tag_name in tags_list:
            tag = Tag.query.filter_by(name=tag_name).first_or_404()
            asset.tags.append(tag)

        db.session.add(asset)
        db.session.commit()
    except Exception as e:
        return jsonify({"code": 400, "message": "error"})

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




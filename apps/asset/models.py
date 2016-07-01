# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.orm import relationship
from apps import db


class Tag(db.Model):
    __tablename__ = 'cmdb_tag'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(32))
    value = db.Column(db.String(64))
    comment = db.Column(db.String(128))
    user_add = db.Column(db.String(32))

    def __repr__(self):
        return '<Tag %r>' % self.value


asset_tag = db.Table('cmdb_asset_tag',
                     db.Column('tag_id', db.Integer, db.ForeignKey('cmdb_tag.id')),
                     db.Column('asset_id', db.Integer, db.ForeignKey('cmdb_asset.id'))
                     )

asset_group_tag = db.Table('cmdb_asset_group_tag',
                           db.Column('tag_id', db.Integer, db.ForeignKey('cmdb_tag.id')),
                           db.Column('group_id', db.Integer, db.ForeignKey('cmdb_asset_group.id'))
                           )

asset_asset_group = db.Table('cmdb_asset_asset_group',
                             db.Column('group_id', db.Integer, db.ForeignKey('cmdb_asset_group.id')),
                             db.Column('asset_id', db.Integer, db.ForeignKey('cmdb_asset.id'))
                             )


class AssetGroup(db.Model):
    __tablename__ = 'cmdb_asset_group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    tags = db.relationship('Tag',
                           secondary=asset_group_tag,
                           backref=db.backref('cmdb_asset_group', lazy='dynamic'),
                           lazy='dynamic')
    user_add = db.Column(db.String(32))
    date_add = db.Column(db.DateTime(), default=datetime.utcnow)
    comment = db.Column(db.String(128))

    def __repr__(self):
        return '<AssetGroup %r>' % self.name


class Service(db.Model):
    __tablename__ = 'cmdb_service'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __repr__(self):
        return '<Service %r>' % self.name


class IDC(db.Model):
    __tablename__ = 'cmdb_idc'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    linkman = db.Column(db.String(32))
    phone = db.Column(db.String(16))
    address = db.Column(db.String(64))
    network = db.Column(db.String(128))
    date_add = db.Column(db.DateTime(), default=datetime.utcnow)
    comment = db.String(db.String(64))
    assets = db.relationship('Asset', backref='idc')

    def __repr__(self):
        return '<Asset %r>' % self.name


class Asset(db.Model):
    __tablename__ = 'cmdb_asset'

    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(128), unique=True, nullable=False)
    ip = db.Column(db.String(32), nullable=True)
    other_ip = db.Column(db.String(128), nullable=True)
    remote_ip = db.Column(db.String(128), nullable=True)
    username = db.Column(db.String(32), nullable=True)
    password = db.Column(db.String(32), nullable=True)
    port = db.Column(db.Integer)
    group = db.relationship('AssetGroup',
                            secondary=asset_asset_group,
                            backref=db.backref('cmdb_asset', lazy='dynamic'),
                            lazy='dynamic')
    idc_id = db.Column(db.Integer, db.ForeignKey('cmdb_idc.id'))
    mac = db.Column(db.String(16), nullable=True)
    cpu = db.Column(db.String(64), nullable=True)
    memory = db.Column(db.String(128), nullable=True)
    disk = db.Column(db.String(256), nullable=True)
    sn = db.Column(db.String(64), nullable=True)
    number = db.Column(db.String(64), nullable=True)
    cabinet = db.Column(db.String(32), nullable=True)
    position = db.Column(db.Integer, nullable=True)
    system_type_id = db.Column(db.Integer, db.ForeignKey('cmdb_tag.id'))
    device_type_id = db.Column(db.Integer, db.ForeignKey('cmdb_tag.id'))
    env_id = db.Column(db.Integer, db.ForeignKey('cmdb_tag.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('cmdb_tag.id'))
    brand_id = db.Column(db.Integer, db.ForeignKey('cmdb_tag.id'))
    system_arch_id = db.Column(db.Integer, db.ForeignKey('cmdb_tag.id'))
    system_type = relationship("Tag", foreign_keys=[system_type_id])
    device_type = relationship("Tag", foreign_keys=[device_type_id])
    env = relationship("Tag", foreign_keys=[env_id])
    status = relationship("Tag", foreign_keys=[status_id])
    brand = relationship("Tag", foreign_keys=[brand_id])
    system_arch = relationship("Tag", foreign_keys=[system_arch_id])
    system_version = db.Column(db.String(32), nullable=True)
    tags = db.relationship('Tag',
                           secondary=asset_tag,
                           backref=db.backref('cmdb_asset', lazy='dynamic'),
                           lazy='dynamic')
    is_active = db.Column(db.Boolean(), default=0)
    comment = db.Column(db.String(128), nullable=True)
    date_add = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<Asset %r>' % self.ip

    def get_idc_name(self):
        idc = IDC.query.get_or_404(self.idc_id)
        return idc.name

    def get_m2m_name(self, name):
        asset = Asset.query.get_or_404(self.id)
        return [instance.name if name == 'group' else instance.value for instance in getattr(asset, name).all()]

    def get_tag_value(self, name):
        asset = Asset.query.get_or_404(self.id)
        try:
            instance = getattr(asset, name)
            ret = instance.value
        except AttributeError as e:
            ret = ''
        return ret

    def to_json(self):
        json_data = {
            'id': self.id,
            'hostname': self.hostname,
            'ip': self.ip,
            'remote_ip': self.remote_ip,
            'port': self.port,
            'username': self.username,
            'password': self.password,
            'idc': self.get_idc_name(),
            'group': self.get_m2m_name('group'),
            'mac': self.mac,
            'cpu': self.cpu,
            'memory': self.memory,
            'sn': self.sn,
            'number': self.number,
            'cabinet': self.cabinet,
            'position': self.position,
            'disk': self.disk,
            'device_type': self.get_tag_value('device_type'),
            'system_type': self.get_tag_value('system_type'),
            'env': self.get_tag_value('env'),
            'status': self.get_tag_value('status'),
            'brand': self.get_tag_value('brand'),
            'tags': self.get_m2m_name('tags'),
            'comment': self.comment,
            'date_add': self.date_add,
        }
        return json_data

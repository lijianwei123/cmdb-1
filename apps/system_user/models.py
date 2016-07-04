# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.orm import relationship
from apps import db
from apps import asset


class SystemUser(db.Model):
    __tablename__ = 'cmdb_system_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100))
    login_type = db.Column(db.Char(1))
    auth_type = db.Column(db.Char(1))
    auto_push_id = db.Column(db.Integer, db.ForeignKey('cmdb_auto_push.id'))
    password = db.Column(db.String(100))
    key_content = db.Column(db.Text)
    key_path = db.Column(db.String(255), nullable=True)
    level = db.Column(db.Integer)   # 这个是用来说明用户的级别,0为普通用户,1为管理用户
    comment = db.Column(db.String(128), nullable=True)
    editor = db.Column(db.String(128))
    data_joined = db.Column(db.DateTime(), default=datetime.utcnow)
    data_edited = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<SystemUser %r:%r>' % (self.name, self.username)

    def get_editor(self):
        return self.editor

    def get_system_user_detail(self):
        """
        获取系统用户的附加信息
        :return:
        """
        auto_push = AutoPush.query.get_or_404(self.auto_push_id)
        detail = {
            "sudo_cmd_group": auto_push.sudo_cmd_group,
            "shell": auto_push.system_user_shell,
            "home": auto_push.system_user_home,
            "groups": auto_push.system_user_groups,
            "UID": auto_push.system_user_UID,
        }
        return detail


class AutoPush(db.Model):
    __tablename__ = 'cmdb_auto_push'

    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('cmdb_tag.id'))
    sudo_cmd_group = db.Column(db.Integer, db.ForeignKey('cmdb_sudo_cmd_group.id'))
    system_user_shell = db.Column(db.String(32), nullable=True)
    system_user_home = db.Column(db.String(255), nullable=True)
    system_user_groups = db.Column(db.String(128), nullable=True)
    system_user_UID = db.Column(db.String(32), nullable=True)


class PushHistory(db.Model):
    __tablename__ = 'cmdb_push_history'

    id = db.Column(db.Integer, primary_key=True)
    system_user_id = db.Column(db.Integer, db.ForeignKey('cmdb_system_user.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('cmdb_tag.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('cmdb_asset_group.id'))
    status = db.Column(db.Boolean(), default=0)
    push_date = db.Column(db.DateTime(), default=datetime.utcnow)
    comment = db.Column(db.String(128), nullable=True)


class PushHistoryDetail(db.Model):
    __tablename__ = 'cmdb_push_history_detail'

    id = db.Column(db.Integer, primary_key=True)
    push_history_id = db.Column(db.Integer, db.ForeignKey('cmdb_push_history.id'))
    asset_id = db.Column(db.Integer, db.ForeignKey('cmdb_asset.id'))
    status = db.Column(db.Boolean(), default=0)
    push_date = db.Column(db.DateTime(), default=datetime.utcnow)
    comment = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        if self.status:
            return '<PushHistoryDetail %r:failed(%r)>' % (self.asset_id, self.comment)
        return '<PushHistoryDetail %r:success>' % self.asset_id

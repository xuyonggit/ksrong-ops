from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

# 初始化db
db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)    # id
    name = db.Column(db.String(20), unique=True)    # 姓名
    net_name = db.Column(db.String(20), unique=True)    # 用户名
    password = db.Column(db.String(250))    # 密码
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))     # 权限ID
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    sex = db.Column(db.Integer, default=0)  # 性别
    enterprise_id = db.Column(db.Integer, db.ForeignKey('enterprise.id'), nullable=True)

    # 自定义表名
    __tablename__ = 'users'

    # 初始化字段 方便以后视图使用
    def __init__(self, name, sex, net_name, enterprise_id):
        self.net_name = net_name
        self.name = name
        self.sex = sex
        self.enterprise_id = enterprise_id

    # 定义保存数据的方法 后面视图好使用
    def save(self):
        db.session.add(self)
        db.session.commit()


class Enterprise(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)    # id
    long_name = db.Column(db.String(256))    # 企业全称
    sort_name = db.Column(db.String(8), unique=True)    # 企业简称
    # 自定义表名
    __tablename__ = 'enterprise'

    # 初始化字段 方便以后视图使用
    def __init__(self, sort_name):
        self.sort_name = sort_name

    def save(self):
        db.session.add(self)
        db.session.commit()


r_p = db.Table('r_p',
               db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
               db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
               )


class Role(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    users = db.relationship('Users', backref='role')

    __tablename__ = 'role'

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Permission(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    roles = db.relationship('Role', secondary=r_p, backref=db.backref('permission', lazy=True))
    __tablename__ = 'permission'

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()


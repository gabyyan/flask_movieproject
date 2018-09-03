from flaskr import db
import datetime


class auth(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(600), nullable=False)
    addTime = db.Column(db.Date, index=True, nullable=False, default=datetime.datetime.now())


class role(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    adminName = db.Column(db.String(30), nullable=False)
    auths = db.Column(db.String(60), nullable=False)
    addTime = db.Column(db.Date, index=True, nullable=False, default=datetime.datetime.now())


class admin(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    pwd = db.Column(db.String(30), nullable=False)
    is_super = db.Column(db.SmallInteger, nullable=False)
    oplogs = db.relationship("oplog", back_populates="adminId")
    adminlogs = db.relationship("adminlog", back_populates="adminId")


class adminlog(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.INTEGER, db.ForeignKey('admin.id', onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    ip = db.Column(db.String(100), nullable=False)
    addTime = db.Column(db.Date, index=True, nullable=False, default=datetime.datetime.now())
    adminId = db.relationship("admin", back_populates='adminlogs')


class oplog(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.INTEGER, db.ForeignKey('admin.id', onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    ip = db.Column(db.String(100), nullable=False)
    operate = db.Column(db.Text, nullable=False)
    addTime = db.Column(db.Date, index=True, nullable=False, default=datetime.datetime.now())
    adminId = db.relationship("admin", back_populates="oplogs")







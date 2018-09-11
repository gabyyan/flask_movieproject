from flaskr import db
import datetime
import uuid


def gen_id():
    return uuid.uuid4().hex


class user(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(30), nullable=False)
    pwd = db.Column(db.String(32), nullable=False)
    nickname = db.Column(db.String(50), nullable=True, unique=True)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    info = db.Column(db.Text, nullable=True)
    face = db.Column(db.String(30), nullable=True)
    # loginTime = db.Column(db.DateTime, nullable=True, onupdate=datetime.datetime.now())
    registTime = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now())
    uuid = db.Column(db.String(32), nullable=True, default=gen_id)

    loginlogs = db.relationship("loginlog", back_populates='userId')
    comments = db.relationship("comment", back_populates='userId')
    collections = db.relationship("collection", back_populates='userId')


class loginlog(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id', onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    userIp = db.Column(db.String(30), nullable=False)
    loginTime = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    userId = db.relationship("user", back_populates='loginlogs')


movie_tag = db.Table('movie_tag',
                     db.Column('tag_id', db.INTEGER, db.ForeignKey('tag.id', ondelete="SET NULL"), nullable=True),
                     db.Column('movie_id', db.INTEGER, db.ForeignKey('movie.id', ondelete="SET NULL"), nullable=True)
                     )


class movie(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(600), nullable=False)
    info = db.Column(db.Text, nullable=False)
    logo = db.Column(db.String(50), nullable=False)
    star = db.Column(db.Float, nullable=False)
    playNum = db.Column(db.Integer, nullable=True)
    commentNum = db.Column(db.INTEGER, nullable=True)
    area = db.Column(db.String(50), nullable=False)
    release_time = db.Column(db.Date, nullable=False)
    length = db.Column(db.String(50), nullable=False)
    addTime = db.Column(db.DateTime, index=True, nullable=False, default=datetime.datetime.now())
    comments = db.relationship("comment", back_populates='movieId')
    collections = db.relationship("collection", back_populates='movieId')
    tags = db.relationship("tag",
                           secondary=movie_tag,
                           back_populates="movies"
                           )

class tag(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    tagName = db.Column(db.String(50), nullable=False, unique=True)
    addTime = db.Column(db.DateTime, index=True,  nullable=False, default=datetime.datetime.now())
    movies = db.relationship("movie",
                             secondary=movie_tag,
                             back_populates="tags")

    def __repr__(self):
        return "%s" % (self.tagName)


class comment(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    movie_id = db.Column(db.INTEGER, db.ForeignKey('movie.id', onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    movieId = db.relationship("movie", back_populates='comments')
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id', onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    userId = db.relationship("user", back_populates="comments")


class collection(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.INTEGER, db.ForeignKey('movie.id', onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    movieId = db.relationship("movie", back_populates='collections')
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id', onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    userId = db.relationship("user", back_populates="collections")


class preview(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    logo = db.Column(db.String(50), nullable=False)
    addTime = db.Column(db.DateTime, index=True, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return "<preview(title='%s', logo='%s', addTime='%s')>" % (
                                self.title, self.logo, self.addTime)



# from flaskr import db
# import datetime


class auth(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    url = db.Column(db.String(600), nullable=False)
    addTime = db.Column(db.DateTime, index=True, nullable=False, default=datetime.datetime.now())

    role_id = db.Column("role", db.ForeignKey('role.id', ondelete="SET NULL"))
    role = db.relationship("role", back_populates="auths")

    def __repr__(self):
        return "%s" % (self.name)


class role(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

    auths = db.relationship("auth", back_populates="role")
    addTime = db.Column(db.DateTime, index=True, nullable=False, default=datetime.datetime.now())

    admin_id = db.Column('admin', db.ForeignKey('admin.id', ondelete="SET NULL"))
    admin = db.relationship('admin', back_populates='roles')

    def __repr__(self):
        return "%s" % (self.name)


class admin(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    pwd = db.Column(db.String(32), nullable=False)
    is_super = db.Column(db.SmallInteger, nullable=False)
    addTime = db.Column(db.DateTime, index=True, nullable=False, default=datetime.datetime.now())

    oplogs = db.relationship("oplog", back_populates="adminId")
    adminlogs = db.relationship("adminlog", back_populates="adminId")
    roles = db.relationship('role', back_populates='admin')


class adminlog(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.INTEGER, db.ForeignKey('admin.id', onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    ip = db.Column(db.String(100), nullable=False)
    addTime = db.Column(db.DateTime, index=True, nullable=False, default=datetime.datetime.now())
    adminId = db.relationship("admin", back_populates='adminlogs')


class oplog(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.INTEGER, db.ForeignKey('admin.id', onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    ip = db.Column(db.String(100), nullable=False)
    operate = db.Column(db.Text, nullable=False)
    addTime = db.Column(db.DateTime, index=True, nullable=False, default=datetime.datetime.now())
    adminId = db.relationship("admin", back_populates="oplogs")







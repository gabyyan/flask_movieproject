from flaskr import db
import datetime
import uuid


def gen_id():
    return uuid.uuid4().hex


class user(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(30), nullable=True)
    pwd = db.Column(db.String(32), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    info = db.Column(db.Text, nullable=True)
    face = db.Column(db.String(30), nullable=True)
    loginTime = db.Column(db.String(30), nullable=True, default=datetime.datetime.now())
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
    playNum = db.Column(db.Integer, nullable=False)
    commentNum = db.Column(db.INTEGER, nullable=False)
    area = db.Column(db.String(50), nullable=False)
    release_time = db.Column(db.DateTime, nullable=False)
    length = db.Column(db.DateTime, nullable=False)
    addTime = db.Column(db.Date, index=True, nullable=False, default=datetime.datetime.now())
    comments = db.relationship("comment", back_populates='movieId')
    collections = db.relationship("collection", back_populates='movieId')
    tags = db.relationship("tag",
                           secondary=movie_tag,
                           back_populates="movies"
                           )

class tag(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    tagName = db.Column(db.String(50), nullable=False)
    addTime = db.Column(db.Date, index=True,  nullable=False, default=datetime.datetime.now())
    movies = db.relationship("movie",
                             secondary=movie_tag,
                             back_populates="tags")


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
    addTime = db.Column(db.Date, index=True, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return "<preview(title='%s', logo='%s', addtime='%s')>" % (
                                self.title, self.logo, self.addtime)


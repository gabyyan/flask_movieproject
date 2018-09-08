from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Regexp, ValidationError
from flaskr import model

class RegistForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(' 用户名必须填写！'), Regexp('^[a-zA-Z][a-zA-Z_0-9]{2,19}$', flags=0, message='用户名格式不正确！')], render_kw={'placeholder': '  字母/数字/下划线 3-20位 首位是字母', "style": "font-size:16px"})
    email = StringField('邮箱', validators=[DataRequired('邮箱必填！'), Email('邮箱格式不正确！')], render_kw={'placeholder': '  邮箱 ', "style": "font-size:16px"})
    phone = StringField('手机', validators=[DataRequired('手机号码必填！'), Regexp('^1[3|4|5|7|8][0-9]{9}$', flags=0, message='手机号码格式错误！')], render_kw={'placeholder': '  手机', "style": "font-size:16px"})
    pwd = PasswordField('密码', validators=[DataRequired('密码必填！'), Regexp('^[a-zA-Z_0-9]{4,10}$', flags=0,  message='密码格式不正确！')], render_kw={'placeholder': '  密码：字母/数字/下划线 4-10位', "style": "font-size:16px"})
    checkpwd = PasswordField('确认密码', validators=[DataRequired('重复密码必填！'), EqualTo('pwd', message='两次密码输入不一致！')], render_kw={'placeholder': '  输入和上一项相同密码', "style": "font-size:16px"})
    submit = SubmitField('登录')

    def validate_username(self, field):
        if model.user.query.filter_by(userName=field.data).first():
            raise ValidationError('用户名已存在')

    def validate_email(self, field):
        if model.user.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')

    def validate_phone(self, field):
        if model.user.query.filter_by(phone=field.data).first():
            raise ValidationError('手机号已被注册')


class LoginForm(FlaskForm):
    account = StringField('帐号', validators=[DataRequired('用户名必须填写！')], render_kw={'placeholder': '   用户名/邮箱/手机号码'})
    pwd = PasswordField('密码', validators=[DataRequired('密码必须填写')], render_kw={'placeholder': '   密码'})
    submit = SubmitField('登录')


from . import homes
from flask import render_template, redirect, request, flash
from flask import url_for, current_app
from flaskr.home.form import RegistForm, LoginForm
from flaskr.home import model
from flaskr import db
import re
import hashlib


@homes.route("/login", methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        account = request.form.get('account', None)
        FillPwd = request.form.get('pwd', None)
        FillPwd_Md5 = hashlib.md5(FillPwd.encode('utf8'))     # md5加密
        password_Md5 = FillPwd_Md5.hexdigest()
        print(account)
        print(FillPwd)
        try:
            if '@' in account:
                search_email = model.user.query.filter_by(email=account).first()
                if search_email is not None and search_email.pwd == password_Md5:
                    return "登录成功"
                else:
                    return render_template("login.html", lForm=login_form,  error="用户名或密码不正确！")
            elif re.match('^\d', account):   #首位是否为数字
                search_phone = model.user.query.filter_by(phone=account).first()
                if search_phone is not None and search_phone.pwd == password_Md5:
                    return "登录成功"
                else:
                    return render_template("login.html", lForm=login_form, error="用户名或密码不正确！")
            else:
                search_usr = model.user.query.filter_by(nickname=account).first()
                print(type(search_usr))
                print(search_usr)
                if search_usr is not None and search_usr.pwd == password_Md5:
                    return "登录成功！"
                else:
                    return render_template("login.html", lForm=login_form, error="用户名或密码不正确！")
        except Exception as e:
            print("\n出错啦\n", e)
            return render_template("login.html", error="Error:500,请刷新后重新登录", lForm=login_form)

    return render_template("login.html", lForm=login_form)


@homes.route("/regist", methods=['POST', 'GET'])
def regist():
    regist_form = RegistForm()

    if regist_form.validate_on_submit():
        email = request.form.get('email', None)
        nickname = request.form.get('nickname', None)
        phone = request.form.get('phone', None)
        pwd = request.form.get('pwd', None)
        # info = model.user(email=regist_form.email.data, nickname=regist_form.nickname.data, phone=regist_form.phone.data, pwd=regist_form.pwd.data)
        pwd_temp = hashlib.md5(request.form['pwd'].encode('utf8'))     # md5加密
        password = pwd_temp.hexdigest()
        info = model.user(email=email, nickname=nickname, phone=phone, pwd=password)
        db.session.add(info)
        db.session.commit()
        return redirect('/login')
    return render_template("regist.html", rForm=regist_form)
from . import admins
from flask import render_template, request, redirect, Response
from flaskr import model
from flaskr import db

import json

from bs4 import BeautifulSoup
import requests
import re

@admins.route("/admin/")
def admin():
    # headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    # res1 = requests.get('https://movie.douban.com/trailers/', headers=headers)
    # # print(res1.text)
    # # with open("html_2.html", encoding='utf-8') as f:
    # soup = BeautifulSoup(res1.text, features='lxml')
    #
    # for img in soup.select("li img"):
    #     # print(img.get('alt'))
    #     preview_add = model.preview(title=str(img.get('alt')), logo=str(img.get('src')))
    #     db.session.add(preview_add)
    #     db.session.commit()
    return render_template("admin_bootstrap.html")


@admins.route("/admin/login")
def adminlogin():
    return render_template("login_admin.html")


@admins.route("/admin/tag_add", methods=['POST', 'GET'])
def tag_add():
    if request.method == "POST":
        name = request.form.get('input_name', None)
        if model.tag.query.filter_by(tagName=name).first():
            return render_template("tag_add.html", error="已存在此标签！")
        else:
            taginfo = model.tag(tagName=name)
            db.session.add(taginfo)
            db.session.commit()
            return redirect('/admin/tag_add')
    return render_template("tag_add.html")


@admins.route("/admin/tag_list", methods=['POST', 'GET'])
def tag_list():
    taglists = model.tag.query.all()
    if request.method == "POST":
        op = request.form.get('op')
        print("打印op is ????\n", op)
        if op == "del_tag":
            id = request.form.get("id", None)
            try:
                deltag = model.tag.query.filter_by(id=id).first()
                db.session.delete(deltag)
                db.session.commit()
            except Exception as e:
                print("打印删除标签的时候出现的错误", e)
                return "error"
        elif op == "edit_tag":
            formdata = request.form.get("formdata", None)
            formobj = json.loads(formdata)
            print("打印formObj\n", formobj)
            tagid = request.form.get("id", None)
            print("打印 id", tagid)
            tagName = formobj['tagName']
            addTime = formobj['addTime']
            try:
                edit_tag = model.tag.query.filter_by(id=tagid).first()
                print("edit_tag\n",edit_tag)
                edit_tag.tagName = tagName
                edit_tag.addTime = addTime
                db.session.commit()
            except Exception as e:
                print("打印编辑标签的时候出现的错误", e)
                return "error"
        return "ok"
    return render_template("tag_list.html", taglists=taglists)


@admins.route("/admin/movie_add", methods=['POST', 'GET'])
def movie_add():
    if request.method == 'POST':
        title = request.form.get('input_title', None)
        url = request.form.get('input_url', None)
        info = request.form.get('input_info', None)
        logo = request.form.get('input_logo', None)
        star = request.form.get('input_star', None)
        area = request.form.get('input_area', None)
        release_time = request.form.get('input_release_time', None)
        length = request.form.get('input_length', None)
        choose_tag = request.form.getlist('input_tag_id')
        print("choose_tag", choose_tag)
        ################################################################ input_tag_id  这是建立的多对多的表
        movie_info = model.movie(title=title, url=url, info=info, logo=logo, star=star, area=area, release_time=release_time, length=length)
        db.session.add(movie_info)
        db.session.commit()
        try:
            for i in choose_tag:
                themovie = model.movie.query.filter_by(title=title).first()
                themovie.tags.append(model.tag.query.filter_by(tagName=i).first())
                db.session.add(themovie)
                db.session.commit()
        except Exception as e:
            print("print error", e)
            db.session.remove(model.movie.query.filter_by(title=title).first())
            db.session.commit()
            return render_template("movie_add.html", error="添加失败，请刷新重试")
    taglists = model.tag.query.all()
    return render_template("movie_add.html", taglists=taglists)


@admins.route("/admin/movie_list", methods=['POST', 'GET'])
def movie_list():
    movielists = model.movie.query.all()
    taglists = model.tag.query.all()
    print("运行到 movie_list")
    if request.method == 'POST':
        op = request.form.get('op',None)
        the_id = request.form.get('id',None)
        if op == "movie_edit":
            formdata = request.form.get('formdata', None)
            formobj = json.loads(formdata)
            teacherList = []
            for i in formobj['label_list']:
                teacherList.append(model.tag.query.filter_by(tagName=i).first())
            print("teacherList\n",teacherList)
            edit_movie = model.movie.query.filter_by(id=the_id).first()
            print("edit_movie\n", edit_movie)
            edit_movie.title = formobj['title']
            edit_movie.length = formobj['length']
            edit_movie.area = formobj['area']
            edit_movie.star = formobj['star']
            edit_movie.release_time = formobj['release_time']
            # edit_movie.tags.set(teacherList)####################################################  没有 set 属性
            edit_movie.tags = []
            edit_movie.tags = teacherList
            db.session.commit()
            return "ok"
        elif op == "del_movie":
            try:
                delmovie = model.movie.query.filter_by(id=the_id).first()
                db.session.remove(delmovie)
                db.session.commit()
            except Exception as e:
                print("打印删除电影的时候出现的错误", e)
                return "error"
    return render_template("movie_list.html", movielists=movielists, taglists=taglists)


@admins.route("/admin/preview_add", methods=['POST', 'GET'])
def preview_add():
    if request.method == 'POST':
        try:
            title = request.form.get('input_title', None)
            logo = request.form.get('input_logo', None)
            preview_info = model.preview(title=title, logo=logo)
            db.session.add(preview_info)
            db.session.commit()
        except Exception as e:
            print("添加预告的时候出错", e)
            return render_template("preview_add.html", error="添加出错，请刷新重试！")

    return render_template("preview_add.html")


@admins.route("/admin/preview_list", methods=['POST', 'GET'])
def preview_list():
    previeslists = model.preview.query.all()

    page=request.args.get('page',1,type=int)  #从request的参数中获取参数page的值，如果参数不存在那么返回默认值1，type=int保证返回的默认值是整形数字
    print("page",page)
    pagination=model.preview.query.paginate(page,per_page=15,error_out=True)
    previeslists=pagination.items
    print("posts\n", previeslists)
    return render_template('preview_list.html', previeslists=previeslists, pagination=pagination)
    # return render_template("preview_list.html", previeslists=previeslists)


@admins.route("/admin/user_list")
def user_list():
    userlists = model.user.query.all()
    return render_template("user_list.html", userlists=userlists)


@admins.route("/admin/user_view")
def user_view():

    userlists = model.user.query.all()
    return render_template("user_view.html", userlists=userlists)


@admins.route("/admin/comment_list")
def comment_list():
    return render_template("comment_list.html")


@admins.route("/admin/moviecol_list")
def moviecol_list():
    return render_template("moviecol_list.html")


@admins.route("/admin/oplog_list")
def oplog_list():
    return render_template("oplog_list.html")


@admins.route("/admin/adminloginlog_list")
def adminloginlog_list():
    return render_template("adminloginlog_list.html")


@admins.route("/admin/userloginlog_list")
def userloginlog_list():
    return render_template("userloginlog_list.html")


@admins.route("/admin/auth_add", methods=['POST', 'GET'])
def auth_add():
    if request.method == "POST":
        name = request.form.get('input_name', None)
        url = request.form.get('input_url', None)
        if model.auth.query.filter_by(name=name).first():
            return render_template("auth_add.html", error="已存在此权限名称！")
        else:
            authority = model.auth(name=name, url=url)
            db.session.add(authority)
            db.session.commit()
            return redirect('/admin/auth_add')
    return render_template("auth_add.html")


@admins.route("/admin/auth_list")
def auth_list():
    authlists = model.auth.query.all()
    return render_template("auth_list.html", authlists=authlists)


@admins.route("/admin/role_add", methods=['POST', 'GET'])
def role_add():
    authlists = model.auth.query.all()
    if request.method == "POST":
        name = request.form.get('input_name', None)
        if model.role.query.filter_by(name=name).first():
            return render_template("role_add.html", error="已存在此角色！请刷新重试")
        else:
            roleinfo = model.role(name=name)
            db.session.add(roleinfo)
            db.session.commit()
###################################################################################这里应该吧 添加的权限保存再角色表的表里
            max_id = model.auth.query.order_by(model.auth.id.desc()).first().id
            for i in range(1, int(max_id)+1):
                choose_auth = request.form.get(''+str(i)+'', None)
                print("\n写出查询结果", choose_auth)
                if choose_auth:
                    try:
                        therole = model.role.query.filter_by(name=name).first()
                        therole.auths.append(model.auth.query.filter_by(name=choose_auth).first())
                        db.session.add(therole)
                        db.session.commit()
                    except Exception as e:
                        print(e)
                        deleterole = model.role.query.filter_by(name=name).one()
                        db.session.delete(deleterole)
                        db.session.commit()
                        return render_template("role_add.html", error="权限添加未成功！")
            return redirect('/admin/role_add')
    return render_template("role_add.html", authlists=authlists)


@admins.route("/admin/role_list")
def role_list():
    rolelists = model.role.query.all()
    return render_template("role_list.html", rolelists=rolelists)


@admins.route("/admin/admin_add", methods=['POST', 'GET'])
def admin_add():
    rolelists = model.role.query.all()
    if request.method == "POST":
        name = request.form.get('input_name', None)
        # pwd = request.form.get('input_pwd', None)
        import hashlib
        pwd_temp = hashlib.md5(request.form['input_pwd'].encode('utf8'))     # md5加密
        password = pwd_temp.hexdigest()

        admin_add_role = request.form.get('admin_add_role', None)
        if model.admin.query.filter_by(name=name).first():
            return render_template("admin_add.html", error="已存在此管理员！")
        else:
            administrator = model.admin(name=name, pwd=password, is_super=2)
            db.session.add(administrator)
            db.session.commit()
            theadmin = model.admin.query.filter_by(name=name).first()
            try:
                theadmin.roles.append(model.role.query.filter_by(name=admin_add_role).first())
                db.session.add(theadmin)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.remove(administrator)
                db.session.commit()
                return render_template("admin_add.html", rolelists=rolelists, error="管理员角色添加失败！")
            return redirect('/admin/admin_add')
    return render_template("admin_add.html", rolelists=rolelists)


@admins.route("/admin/admin_list")
def admin_list():
    adminlists = model.admin.query.all()
    return render_template("admin_list.html", adminlists=adminlists)


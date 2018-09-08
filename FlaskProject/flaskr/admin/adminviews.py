from . import admins
from flask import render_template, request, redirect
from flaskr import model
from flaskr import db


@admins.route("/admin")
def admin():
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


@admins.route("/admin/tag_list")
def tag_list():
    taglists = model.tag.query.all()
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
        movie_info=model.movie(title=title, url=url, info=info, logo=logo, star=star, area=area, release_time=release_time, length=length)
        db.session.add(movie_info)
        db.session.commit()
        try:
            for i in choose_tag:
                themovie = model.movie.query.filter_by(title=title).first()
                themovie.tags.append(model.tag.filter_by(tagName=i).first())
                db.session.add(themovie)
                # db.session.commit()
        except Exception as e:
            print("print error", e)
            db.session.remove(movie_info)
            db.session.commit()
            return render_template("movie_add.html", error="添加失败，请刷新重试")
    taglists = model.tag.query.all()
    return render_template("movie_add.html", taglists=taglists)


@admins.route("/admin/movie_list")
def movie_list():
    movielists = model.movie.query.all()
    return render_template("movie_list.html", movielists=movielists)


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


@admins.route("/admin/preview_list")
def preview_list():
    previeslists = model.preview.query.all()
    return render_template("preview_list.html", previeslists=previeslists)


@admins.route("/admin/user_list")
def user_list():
    userlists = model.user.query.all()
    return render_template("user_list.html", userlists=userlists)


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
            max_id = model.auth.query.order_by(model.auth.id.desc()).first().id
###################################################################################这里应该吧 添加的权限保存再角色表的表里
            for i in range(0, max_id+1):
                choose_auth = request.form.get(''+str(i)+'', None)
                print("\n写出查询结果", choose_auth)
                if choose_auth:
                    try:
                        therole = model.role.query.filter_by(name=name)
                        therole.auths.append(model.auth.query.filter_by(name=choose_auth)).first()
                        db.session.add(therole)
                        db.session.commit()
                    except Exception as e:
                        print(e)
                        db.session.remove(roleinfo)
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
        pwd = request.form.get('input_pwd', None)
        admin_add_role = request.form.get('admin_add_role', None)
        if model.admin.query.filter_by(name=name).first():
            return render_template("admin_add.html", error="已存在此管理员！")
        else:
            administrator = model.admin(name=name, pwd=pwd, is_super=2)
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


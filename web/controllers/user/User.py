from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import flash
from flask import redirect
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from common.models.User import User
from common.libs.Forms import UserForm
from common.libs.Helper import iPagination
from application import app
from application import db
user_route = Blueprint('user_page', __name__)


@user_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(login_name=username, status=1).first()
        if user and check_password_hash(user.login_pwd, password):
            try:
                session['isLogged'] = 1
                session['id'] = user.id
                session['username'] = user.login_name
                return redirect(url_for('.index'))
            except:
                flash("账号或密码不正确!", category="error")
    return render_template('login.html')


@user_route.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('.login'))


@user_route.route('/')
@user_route.route('/<int:page>')
@user_route.route('/index')
@user_route.route('/index/<int:page>')
def index(page=None):
    if page is None:
        page = 1

    params = {
        "total": User.query.count(),
        "page_size": app.config['PAGE_SIZE'],
        "display": app.config['PAGE_DISPLAY'],
        "page": page,
        "url": request.path.replace('/{}'.format(page), '')
    }
    pagebanner = iPagination(params)
    keyword = request.args.get("search")
    if keyword:
        users = User.query.filter(User.login_name.contains(keyword)).order_by(User.id)\
            .paginate(page=page, per_page=app.config['PAGE_SIZE'])
        params['total'] = users.total
        pagebanner = iPagination(params)
        condition = '?search=' + keyword
        return render_template('/user/index.html', users=users, pages=pagebanner, condition=condition)
    users = User.query.order_by(User.id).paginate(page=page, per_page=app.config['PAGE_SIZE'])
    return render_template('/user/index.html', users=users, pages=pagebanner)


@user_route.route('/add', methods=['GET', 'POST'])
def add():
    form = UserForm()
    if form.validate_on_submit():
        try:
            user = User(
                form.login_name.data,
                form.login_pwd.data,
                form.status.data
            )
            db.session.add(user)
            db.session.commit()
            flash("添加管理员成功！")
            return redirect(url_for('.index'))
        except:
            flash("添加管理员失败!", category="error")
    return render_template('/user/add.html', form=form)


@user_route.route('/edit/<int:pk>', methods=['GET', 'POST'])
def edit(pk):
    user = User.query.get(pk)
    if user is None:
        return redirect(url_for('.index'))
    form = UserForm(obj=user)
    if form.validate_on_submit():
        try:
            user.login_name = form.login_name.data
            user.login_pwd = generate_password_hash(form.login_pwd.data)
            user.status = form.status.data
            db.session.add(user)
            db.session.commit()
            flash("编辑管理员成功！")
            return redirect(url_for('.index'))
        except:
            flash("编辑管理员失败!", category="error")
    return render_template('/user/edit.html', form=form)


@user_route.route('/delete/<int:pk>', methods=['GET', 'POST'])
def delete(pk):
    user = User.query.get(pk)
    if user is None:
        return redirect(url_for('.index'))
    try:
        db.session.delete(user)
        db.session.commit()
        flash("删除管理员成功!")
    except:
        flash("删除管理员失败!", category="error")
    return redirect(url_for('.index'))
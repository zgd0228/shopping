from flask import render_template,Blueprint,request,redirect,session,url_for,flash
from App.models import *
from App.templatetags import my_tags
from ..utils import Menus,Users,Good,time_format
from werkzeug.security import generate_password_hash
from werkzeug.datastructures import CombinedMultiDict
import uuid
import os

menus = Blueprint('menu',__name__)

@menus.route('/menu')
def menu():
    user_id = session['user_id']
    user = User.query.filter_by(id=user_id).first()
    menu_list = Menu.query.all()
    #menu_list = user.role.menu
    my_tags.menu_list()
    return render_template('admin/menu.html', menu_list=menu_list)

@menus.route('/menu/list')
def menu_list():

    menu = Menu.query.all()
    mid = request.values.get('mid')
    pid = request.values.get('pid')
    seconds = Permission.query.filter_by(mid=mid).all()
    permission = []
    if pid:
        permission = Permission.query.filter_by(pid=pid).all()
    return render_template('admin/menu_list.html', menus=menu, seconds=seconds, mid=mid, pid=pid, permission=permission)


@menus.route('/menu/add',methods=["GET","POST"])
def menu_add():
    if request.method=='GET':
        form = Menus.AddMenuForm()
        return render_template('admin/change.html', form=form)
    form = Menus.AddMenuForm(request.form)
    if form.validate():
        menu = Menu(
            title=form.title.data,
            icon=form.icon.data
        )
        db.session.add(menu)
        db.session.commit()
        return redirect(url_for('menu.menu_list'))
    return render_template('admin/change.html', form=form)

@menus.route('/menu/edit/<id>',methods=["GET","POST"])
def menu_edit(id):
    menu_obj = Menu.query.filter_by(id=id).first()
    if request.method == "GET":
        form = Menus.AddMenuForm(instance=menu_obj)
        return render_template('admin/change.html', form=form)
    form = Menus.AddMenuForm(request.form)
    if form.validate():
        menu = Menu(
            title=form.title.data,
            icon=form.icon.data,
        )
        db.session.update(menu)
        db.session.commit()
        return redirect(url_for('menu.menu_list'))
    return render_template('admin/change.html', form=form)

@menus.route('/menu/delete/<id>',methods=["GET","POST"])
def menu_delete(id):
    mid = request.values.get('mid')
    pid = request.values.get('pid')
    if request.method == "GET":
        return render_template('admin/delete.html')
    Menu.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('menu.menu_list'))

@menus.route('/menu/second/add/<id>',methods=["GET","POST"])
def menu_second_add(id):
    if request.method=='GET':
        form = Menus.AddSecondMenuForm()
        return render_template('admin/change.html', form=form)
    form = Menus.AddSecondMenuForm(request.form)
    if form.validate():
        menu = Permission(
            title=form.title.data,
            name=form.name.data,
            url=form.url.data,
            mid=id
        )
        db.session.add(menu)
        db.session.commit()
        return redirect(url_for('menu.menu_list'))
    return render_template('admin/change.html', form=form)

@menus.route('/menu/second/edit/<id>',methods=["GET","POST"])
def menu_second_edit(id):
    menu_obj = Permission.query.filter_by(id=id).first()
    if request.method == "GET":
        form = Menus.AddSecondMenuForm(instance=menu_obj)
        return render_template('admin/change.html', form=form)
    form = Menus.AddSecondMenuForm(request.form)
    if form.validate():
        permission= Permission(
            title=form.title.data,
            name=form.name.data,
            url = form.url.data
        )
        db.session.add(permission)
        db.session.commit()
        return redirect(url_for('menu.menu_list'))
    return render_template('admin/change.html', form=form)

@menus.route('/menu/second/delete/<id>',methods=["GET","POST"])
def menu_second_delete(id):
    if request.method == "GET":
        return render_template('admin/delete.html')
    Permission.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('menu.menu_list'))




@menus.route('/permission/add/<id>/filter=mid?<mid>',methods=["GET","POST"])
def permission_add(id,mid):

    if request.method=='GET':
        form = Menus.AddSecondMenuForm()
        return render_template('admin/change.html', form=form)
    form = Menus.AddSecondMenuForm(request.form)
    if form.validate():
        permission = Permission(
            title=form.title.data,
            name=form.name.data,
            url=form.url.data,
            pid=id
        )
        db.session.add(permission)
        db.session.commit()
        return redirect(url_for('menu.menu_list'))
    return render_template('admin/change.html', form=form)

@menus.route('/permission/edit/<id>',methods=["GET","POST"])
def permission_edit(id):
    menu_obj = Menu.query.filter_by(id=id).first()
    if request.method == "GET":
        form = Menus.AddSecondMenuForm(instance=menu_obj)
        return render_template('admin/change.html', form=form)
    form = Menus.AddSecondMenuForm(request.form)
    if form.validate():
        menu = Menu(
            title=form.title.data,
            icon=form.icon.data,
        )
        db.session.update(menu)
        db.session.commit()
        return redirect(url_for('menu.menu_list'))
    return render_template('admin/change.html', form=form)

@menus.route('/permission/delete/<id>',methods=["GET","POST"])
def permission_delete(id):
    if request.method == "GET":
        return render_template('admin/delete.html')
    Permission.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('menu.menu_list'))




@menus.route('/desc/list',methods=["GET","POST"])
def desc_list():
    uid = request.values.get('uid')
    rid = request.values.get('rid')

    user_id = uid
    role_id = None
    has_role = []
    has_permission_per = []
    if uid:
        users = User_Role.query.filter_by(user_id=uid).all()
        # user_id = users.id
        for role in users:
            has_role.append(role.role_id)
    if rid:
        roles = Role.query.filter_by(id=rid).first()
        role_id = roles.id
        roles = Role.query.filter_by(id=rid).first()
        for item in roles.permission:
            has_permission_per.append(item.id)
    users = User.query.all()
    roles = Role.query.all()
    menus = Menu.query.all()
    permissions = Permission.query.all()
    role_list = request.form.getlist('role')
    menu_list = request.form.getlist('permission')

    if role_list:
        for item in role_list:
            if not User_Role.query.filter_by(user_id=int(uid),role_id=int(item)).first():
                user_role = User_Role(
                    user_id=int(uid),
                    role_id=int(item)
                )
                db.session.add(user_role)
                db.session.commit()
    if menu_list:
        for item in menu_list:
            if not Role_Permission.query.filter_by(role_id=int(rid),permission_id=int(item)).first():
                role_permission = Role_Permission(
                    role_id=int(rid),
                    permission_id=int(item)
                )
                db.session.add(role_permission)
                db.session.commit()
    menu_dict = {}
    # for item in menus:
    #     menu_dict[item] = item.permission
    #     for per in item.permission:
    #         if per

    return render_template('admin/desc_list.html', users=users, roles=roles, menus=menus, user_id=user_id,
                           role_id=role_id, has_role=has_role, has_permission_per=has_permission_per,
                           permissions=permissions)


@menus.route('/multi/list',methods=["GET","POST"])
def multi_list():


    return render_template('admin/multi_list.html')



@menus.route('/multi/delete/<id>',methods=["GET","POST"])
def multi_delete(id):
    return render_template('admin/multi_list.html')


@menus.route('/test')
def get_all_urls_dict():
    all_permission = Permission.query.all()
    print(all_permission)
    return 'text'


@menus.route('/user_list')
def user_list():
    users = User.query.all()
    return render_template('admin/user_list.html', users = users)

@menus.route('/user_add',methods=["GET","POST"])
def user_add():
    if request.method=="GET":
        form = Users.RegisterForm()
        return render_template('admin/user_list.html', form=form)
    form=Users.RegisterForm(request.form)
    if form.validate():
        pwd = generate_password_hash('111111')
        user = User(
            username=form.username.data,
            password=pwd,
            email=form.email.data,
            telephone=form.telephone.data,
            gender= form.gender.data,
        )
        db.session.add(user)
        db.session.commit()
    return redirect(url_for('menu.user_list'))

@menus.route('/user_edit/user?=<id>',methods=["GET","POST"])
def user_edit(id):
    if request.method == "GET":
        user_obj = User.query.filter_by(id=id).first()
        form = Users.RegisterForm(instance=user_obj)
        return render_template('admin/user_list.html', form=form)
    form = Users.RegisterForm(request.form)
    if form.validate():
        pwd = generate_password_hash('111111')
        user = User(
            username=form.username.data,
            password=pwd,
            email=form.email.data,
            telephone=form.telephone.data,
            gender=form.gender.data,
        )
        db.session.add(user)
        db.session.commit()
    return redirect(url_for('menu.user_list'))


@menus.route('/user_deleter/user?=<id>',methods=["GET","POST"])
def user_deleter(id):
    if request.method=="GET":
        return render_template('admin/delete.html')

    User.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('menu.user_list'))



@menus.route('/goods_list/bid<id>')
def goods_list(id):
    goods_list = Goods.query.filter_by(bid=id).all()
    return render_template('admin/goods_list.html', goods_list=goods_list, bid=id)


@menus.route('/goods_add/<bid>',methods=["GET","POST"])
def goods_add(bid):
    if request.method=="GET":
        form = Good.AddGoodsForm()
        return render_template('admin/change.html', form=form)
    form=Good.AddGoodsForm(CombinedMultiDict([request.form,request.files]))
    if form.validate():
        picture_obj = request.files.get('picture')
        picture_name = picture_obj.filename
        if picture_name.split('.')[1] not in ['jpg','png']:
            flash('图片格式必须为jpg或者png','err')
            return render_template('admin/change.html', form=form)
        upload_path = os.path.join('App/static/uploads' , (str(uuid.uuid4()))+'.'+picture_name.split('.')[1])  # 文件所要存放的目录
        picture_obj.save(dst=upload_path)
        goods = Goods(
            title=form.title.data,
            price=form.price.data,
            picture=upload_path.split('/')[-1],
            bid=bid,
            add_time=time_format.get_current_datetime_str('%Y-%m-%d %H:%M:%S')
        )
        db.session.add(goods)
        db.session.commit()

    return redirect(url_for('menu.goods_list',id=bid))

@menus.route('/goods_edit/<id>',methods=["GET","POST"])
def goods_edit(id):
    goods_obj = Goods.query.filter_by(id=id).first()
    bid = goods_obj.bid
    if request.method == "GET":
        form = Good.AddGoodsForm(instance=goods_obj)
        return render_template('admin/change.html', form=form)
    form = Good.AddGoodsForm(request.form)
    if form.validate():
        goods = Goods(
            title=form.title.data,
            price=form.price.data,
            sid=form.sort.data

        )
        db.session.update(goods)
        db.session.commit()
    return redirect(url_for('menu.goods_list',id=bid))

@menus.route('/goods_delete/<id>',methods=["GET","POST"])
def goods_delete(id):
    if request.method == "GET":
        return render_template('admin/delete.html')
    bid = Goods.query.filter_by(id=id).first()
    Goods.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('menu.goods_list',id=bid))



@menus.route('/sort/list')
def sort_list():
    sort_list = Sort.query.all()
    return render_template('admin/sort_list.html', sort_list = sort_list)

@menus.route('/sort/add',methods=["GET","POST"])
def sort_add():
    if request.method=="GET":
        form = Good.AddSortForm()
        return render_template('admin/change.html', form=form)
    form=Good.AddSortForm(request.form)
    if form.validate():
        sort = Sort(
            title=form.title.data,
            create_date = time_format.get_current_datetime_str('%Y-%m-%d %H:%M:%S')
        )
        db.session.add(sort)
        db.session.commit()
    return redirect(url_for('menu.sort_list'))

@menus.route('/sort/edit/<id>',methods=["GET","POST"])
def sort_edit(id):
    sort_obj = Sort.query.filter_by(id=id).first()
    if request.method == "GET":
        form = Good.AddSortForm(instance=sort_obj)
        return render_template('admin/change.html', form=form)
    form = Good.AddSortForm(request.form)
    if form.validate():
        sort = Sort(
            title=form.title.data,
        create_date = time_format.get_current_datetime_str('%Y-%m-%d %H:%M:%S')
        )
        db.session.update(sort)
        db.session.commit()
    return redirect(url_for('menu.sort_list'))


@menus.route('/sort/deleter/user?=<id>',methods=["GET","POST"])
def sort_deleter(id):
    if request.method=="GET":
        return render_template('admin/delete.html')

    Sort.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('menu.sort_list'))


@menus.route('/brand/list/sid<sid>')
def brand_list(sid):
    brand_list = Brands.query.filter_by(sid=sid).all()
    return render_template('admin/brand_list.html', brand_list = brand_list, sid=sid)

@menus.route('/brand/add/<sid>',methods=["GET","POST"])
def brand_add(sid):
    if request.method=="GET":
        form = Good.AddBrandForm()
        return render_template('admin/change.html', form=form)
    form=Good.AddBrandForm(request.form)
    if form.validate():
        brand = Brands(
            title=form.title.data,
            sid=sid,
            create_date=time_format.get_current_datetime_str('%Y-%m-%d %H:%M:%S')
        )
        db.session.add(brand)
        db.session.commit()
    return redirect(url_for('menu.brand_list',sid=sid))

@menus.route('/brand/edit/<id>',methods=["GET","POST"])
def brand_edit(id):
    brand_obj = Brands.query.filter_by(id=id).first()
    sid = brand_obj.sid
    if request.method == "GET":
        form = Good.AddBrandForm(instance=brand_obj)
        return render_template('admin/change.html', form=form)
    form = Good.AddBrandForm(request.form)
    if form.validate():
        brand = Brands(
            title=form.title.data
        )
        db.session.update(brand)
        db.session.commit()
    return redirect(url_for('menu.brand_list',sid=sid))


@menus.route('/brand/deleter/user?=<id>',methods=["GET","POST"])
def brand_deleter(id):
    if request.method=="GET":
        return render_template('admin/delete.html')

    sid = Brands.query.filter_by(id=id).first().sid
    Brands.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('menu.brand_list',sid=sid))



















from flask import session,render_template,redirect,url_for,request,Blueprint,flash
from ..utils import Roles
from App import db
from ..models import Role



roles = Blueprint('role',__name__)

@roles.route('/role/list')
def role_list():
    role_obj = Role.query.all()
    return render_template('admin/role_list.html', roles=role_obj)



@roles.route('/role/add',methods=["POST","GET"])
def role_add():
    if request.method == "GET":

        form = Roles.AddRoleForm()
        return render_template('admin/change.html', form=form)
    form = Roles.AddRoleForm(request.form)
    if form.validate():
        title = form.title.data
        role = Role(title=title)
        db.session.add(role)
        db.session.commit()
        return redirect(url_for('role.role_list'))
    return render_template('admin/change.html', form=form)


@roles.route('/role/edit/<rid>',methods=["POST","GET"])
def role_edit(rid):
    if request.method == "GET":
        role = Role.query.filter_by(id=rid).first()
        if role:
            form = Roles.AddRoleForm()
            form.title.data = role.title
            return render_template('admin/change.html', form=form)
        else:
            flash('该角色不存在','err')
            return redirect(url_for('role.role_list'))
    form = Roles.AddRoleForm(request.form)
    if form.validate():
        title = form.title.data
        role = Role(title=title)
        db.session.add(role)
        db.session.commit()
        return redirect(url_for('role.role_list'))
    return render_template('admin/change.html', form=form)


@roles.route('/role/delete/<rid>',methods=["POST","GET"])
def role_delete(rid):
    role = Role.query.filter_by(id=rid).first()
    if request.method == "GET":
        if role:
            return render_template('admin/delete.html')
        else:
            flash('该角色不存在','err')
            return redirect(url_for('role.role_list'))
    Role.query.filter_by(id=rid).delete()
    return redirect(url_for('role.role_list'))

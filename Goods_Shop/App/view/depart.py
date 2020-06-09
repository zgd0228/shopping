from flask import session,render_template,redirect,url_for,request,Blueprint,flash
from ..utils import Departs
from App import db
from ..models import Depart



departs = Blueprint('depart',__name__)

@departs.route('/depart/list')
def depart_list():
    depart_obj = Depart.query.all()
    return render_template('admin/depart_list.html', departs=depart_obj)



@departs.route('/depart/add',methods=["POST","GET"])
def depart_add():
    if request.method == "GET":

        form = Departs.AddRoleForm()
        return render_template('admin/change.html', form=form)
    form = Departs.AddRoleForm(request.form)
    if form.validate():
        title = form.title.data
        depart = Depart(title=title)
        db.session.add(depart)
        db.session.commit()
        return redirect(url_for('depart.depart_list'))
    return render_template('admin/change.html', form=form)


@departs.route('/depart/edit/<did>',methods=["POST","GET"])
def depart_edit(did):
    if request.method == "GET":
        depart = Depart.query.filter_by(id=did).first()
        if depart:
            form = Departs.AddRoleForm()
            form.title.data = depart.title
            return render_template('admin/change.html', form=form)
        else:
            flash('该角色不存在','err')
            return redirect(url_for('depart.depart_list'))
    form = Departs.AddRoleForm(request.form)
    if form.validate():
        title = form.title.data
        depart = Depart(title=title)
        db.session.add(depart)
        db.session.commit()
        return redirect(url_for('depart.depart_list'))
    return render_template('admin/change.html', form=form)


@departs.route('/depart/delete/<did>',methods=["POST","GET"])
def depart_delete(did):
    depart = Depart.query.filter_by(id=did).first()
    if request.method == "GET":
        if depart:
            return render_template('admin/delete.html')
        else:
            flash('该角色不存在','err')
            return redirect(url_for('depart.depart_list'))
    Depart.query.filter_by(id=did).delete()
    return redirect(url_for('depart.depart_list'))

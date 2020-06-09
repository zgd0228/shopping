from flask import redirect,session,Blueprint,render_template,make_response,request
from App.utils import Users

from App.models import User

from App import db

adminer = Blueprint('admin',__name__)

@adminer.route('/menu_list',methods=["GET","POST"])
def menu():
    if request.method=="GET":
        return render_template('admin/menu.html')

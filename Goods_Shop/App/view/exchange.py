from flask import request,redirect,render_template,Blueprint,session,url_for,flash
from App.models import *
from ..utils import Users,Good,time_format
from App import db




change = Blueprint('change',__name__)

@change.route('/index')
def index():
    new_goods = Goods.query.filter_by(bid=4).all()
    hot_goods = Goods.query.filter_by(bid=1).all()
    sort_list = Sort.query.all()
    return render_template('index.html',new_goods=new_goods,hot_goods=hot_goods,sort_list=sort_list)

@change.route('/order_list',methods=['POST','GET'])
def order_list():


    return render_template('index.html')

@change.route('/cart')
def shopping_cart():
    cart = Cart.query.filter_by(uid=session.get('user_id')).all()
    return render_template('shopping_cart.html',cart=cart)

@change.route('/goods_detail/<id>')
def goods_detail(id):
    good_detail = Goods.query.filter_by(id=id).first()
    hot_goods = Goods.query.filter_by(bid=1).all()
    return render_template('good_detail.html',goods=good_detail,hot_goods=hot_goods)



@change.route('/goods_search',methods=['POST','GET'])
def goods_search():
    name = request.args.get('keywords','',type=str)
    good_search = Goods.query.filter(Goods.title.like('%'+name+'%')).order_by(Goods.add_time).all()
    hot_goods = Goods.query.filter_by(bid=1).all()
    return render_template('good_search.html',good=good_search,hot_goods=hot_goods)

@change.route('/clear')
def cart_clear():
    return 'xx'

@change.route('/good_list/sort_id=?<id>',methods=['GET','POST'])
def good_list(id):

    good_search = []
    hot_goods = Goods.query.filter_by(bid=1).all()
    brand_list = Brands.query.filter_by(sid=id)
    for item in brand_list:
        goods = Goods.query.filter_by(bid=item.id).all()
        if goods:
            good_search.extend(goods)

    return render_template('good_search.html',good=good_search,hot_goods=hot_goods)

@change.route('/cart_add')
def cart_add():

    cart = Cart(
        gid=request.args.get('goods_id'),
        name=Goods.query.filter_by(id=request.args.get('goods_id')).first().title,
        number = request.args.get('number'),
        uid = session.get('user_id')
    )
    db.session.add(cart)
    db.session.commit()
    return redirect(url_for('change.shopping_cart'))


@change.route('/adder_list',methods=['POST','GET'])
def adder_list():
    adder_list = Adder.query.filter_by(uid=session.get('user_id')).all()
    return 'xx'







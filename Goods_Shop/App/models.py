from App import db

# 会员数据模型
class User(db.Model):
    # 用户
    __tablename__ = 'table_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    password = db.Column(db.String(1024))
    email = db.Column(db.String(32), unique=True)
    telephone = db.Column(db.String(11), unique=True)
    gender = db.Column(db.String(8))
    # rid = db.Column(db.Integer, db.ForeignKey('table_role.id'))
    # role = db.relationship('Role', backref='user')
    role = db.relationship("Role", secondary='table_user_role', backref='role')
    did = db.Column(db.Integer, db.ForeignKey('table_depart.id'))
    depart = db.relationship('Depart', backref='user')

    def __repr__(self):
        return '%s' % self.name


class Depart(db.Model):
    __tablename__ = 'table_depart'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True, unique=True)


    def __repr__(self):
        return '%s' % self.title



class Role(db.Model):
    # 角色
    __tablename__ = 'table_role'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    permission = db.relationship("Permission", secondary='table_role_permission', backref='role')

    def __repr__(self):
        return "%s" % self.title


class User_Role(db.Model):
    __tablename__ = 'table_user_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('table_user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('table_role.id'))


class Menu(db.Model):
    # 菜单
    __tablename__ = 'table_menu'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    icon = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return "%s" % self.title


class Role_Permission(db.Model):
    __tablename__ = 'table_role_permission'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey('table_role.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('table_permission.id'))


class Permission(db.Model):
    # 菜单
    __tablename__ = 'table_permission'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64), unique=True)
    url = db.Column(db.String(255), unique=True)
    mid = db.Column(db.Integer, db.ForeignKey('table_menu.id'))
    menu = db.relationship("Menu", backref='permission')
    pid = db.Column(db.Integer, db.ForeignKey('table_permission.id'), nullable=True)


    def __repr__(self):
        return "%s" % self.title


class Adder(db.Model):
    # 收货地址
    __tablename__ = 'table_adders'
    id = db.Column(db.Integer, primary_key=True)
    adder = db.Column(db.String(64))
    name = db.Column(db.String(32), index=True)
    tele = db.Column(db.Integer)
    uid = db.Column(db.Integer, db.ForeignKey('table_user.id'))
    user = db.relationship("User", backref='adders')

    def __repr__(self):
        return '%s' % self.name


class Cart(db.Model):
    # 购物车
    __tablename__ = 'table_cart'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    uid = db.Column(db.Integer, db.ForeignKey('table_user.id'))
    gid = db.Column(db.Integer, db.ForeignKey('table_goods.id'))
    number = db.Column(db.Integer)
    user = db.relationship("User", backref='cart')
    good = db.relationship("Goods", backref='ref')

    def __repr__(self):
        return '%s' % self.name


class Order(db.Model):
    # 订单
    __tablename__ = 'table_order'
    id = db.Column(db.Integer, primary_key=True)
    good_name = db.Column(db.String(32))
    price = db.Column(db.DECIMAL(10, 2))
    num = db.Column(db.Integer)
    adder_id =  db.Column(db.Integer, db.ForeignKey('table_adders.id'))
    adder = db.relationship("Adder", backref='order')
    statue = db.Column(db.String(32))
    add_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '%s' % self.good_name


class Sort(db.Model):
    # 分类
    __tablename__ = 'table_sort'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True)
    create_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '%s' % self.title


class Brands(db.Model):
    # 品牌
    __tablename__ = 'table_brand'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    create_date = db.Column(db.DateTime, nullable=False)
    sid = db.Column(db.Integer, db.ForeignKey('table_sort.id'))
    sort = db.relationship("Sort", backref='brand')

    def __repr__(self):
        return '%s' % self.title


class Goods(db.Model):
    # 商品
    __tablename__ = 'table_goods'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True)
    price = db.Column(db.DECIMAL(10, 2))
    picture = db.Column(db.String(225), nullable=False)
    add_time = db.Column(db.DateTime, nullable=False)
    bid = db.Column(db.Integer, db.ForeignKey('table_brand.id'))
    brand = db.relationship("Brands", backref='goods')

    def __repr__(self):
        return '%s' % self.title




























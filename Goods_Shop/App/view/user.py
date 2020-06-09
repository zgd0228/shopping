from flask import redirect,session,Blueprint,render_template,make_response,request,flash
from App.utils import Users
import random
import string
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from App.models import User
from werkzeug.security import generate_password_hash,check_password_hash
from App import db

users = Blueprint('users',__name__)

def rndColor():
    '''随机颜色'''
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def gene_text():
    '''生成4位验证码'''
    return ''.join(random.sample(string.ascii_letters+string.digits, 4))


def draw_lines(draw, num, width, height):
    '''划线'''
    for num in range(num):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

def get_verify_code():
    '''生成验证码图形'''
    code = gene_text()
    # 图片大小120×50
    width, height = 120, 50
    # 新图片对象
    im = Image.new('RGB',(width, height),'white')
    # 字体
    font = ImageFont.truetype('app/static/fonts/arial.ttf', 40)
    # draw对象
    draw = ImageDraw.Draw(im)
    # 绘制字符串
    for item in range(4):
        draw.text((5+random.randint(-3,3)+23*item, 5+random.randint(-3,3)),
                  text=code[item], fill=rndColor(),font=font )
    return im, code


@users.route('/code')
def get_code():
    image, code = get_verify_code()
    # 图片以二进制形式写入
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把buf_str作为response返回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = code
    return response


@users.route('/login',methods=["GET","POST"])
def login():
    if 'user_id' in session:
        redirect('index')
    if request.method=='GET':
        form = Users.LoginForm()
        return render_template('login.html',form=form)
    form = Users.LoginForm(request.form)
    if form.validate():
        if session['image'].lower() == form.verify_code.data.lower():
            user = User.query.filter_by(name=form.username.data).first()
            if not user:
                return render_template('login.html',form=form)
            if not check_password_hash(user.password,form.password.data):
                flash('用户名密码错误','err')
                return render_template('login.html', form=form)
            session['user_id'] = user.id
            session['username'] = user.name

            if user.role[0]=='普通用户':
                return redirect('index')
            return redirect('menu')
    return render_template('login.html',form=form)


@users.route('/register',methods=["GET","POST"])
def register():
    if request.method == "GET":
        form = Users.RegisterForm()
        return render_template('register.html', form=form)
    form = Users.RegisterForm(request.form)
    if form.validate():
        user = User(name=form.username.data,
                     password=generate_password_hash(form.password.data),
                     email=form.email.data,
                     telephone=form.telephone.data,
                     gender=str(form.gender.data),
                     did=1
                    )
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        session['username'] = user.name
        return redirect('index')
    return render_template('register.html', form=form)


@users.route('/logout')
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    return redirect('login')


@users.route('/modifypassword',methods=["GET","POST"])
def modify_pwd():
    if request.method=='GET':
        form = Users.Modify_Pwd()
        return render_template('modify_password.html',form=form)
    form = Users.Modify_Pwd(request.form)
    if form.validate():
        user = User.query.filter_by(id=session.get('user_id')).first()
        user.password = generate_password_hash(form.new_password.data)
        db.session.add(user)
        db.commit()
        return redirect('index')
    return render_template('modify_password.html',form=form)
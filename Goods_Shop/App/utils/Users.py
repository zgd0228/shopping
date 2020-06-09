from wtforms import Form
from wtforms.fields import core
from wtforms.fields import simple
from wtforms.fields import html5
from werkzeug.security import check_password_hash
from wtforms import validators,ValidationError
from wtforms import widgets
from flask import session
from ..models import User

class LoginForm(Form):
    username = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空'),
        ],
        widget = widgets.TextInput(),
        render_kw={'class':'form-control'}
    )
    password = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )
    verify_code = simple.StringField(
        'VerifyCode',
        validators=[validators.DataRequired()],
        render_kw={
            "class": "validate-code",
            "size": 18,
            "maxlength": 4,
        }
    )

    submit = simple.SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary login",
        }
    )


class RegisterForm(Form):

    username = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.Length(max=8,min=2,message='用户名长度最小为%s,最长为%s'%(min,max))
        ],
        widget=widgets.TextInput(),
        render_kw={"type"       : "text",
            "placeholder": "请输入用户名！",
            "class":"validate-username",
            "size" : 38,}
    )
    password = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.Length(max=16, min=6, message='密码长度最小为%s-%s' % (min, max))
        ],
        widget=widgets.PasswordInput(),
        render_kw={"placeholder": "请输入密码！",
            "size": 38,}
    )
    pwd_confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.EqualTo('password',message='两次密码输入不一致')
        ],
        widget=widgets.PasswordInput(),
        render_kw={"placeholder": "请输入确认密码！",
            "size": 38,}
    )
    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空'),
            validators.Email(message='邮箱格式不正确')
        ],
        widget = widgets.TextInput(),
        render_kw={"type": "email",
            "placeholder": "请输入邮箱！",
            "size": 38,}
    )
    telephone = simple.StringField(
        label='电话号码',
        validators=[
            validators.DataRequired(message='邮箱不能为空'),
            validators.Length(max=11, min=11, message='电话号码为11位')
        ],
        widget=widgets.TextInput(),
        render_kw={"type": "text",
            "placeholder": "请输入联系电话！",
            "size": 38,}
    )
    gender = core.SelectField(
        label='性别',
        choices=(
            (1,'男'),
            (2,'女')
        ),
        coerce=int,
        default=1
    )
    submit = simple.SubmitField(
        '同意并注册',
        render_kw={
            "class": "btn btn-primary login",
        }
    )

    def validate_email(self, field):
        """
        检测注册邮箱是否已经存在
        :param field: 字段名
        """
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("邮箱已经存在！")

    def validate_phone(self, field):
        """
        检测手机号是否已经存在
        :param field: 字段名
        """
        phone = field.data
        user = User.query.filter_by(telephone=phone).count()
        if user == 1:
            raise ValidationError("手机号已经存在！")

    def validate_user(self, field):
        """
        检测手机号是否已经存在
        :param field: 字段名
        """
        users = field.data
        user = User.query.filter_by(user=users).count()
        if user == 1:
            raise ValidationError("用户名已经存在！")


class Modify_Pwd(Form):
    password = simple.PasswordField(
        label='旧密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.Length(max=16, min=6, message='密码长度最小为%s-%s' % (min, max))
        ],
        widget=widgets.PasswordInput(),
        render_kw={"placeholder": "请输入旧密码！",
                   "size": 38, }
    )
    new_password = simple.PasswordField(
        label='新密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),

        ],
        widget=widgets.PasswordInput(),
        render_kw={"placeholder": "请输入确认密码！",
                   "size": 38, }
    )
    repassword = simple.PasswordField(
        label='再次输入密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.EqualTo('new_password', message='两次密码输入不一致')
        ],
        widget=widgets.PasswordInput(),
        render_kw={"placeholder": "请再次输入确认密码！",
                   "size": 38, }
    )

    submit = simple.SubmitField(
        '修改密码',
        render_kw={
            "class": "btn btn-primary login",
        }
    )

    def validate_old_new(self,field):
        old_pwd = field.data
        user_id = session.get('user_id')
        user = User.query.filter_by(id=user_id).first()
        if not check_password_hash(user.password,old_pwd):
            raise ValidationError('旧密码不正确')


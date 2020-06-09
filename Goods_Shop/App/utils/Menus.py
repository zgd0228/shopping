from wtforms import Form
from wtforms.fields import core
from wtforms.fields import simple
from wtforms.fields import html5
from wtforms import validators,ValidationError
from wtforms import widgets
from flask import session
from ..models import Menu,Permission


ICON_LIST = [
    ['fa-hand-scissors-o', '<i aria-hidden="true" class="fa fa-hand-scissors-o"></i>'],
    ['fa-hand-spock-o', '<i aria-hidden="true" class="fa fa-hand-spock-o"></i>'],
    ['fa-hand-stop-o', '<i aria-hidden="true" class="fa fa-hand-stop-o"></i>'],
    ['fa-handshake-o', '<i aria-hidden="true" class="fa fa-handshake-o"></i>'],
    ['fa-hard-of-hearing', '<i aria-hidden="true" class="fa fa-hard-of-hearing"></i>'],
    ['fa-hashtag', '<i aria-hidden="true" class="fa fa-hashtag"></i>'],
    ['fa-hdd-o', '<i aria-hidden="true" class="fa fa-hdd-o"></i>'],
    ['fa-headphones', '<i aria-hidden="true" class="fa fa-headphones"></i>'],
    ['fa-heart', '<i aria-hidden="true" class="fa fa-heart"></i>'],
    ['fa-heart-o', '<i aria-hidden="true" class="fa fa-heart-o"></i>'],
    ['fa-heartbeat', '<i aria-hidden="true" class="fa fa-heartbeat"></i>'],
    ['fa-history', '<i aria-hidden="true" class="fa fa-history"></i>'],
    ['fa-home', '<i aria-hidden="true" class="fa fa-home"></i>'],
    ['fa-hotel', '<i aria-hidden="true" class="fa fa-hotel"></i>'],
    ['fa-hourglass', '<i aria-hidden="true" class="fa fa-hourglass"></i>'],
    ['fa-hourglass-1', '<i aria-hidden="true" class="fa fa-hourglass-1"></i>'],
    ['fa-hourglass-2', '<i aria-hidden="true" class="fa fa-hourglass-2"></i>'],
    ['fa-hourglass-3', '<i aria-hidden="true" class="fa fa-hourglass-3"></i>'],
    ['fa-hourglass-end', '<i aria-hidden="true" class="fa fa-hourglass-end"></i>'],
    ['fa-hourglass-half', '<i aria-hidden="true" class="fa fa-hourglass-half"></i>'],
    ['fa-hourglass-o', '<i aria-hidden="true" class="fa fa-hourglass-o"></i>'],
    ['fa-hourglass-start', '<i aria-hidden="true" class="fa fa-hourglass-start"></i>'],
    ['fa-i-cursor', '<i aria-hidden="true" class="fa fa-i-cursor"></i>'],
    ['fa-id-badge', '<i aria-hidden="true" class="fa fa-id-badge"></i>'],
    ['fa-id-card', '<i aria-hidden="true" class="fa fa-id-card"></i>'],
    ['fa-id-card-o', '<i aria-hidden="true" class="fa fa-id-card-o"></i>'],
    ['fa-image', '<i aria-hidden="true" class="fa fa-image"></i>'],
    ['fa-mail-reply-all', '<i aria-hidden="true" class="fa fa-mail-reply-all"></i>'],
    ['fa-reply', '<i aria-hidden="true" class="fa fa-reply"></i>'],
    ['fa-reply-all', '<i aria-hidden="true" class="fa fa-reply-all"></i>'],
    ['fa-retweet', '<i aria-hidden="true" class="fa fa-retweet"></i>'],
    ['fa-wrench', '<i aria-hidden="true" class="fa fa-wrench"></i>']]


class AddMenuForm(Form):
    title = simple.StringField(
        label='菜单名称',
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=10,min=2,message='用户名长度为%s-%s'%(min,max))
        ],
        widget = widgets.TextInput(),
        render_kw={'class':'form-control'}
    )

    icon = core.RadioField(
        label= '图标',
        render_kw={'class':'clearfix'},
        choices = ICON_LIST
    )

    submit = simple.SubmitField(
        '提交',
        render_kw={
            "class": "btn btn-primary login",
        }
    )

class AddSecondMenuForm(Form):
    title = simple.StringField(
        label='菜单名称',
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=10,min=2,message='用户名长度为%s-%s'%(min,max))
        ],
        widget = widgets.TextInput(),
        render_kw={'class':'form-control'}
    )

    name = simple.StringField(
        label='路由名称',
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=50, min=2, message='用户名长度为%s-%s' % (min, max))
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )

    url = simple.StringField(
        label='路由',
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=50, min=2, message='用户名长度为%s-%s' % (min, max))
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )


    submit = simple.SubmitField(
        '提交',
        render_kw={
            "class": "btn btn-primary login",
        }
    )


class MutilAddForm(Form):
    title = simple.StringField(
        label='菜单名称',
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=10, min=2, message='用户名长度为%s-%s' % (min, max))
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )

    name = simple.StringField(
        label='路由名称',
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=50, min=2, message='用户名长度为%s-%s' % (min, max))
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )

    url = simple.StringField(
        label='路由',
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=50, min=2, message='用户名长度为%s-%s' % (min, max))
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    mid = core.SelectField(
        label='菜单',
        choices=[(None, '-------------')] ,
        coerce=int,
        default=None
    )
    pid = core.SelectField(
        label='父权限',
        choices=[(None, '-------------')],
        coerce=int,
        default=None
    )
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.mid.choices += Menu.query.all()
        self.pid.choices += Permission.query.filter_by(pid=None).all()



class MutilEditForm(Form):
    title = simple.StringField(
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=20, min=2, message='用户名长度为%s-%s' % (min, max))
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )

    name = simple.StringField(
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=50, min=2, message='用户名长度为%s-%s' % (min, max))
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )

    url = simple.StringField(
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=50, min=2, message='用户名长度为%s-%s' % (min, max))
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )

    mid = core.SelectField(
        label='菜单',
        choices=[(None, '-------------')],
        coerce=int,
        default=None
    )
    pid = core.SelectField(
        label='父权限',
        choices=[(None, '-------------')],
        coerce=int,
        default=None
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mid.choices += Menu.query.all()
        self.pid.choices += Permission.query.filter_by(pid=None).all()


















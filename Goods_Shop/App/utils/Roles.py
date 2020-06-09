from wtforms import Form
from wtforms.fields import core
from wtforms.fields import simple
from wtforms.fields import html5
from wtforms import validators,ValidationError
from wtforms import widgets
from flask import session
from ..models import User,Goods,Sort





class AddRoleForm(Form):
    title = simple.StringField(
        label='角色名称',
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=10,min=2,message='用户名长度为%s-%s'%(min,max))
        ],
        widget = widgets.TextInput(),
        render_kw={'class':'form-control'}
    )


    submit = simple.SubmitField(
        '提交',
        render_kw={
            "class": "btn btn-primary login",
        }
    )



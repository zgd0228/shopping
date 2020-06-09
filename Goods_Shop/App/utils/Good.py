from wtforms import Form
from wtforms.fields import core
from wtforms.fields import simple
from wtforms.fields import html5
from wtforms import validators,ValidationError
from wtforms import widgets
from flask import session
from ..models import User,Goods,Sort

class AddSortForm(Form):
    title = simple.StringField(
        label='分类名称',
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


class AddBrandForm(Form):
    title = simple.StringField(
        label='品牌名称',
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=10,min=1,message='用户名长度为%s-%s'%(min,max))
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


class AddGoodsForm(Form):
    title = simple.StringField(
        label='商品名称',
        validators=[
            validators.DataRequired(message='名称不能为空'),
            validators.Length(max=800,min=1,message='用户名长度为%s-%s'%(min,max))
        ],
        widget = widgets.TextInput(),
        render_kw={'class':'form-control'}
    )
    price = simple.StringField(
        label='商品价格',
        validators=[
            validators.DataRequired(message='不能为空'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    picture = simple.FileField(
        label='商品图片',
        validators = [
                     validators.DataRequired(message='不能为空'),
                 ],
        widget = widgets.FileInput(),
    )
    '''
    sort = core.SelectField(
        label='类别',
        choices=(
        ),
        widget=widgets.Select(),
        coerce=int,
        default=1
    )

    def __init__(self,*args,**kwargs):
        super(AddGoodsForm, self).__init__(*args,**kwargs)
        sort_obj_list = Sort.query.all()
        self.sort.choices = tuple((item.id,item.title)for item in sort_obj_list)
    '''

    submit = simple.SubmitField(
        '提交',
        render_kw={
            "class": "btn btn-primary login",
        }
    )


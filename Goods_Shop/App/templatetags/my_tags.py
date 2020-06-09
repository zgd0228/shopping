from App.models import *
from ..utils import Menus
from collections import OrderedDict


def menu_list():
    menu_list = Menu.query.all()

    menu_dict = {}

    for menu in menu_list:
        menu_dict2 = {}
        menu_dict2['title'] = menu.title
        menu_dict2['icon'] = menu.icon
        menu_dict[menu.id]=menu_dict2

        per_list = []
        permission_list = Permission.query.filter_by(mid=menu.id).all()
        for per in permission_list:
            children_dict = {}
            children_dict['id'] = per.id
            children_dict['title'] = per.title
            children_dict['urls'] = per.url
            per_list.append(children_dict)
        menu_dict[menu.id]['children'] = per_list

    key_list = sorted(menu_dict)
    order_dict = OrderedDict()
    for key in key_list:
        val = menu_dict[key]
        val['class'] = 'hide'
        for item in val['children']:
            if item['id'] == '1':
                item['class'] = 'active'
                val['class'] = ''
        order_dict[key] = val


def bar_list():
    bar_list = [
        {'title': '首页', 'url': '#'}
    ]
    for item in bar_list:
        if not item['pid']:
            bar_list.extend([{'title': item['title'], 'url': item['url'], 'class': 'active'}])
        else:
            bar_list.extend([{'title': item['p_title'], 'url': item['p_url']},
                             {'title': item['title'], 'url': item['url'], 'class': 'active'}])




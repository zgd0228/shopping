file_info = {
   '银川分行市民大厅营销经营情况表':
           {'统计表':
                {'title':'市民大厅批量拓客工作情况统计表',
                'cols':['A','B','C','D','E','F','G','H','I','J','K','L'],
                'widths':[6,14,35,18,12,14,13,13,13,13,13,13]
                 },
           '明细表':
                {'title':'市民大厅批量拓客工作情况明细表',
                'cols':['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'],
                'widths':[6,14,35,18,12,14,13,13,13,13,13,13,13,13,16,33]
                 },
            },
   '客户营销人员':
           {'统计表':
                {'title':'市民大厅批量拓客营销情况统计表',
                'cols':['A','B','C','D','E','F','G','H','I','J','K','L'],
                'widths':[6,14,35,18,12,14,13,13,13,13,13,13]},
           '明细表':
                {'title':'市民大厅批量拓客营销情况明细表',
                'cols':['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'],
                'widths':[6,14,35,18,12,14,13,13,13,13,13,13,13,13,16,33]},
            },
   '客户经营人员':
           {'统计表':
                {'title':'市民大厅批量拓客经营情况统计表',
                'cols':['A','B','C','D','E','F','G','H','I'],
                'widths':[6,14,35,18,12,14,13,13,13]
                 },
           '明细表':
                {'title':'市民大厅批量拓客经营情况明细表',
                'cols':['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'],
                'widths':[6,14,35,18,12,14,13,13,13,13,13,13,13,13,16,33]
                 }
            }
    }

from werkzeug.security import generate_password_hash

xx = generate_password_hash('zgd383161501')
print(xx)



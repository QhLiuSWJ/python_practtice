menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


current_layer = menu
#parent_layer =menu
parent_layer =[]
while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice)==0:continue
    if choice in current_layer:
        parent_layer.append(current_layer)
        #print(parent_layer)
        current_layer=current_layer[choice]
    elif choice =="b":
        if parent_layer:
            current_layer = parent_layer.pop()
    else:
        print(" without this item")
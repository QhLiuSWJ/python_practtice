# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:jsonManuplate.py
@time:2020/03/20
"""

import json
import os, sys

json_path = "C:/Users/QHL/Desktop/打标/3_刘清华/lqh/42.json"


def get_json_data(ss):
    with open(ss, 'rb') as f:
        params = json.load(f)
        params['flags'] = "nin"
        print(params['shapes'][0]['label'])
        for s in params:
            print(s)
            input('等待：')
        f.close()
        print(params)


def write_json_data(dict,ss):
    # 写入json文件

    with open(ss, 'w') as r:
        # 定义为写模式，名称定义为r

        json.dump(dict, r)
        # 将dict写入名称为r的文件中

    r.close()
    # 关闭json写模式


if __name__ == '__main__':
    get_json_data(json_path)

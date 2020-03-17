# re模块提供了re.sub用于替换字符串中的匹配项。
# re.sub(pattern, repl, string, count=0, flags=0)
"""
repl : 替换的字符串，也可为一个函数。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
flags : 编译时用的匹配模式，数字形式。
"""
import re
phone = '电话：13529384859	#欠费了'
# 删除注释
num=re.sub(r'#.*$',' ',phone)
print('phonenumber:',num)
# 移除非数字内容
num = re.sub(r'\D','',phone)
print('phonenumber:',num)

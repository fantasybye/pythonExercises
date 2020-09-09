#! python 3
# 编写一个程序，打开文件夹中所有的.txt 文件，查找匹配用户
# 提供的正则表达式的所有行。结果打印到屏幕上

import re,os
path=input('请输入路径:')
a=os.listdir(path)#列出指定目录下所有的文件名和文件夹名，并赋给a
text=''#初始化text变量
for i in range(len(a)):#迭代a中所有元素，找出符合要求的元素
    if os.path.isfile(os.path.join(path,a[i]))
        and os.path.splitext(os.path.join(path,a[i]))[1]=='.txt':#判断是否为txt文件
        with open(os.path.join(path,a[i]),'r')
        as f:#读取txt文件中的内容，并加到text变量里
            text += f.read()
rg=re.compile(r'\d+')#创建正则表达式
text2=rg.findall(text)#找出匹配正则表达式的内容
print(text2)#输出结果

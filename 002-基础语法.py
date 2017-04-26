#!/usr/bin/python
#-*- coding: UTF-8 -*-

# http://www.runoob.com/python/python-basic-syntax.html
# Python 标识符
# 在 Python 里，标识符有字母、数字、下划线组成。
# 在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
# Python 中的标识符是区分大小写的。
# 以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
# 以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
###
# Python 引号
# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用语文档字符串，在文件的特定地点，被当做注释。
# word = 'word'
# sentence = "这是一个句子。"
# paragraph = """这是一个段落。
# 包含了多个语句"""
###
# python 中多行注释使用三个单引号(''')或三个双引号(""")。
# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# # 文件名：test.py
#
#
# '''
# 这是多行注释，使用单引号。
# 这是多行注释，使用单引号。
# 这是多行注释，使用单引号。
# '''
#
# """
# 这是多行注释，使用双引号。
# 这是多行注释，使用双引号。
# 这是多行注释，使用双引号。
# """

###
# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
# #!/usr/bin/python
#
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# 执行以上代码，输入结果为：
# $ python test.py
# runoob

###
# 多个语句构成代码组
# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。
# 如下实例：
# if expression :
#    suite
# elif expression :
#    suite
# else :
#    suite
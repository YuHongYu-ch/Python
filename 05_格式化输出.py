"""
格式化输出
"""

age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
stu_id2 = 1000

# 今年我的年龄是x岁 --整数 %d
print('今年我的年龄是%d岁' % age)

# 名字是x --字符串 %s
print('我的名字是%s' % name)

# 体重是x --浮点数 %f
print('体重是%.2f' % weight)

# 我的学号是x --整数 %d
print('我的学号是%d' % stu_id)

# 我的学号是001  --
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)

#我的名字是x，今年x岁了
print('我的名字是%s，今年%d岁了' %(name,age))

#我的名字是x，今年x岁了,体重x公斤，学号是x
print('我的名字是%s，今年%d岁了,体重%.2f公斤，学号是%03d' %(name,age,weight,stu_id))
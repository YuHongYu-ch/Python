"""
input接收用户输入
"""
name = input("请输入你的名字:")
print(f'输入的名字是:{name}')

# input接收用户输入的数字并打印出类型
num = input("请输入一个数字：")
print(type(num))

# 转换用户输入的str类型为int类型，并输出验证是否成功
print(type(int(num)))

# eval函数--返回参数的本来类型值。
str1 = '1'
str2 = '1.1'
str3 = '(12,15,22,55)'
str4 = '[22,33,55,66]'

print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))

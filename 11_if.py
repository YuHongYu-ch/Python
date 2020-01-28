print('1↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓if语句')
age = 20
if age >= 18:
    print("已经成年，可以上网")
print('系统关闭')

print('2↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓if语句进阶，接收数据判断')
# input接收上网人员年龄判断是否可以上网。
age1 = int(input('请输入您的年龄：'))
if age1 >= 18:
    print(f'您的年龄为{age1}岁，可以上网。')
print('系统关闭')

print('3↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓if else语句')
# input接收上网人员年龄判断是否可以上网。
age2 = int(input('请输入您的年龄：'))
if age2 >= 18:
    print(f'您的年龄为{age2},可以上网。')
else:
    print(f'年龄{age2}，不满足上网条件。')

print('3↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓if else多重判断语句')
age3 = int(input('请输入年龄:'))
if age3 < 18:
    print('童工')
# elif (age3 >= 18) and (age3 <= 60):
elif 18 <= age3 <= 60:
    print('合法年龄')
else:
    print('退休年龄')

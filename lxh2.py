
a = 6
b = 7
c = '5'
result = a > b
print(result)



# 自己定义的布尔值
a = True
b = False

# 靠程序执行得到的布尔值
c = 5 > 3
d = 7 < 2

print(type(a), a)  # True
print(type(b), b)  # Flase
print(type(c), c)  # True
print(type(d), d)  # Flase


print(bool('hello')) # True
print(bool('0'))	 # True
print(bool('18.5'))	 # True
print(bool('-9'))	 # True
print(bool(''))	     # 


# 使用input()获取用户的输入
name = input('请输入你的姓名：陈冠希')
age = input('请输入你的年龄：19')

# input()获取到的内容全都是字符串类型
print(type(age))



input("请问你叫什么名字？")

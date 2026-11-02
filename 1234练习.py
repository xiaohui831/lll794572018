name = input("请输入你的名字：")
age = input("请输入你的年龄：")
jingbu = input("请输入你的金币数量：")
if int(age) < 18:
    print(f"{name},你未成年，不能参加冒险活动")
else:
    print(f'{name},你已经成年，可以参加冒险活动')
    while int(jingbu) > 10:
        if input("你是否要购买勇者之剑？:(yes/no)") == "yes":
            print(f'{name},你有{jingbu}金币，可以购买勇者之剑')
            jingbu = int(jingbu) - 10
            print(f'你买了一把勇者之剑,花费了10金币，你现在还有{jingbu}金币')
        else:
            print(f'真可惜，期待你下次光临')
            break
        


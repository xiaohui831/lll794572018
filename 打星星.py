def love():
    print(("爱是这个世界上最伟大的"))



def order(num, dish):
    print(f'您点的是：{num}份 {dish}')
    print(f'{dish}可是很好吃的！')
    print(f'你只点了{num}份，够吃吗？\n')

order(5,"辣椒炒肉板面")

def test(b, a=1):
    print(a, b)

test(5)      # 此时 

n = 1
while n <= 10:
    print(f'第{n}次你好啊')
    n += 1
print(f'我是while循环以外的代码，执行到这里时，循环已经结束了，此时的n是：{n}')



print('😦您现在身处密室，需要正确回答问题之后，才能逃出密室！')
riddle = '你是什么人？'
answer = '你的心上人'
guess = ''

while guess != answer:
    print(riddle)
    guess = input('请输入答案：')
    if guess == answer:
        print('✅️答案正确，逃脱成功！')
    else:
        print('❌️回答错误，请再想想！')
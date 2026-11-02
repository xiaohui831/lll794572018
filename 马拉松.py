age = input("请问你的年龄是：")
has_report = input("你有报告吗？（是/否）：")
if int(age) > 18 and int(age) < 56:
    if has_report == "是":
        print("你可以参加马拉松比赛。")
    else:
        print("你需要有报告才能参加马拉松比赛。")
else:
    print("你不在参赛年龄范围内。")
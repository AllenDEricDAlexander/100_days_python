# project higher lower game

import random


def higher_lower_game():
    print("欢迎来到 Higher or Lower 游戏！")
    print("我已经选择了一个 1 到 100 之间的数字。你来猜一猜吧！")

    # 计算机随机选择一个1到100之间的数字
    secret_number = random.randint(1, 100)

    attempts = 0  # 记录猜测的次数

    while True:
        # 玩家输入猜测的数字
        guess = input("请输入你的猜测：")

        # 检查输入是否是有效的数字
        if not guess.isdigit():
            print("请输入一个有效的数字！")
            continue

        guess = int(guess)
        attempts += 1  # 增加猜测次数

        # 判断猜测结果
        if guess < secret_number:
            print("太低了！再试一次。")
        elif guess > secret_number:
            print("太高了！再试一次。")
        else:
            print(f"恭喜你！猜对了！数字是 {secret_number}。")
            print(f"你猜了 {attempts} 次。")
            break


# 启动游戏
higher_lower_game()

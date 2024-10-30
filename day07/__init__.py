# hangman game
# 　for while loops if/else lists
import random


def choose_word():
    words = ['python', 'hangman', 'programming', 'developer', 'challenge']
    return random.choice(words)


def display_hangman(tries):
    stages = [  # 0:头，1:身体，2:左手，3:右手，4:左脚，5:右脚
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |   
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    
           |   
           |
        ''',
        '''
           ------
           |    |
           |    
           |    
           |   
           |
        ''',
        '''
           ------
           |    
           |    
           |    
           |   
           |
        ''',
    ]
    return stages[tries]


def play():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("欢迎来到 Hangman 游戏！")

    while tries > 0 and word_letters != guessed_letters:
        print(display_hangman(tries))
        print("已猜的字母:", ' '.join(guessed_letters))

        # 显示当前的进度
        word_progress = [letter if letter in guessed_letters else '_' for letter in word]
        print("当前单词: ", ' '.join(word_progress))

        guess = input("猜一个字母: ").lower()

        if guess in guessed_letters:
            print("你已经猜过这个字母，请再试一次。")
        elif guess in word_letters:
            guessed_letters.add(guess)
            print("好工作！")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print("抱歉，字母不在单词中。你还剩下 {} 次机会。".format(tries))

    if tries == 0:
        print(display_hangman(tries))
        print("游戏结束！正确的单词是: {}".format(word))
    else:
        print("恭喜你！你猜对了单词: {}".format(word))


if __name__ == "__main__":
    play()

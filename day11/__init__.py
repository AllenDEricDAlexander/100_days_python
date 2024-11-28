# The Blackjack Capstone Project
import random


# 创建一副牌
def create_deck():
    """创建一副标准的 52 张扑克牌。"""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(value, suit) for suit in suits for value in values]
    random.shuffle(deck)
    return deck


# 计算牌面点数
def card_value(card):
    """计算单张牌的点数。"""
    value, suit = card
    if value in ['J', 'Q', 'K']:
        return 10
    elif value == 'A':
        return 11
    else:
        return int(value)


# 计算手牌总点数
def calculate_hand_value(hand):
    """计算手牌的总点数，处理A作为1或11的情况。"""
    total_value = sum(card_value(card) for card in hand)
    # 处理A的情况
    aces = sum(1 for card in hand if card[0] == 'A')
    while total_value > 21 and aces:
        total_value -= 10  # 将A的值从11变成1
        aces -= 1
    return total_value


# 显示手牌
def display_hand(player, hand):
    """显示玩家的手牌和点数。"""
    print(f"{player} 手牌: ", [f"{card[0]} of {card[1]}" for card in hand])
    print(f"{player} 总点数: {calculate_hand_value(hand)}")


# 玩家回合
def player_turn(deck, hand):
    """玩家回合，玩家可以选择要牌或停牌。"""
    while True:
        display_hand("玩家", hand)
        if calculate_hand_value(hand) > 21:
            print("玩家爆点了，游戏结束！")
            return False  # 玩家爆点，游戏结束
        action = input("是否要继续要牌? (y/n): ").lower()
        if action == 'y':
            hand.append(deck.pop())  # 从牌堆拿一张牌
        elif action == 'n':
            break  # 玩家停牌
        else:
            print("无效输入，请输入 'y' 或 'n'。")
    return True


# 庄家回合
def dealer_turn(deck, hand):
    """庄家回合，庄家会按照规则自动抽牌。"""
    while calculate_hand_value(hand) < 17:  # 庄家点数小于17时继续要牌
        hand.append(deck.pop())
    display_hand("庄家", hand)
    if calculate_hand_value(hand) > 21:
        print("庄家爆点了，玩家获胜！")
        return False  # 庄家爆点，游戏结束
    return True


# 结算胜负
def determine_winner(player_hand, dealer_hand):
    """判断胜负。"""
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"\n最终结果: 玩家点数: {player_value}, 庄家点数: {dealer_value}")
    if player_value > 21:
        print("玩家爆点，庄家获胜！")
    elif dealer_value > 21:
        print("庄家爆点，玩家获胜！")
    elif player_value > dealer_value:
        print("玩家获胜！")
    elif player_value < dealer_value:
        print("庄家获胜！")
    else:
        print("平局！")


# 主游戏函数
def play_blackjack():
    """主程序，运行一局黑杰克游戏。"""
    # 创建牌堆
    deck = create_deck()

    # 初始化玩家和庄家的手牌
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # 显示庄家的一张牌（隐藏另一张牌）
    print("庄家手牌: ", [f"{dealer_hand[0][0]} of {dealer_hand[0][1]}", "Hidden"])

    # 玩家回合
    if not player_turn(deck, player_hand):
        return  # 玩家爆点，游戏结束

    # 庄家回合
    if not dealer_turn(deck, dealer_hand):
        return  # 庄家爆点，游戏结束

    # 结算胜负
    determine_winner(player_hand, dealer_hand)


# 启动游戏
if __name__ == "__main__":
    play_blackjack()

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""
def game():  # 定义一个函数
    my_hp = 1000  # 1000赋值给 my_hp
    my_power = 200  # 200赋值给 my_power
    your_hp = 1000  # 1000赋值给your_hp
    your_power = 199  # 199赋值给your_power
    while True:
        my_hp = my_hp - your_power  # 运算
        your_hp = your_hp - my_power  # 运算
        if my_hp <= 0:
                print("你赢了")
                break #退出循环
        elif your_hp <= 0:
                print("我赢了")
                break #退出循环

game() #函数调用

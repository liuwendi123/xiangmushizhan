"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

def game():#定义一个函数
    my_hp = 1000 #1000赋值给 my_hp
    my_power = 200 #200赋值给 my_power
    enemy_hp = 1000 #1000赋值给enemy_hp
    enemy_power = 199 #199赋值给enemy_power
    my_final_hp = my_hp - enemy_power #运算
    enemy_final_hp = enemy_hp - my_power # 运算
    if my_final_hp > enemy_final_hp:
        print("我赢了")
    else:
        print("你赢了")


game() #函数调用

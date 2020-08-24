


class GameContra(object):
    def __init__(self, name, hp=1000, attack=200):
        self.name = name
        self.hp = int(hp)
        self.attack = int(attack)


def fight(player, enemy):
    while (player.hp) > 0 and (enemy.hp > 0):
        player.hp = player.hp - enemy.attack
        enemy.hp = enemy.hp - player.attack

        if player.hp != 0 and enemy.hp != 0:
            print(f'【玩家】剩余血量:{player.hp} \n【玩家】攻击力:{player.attack}')
            print('————————————————')
            # time.sleep(1.5)
            print(f'【敌人】剩余血量：{enemy.hp} \n【敌人】攻击力:{enemy.attack}')
            print('————————————————')
            # time.sleep(1.5)
        elif player.hp == 0:
            print(f"冠军是：{player.name}")
        else:
            print(f"冠军是：{enemy.name}")

A1 = GameContra("yang")
# print(A1.person())
A2 = GameContra("liu")
# print(A2.person())
fight(A1, A2)
# print(B1.fight())
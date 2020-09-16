"""
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""
class dog :
    hair = "brown"
    Claw = "攻击敌人"
    def __init__(self,hair,Claw):
        self.hair=hair
        self.Claw=Claw
    print(f"爪子的颜色是{hair}")
    print(f"用来{Claw}")
class bingxiang:
    Beer = "三得利"
    Icecream = "小布丁"
    def __init__(self,Beer,Icecream):
        self.Beer=Beer
        self.Icecream=Icecream
class zhangwuji:
    neigong="九阳神功"
    waigong="乾坤大挪移"
    def __init__(self,neigong,waigong):
        print(neigong)
        print(waigong)
class crocodile:
    character="冷血"
    weight = 2000
    tooth ="锋利"
    def __init__(self,character,weight,tooth):
        print(character)
        print(weight)
        print(tooth)

class caixukun:
    levelofappearance = "帅气"
    height = 180
    song = "情人"
    print(levelofappearance)
    print(height)
    print(song)
# coding: utf-8

print("#スコープ")
message = "paiza"
a = 10
b = 20
def sum(x, y):
    a = 3
    global message
    message += "paiza"
    print(message + " " + str(a))
    return x + y
num = sum(a, b)
print(num)
print(message + " " + str(a))

print("#クラス内でメソッドを定義するときはselfを定義しないといけない")
class Player01:
    # クラスからオブジェクトを作るとき、
    # オブジェクトの初期化をする
    # ⇒コンストラクタを追加
    def __init__(self,job):
        self.job = job  #インスタンス変数
    def walk(self):#クラス内は引数にselfが必要
        print(self.job +" is walking")
player1 = Player01("BOY")
player1.walk()  #BOY is walking
player2 = Player01("Girl")
player2.walk()  #Girl is walking

class Item:
    tax = 1.08
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    def total(self):
        return int(self.price * self.quantity * Item.tax)
apple = Item(120, 15)
total = apple.total()
print("合計金額は" + str(total) + "円です")
orange = Item(85, 32)
print("合計金額は" + str(orange.total()) + "円です")


class Player:
    Characteristic = 1.2
    def __init__(self, job, weapon):
        self.job = job
        self.__weapon = weapon#プライベート変数  #アクセス制限

    def walk(self):
        print(self.job + "は荒野を歩いていた")
        self.__attack("スライム")  #アクセス制限

    def __attack(self, enemy): #プライベートメソッド
        print(self.__weapon + "で" + enemy + "を攻撃")
        print(str(Player.Characteristic*100)+"のダメージ")

player1 = Player("戦士", "剣")
player1.walk()
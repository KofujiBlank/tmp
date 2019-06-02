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


#継承
class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた。")

class JewelryBox(Box):
    def look(self):
        print("宝箱はキラキラと輝いている。")

box = Box("鋼鉄の剣")
box.open()

jewelrybox = JewelryBox("魔法の指輪")
jewelrybox.look()
jewelrybox.open() #定義されていないものがあるとスーパークラスから呼び出される

#スーパークラスで定義したメソッドと同じ名前メソッドをサブクラスで作るとオーバーライドされる


class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    def say_hello(self, target):
        print(self.msg, target)

player = Hello()
player.say_hello("python")



player = Hello()
player.say_hello("python")

class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

class Wizard(Player):
    def __init__(self):
        super().__init__("魔法使い")

    def attack(self, enemy):
        self.__spell()
        print(self.name + "は、" + enemy + "に炎を放った！")

    def __spell(self):
        print("ズバーン！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
# hero.attack("スライム")
warrior = Player("戦士")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

wizard._Wizard__spell()

#clsはクラスメゾットのことselfとかと一緒
#pythonは関数もオブジェクト
class Player:
    __charactor_count = 0

    #@classmethod
    def summary(cls):
        print(str(Player.__charactor_count) + "人で、スライムを攻撃した。")
    def __init__(self, name):
        self.name = name
        Player.__charactor_count += 1
        print(str(Player.__charactor_count) + "番目のプレイヤー、" + self.name + "が登場した。")

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")
    summary = classmethod(summary)#@classmethod で代用できる
    #渡した関数をクラスメゾットにして返してくれる    
    
class Wizard(Player):
    def __init__(self):
        super().__init__("魔法使い")

    def attack(self, enemy):
        self.__spell()
        print(self.name + "は、" + enemy + "に炎を放った！")

    def __spell(self):
        print("ズバーン！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
warrior = Player("戦士")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

Player.summary()

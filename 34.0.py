class Person:
    def greeting(self):
        print("hello")


# 클래스 사용 시,
james = Person()

# 매서드 호출 시, 인스턴스를 통해 호출 함
james.greeting()

# 인스턴스와 객체는 같지만, 클래스와 연관되어 있을 시에만 인스턴스로 이름을 바꾸면 됨


class Person:
    def __init__(self):
        self.hello = "안녕하세요"

    def greetings(self):
        print(self.hello)


maria = Person()
maria.greeting()


class Person():
    def __init__(self, name, age, address, wallet)
    self.name = name
    self.age = age
    self.address = address
    self.__wallet = wallet

    def greeting(self):
        print({0} I am {1}.format(self.hello, self.name))

    def pay(self, amount)
    print("you are now {0} left".format(self.__wallet))


maria = Person()
maria.greeting()
maria.pay(3000)
print("이름: ", maria.name)


class Knight(self):
    def slash(self, health, manam, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print("베기")


class Annie:
    def tibbers(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print("티버: 피해량 {0}".format(self.ability_power * 0.65 + 400))

        If else
    if else

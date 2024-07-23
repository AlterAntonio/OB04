from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self):
        self.ammo = True
        self.range = 1
        self.damage = 5
        self.name = 'меч'

    def attack(self, monster):
        if monster.distance > self.range:
            print('Монстр вне досягаемости меча')
        else:
            monster.take_damage(self.damage)

    def __str__(self): return f'{self.name}, урон: {self.damage}, дальность поражения: {self.range}'

class Bow(Weapon):
    def __init__(self):
        self.ammo = 10
        self.range = 12
        self.damage = 4
        self.name = 'лук'

    def attack(self, monster):
        if monster.distance > self.range:
            print('Промах! Монстр вне досягаемости стрел.')
            self.ammo -= 1
            print(f'Стрел осталось: {self.ammo}')
        else:
            if self.ammo > 0:
                self.ammo -= 1
                monster.take_damage(self.damage)
                print(f'Стрел осталось: {self.ammo}')
            else:
                print('Колчан пуст! Надо срочно поменять оружие!')

    def __str__(self): return (f'{self.name}, урон: {self.damage}, дальность поражения: {self.range}, стрел осталось: '
                               f'{self.ammo}')

class Rifle(Weapon):
    def __init__(self):
        self.ammo = 5
        self.range = 20
        self.damage = 6
        self.name = 'охотничий карабин'

    def attack(self, monster):
        if monster.distance > self.range:
            print('Промах! Монстр вне досягаемости.')
            self.ammo -= 1
            print(f'Пуль в обойме: {self.ammo}')
        else:
            if self.ammo > 0:
                self.ammo -= 1
                monster.take_damage(self.damage)
                print(f'Патронов в обойме: {self.ammo}')
            else:
                print(f'Обойма пустая, надо срочно поменять оружие!')

    def __str__(self): return (f'{self.name}, урон: {self.damage}, дальность поражения: {self.range}, патронов в '
                               f'обойме: {self.ammo}')

class Fighter:
    def __init__(self, *args: Weapon, health=50):
        self.health = health
        self.arsenal = args
        self.using_weapon = args[0]
        print(f'У бойца в руках {self.using_weapon}')

    def move(self, monster):
        print('Вы решили приблизиться к монстру.')
        monster.attack(self)

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0: print(f'Боец получил урон {damage}, осталось HP: {self.health}')
        else: print(f'Потрачено')

    def changeWeapon(self):
        choice = 1
        print(f'У вас в арсенале есть:')
        for weapon in self.arsenal:
            if weapon is self.using_weapon:
                print(f'{choice} - {weapon}, сейчас используется')
            else: print(f'{choice} - {weapon}')
            choice += 1

        try: user_choice = int(input('Ваш выбор: ')) - 1
        except: print('Введите доступный номер из списка!')
        else:
            if user_choice in range(len(self.arsenal)):
                self.using_weapon = self.arsenal[user_choice]
                print(f'У бойца в руках {self.using_weapon}')


class Monster:
    def __init__(self, health=100, damage=8, distance=25):
        self.health = health
        self.damage = damage
        self.distance = distance
        print(f'Монстр приближается! Дистанция - {self.distance}')

    def attack(self, fighter):
        if self.distance == 1: fighter.take_damage(self.damage)
        else:
            self.distance -= 1
            print(f'Монстр приближается! Дистанция - {self.distance}')

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f'Монстр получил урон {damage}, осталось HP: {self.health}')
        else:
            print(f'Монстр убит')


fighter = Fighter(Sword(), Bow(), Rifle())
monster = Monster(health=100, distance=21)

while fighter.health > 0 and monster.health > 0:
    print('Ситуация развивается стремительно, надо действовать!')
    print(f'1 - атаковать монстра выбранным оружием: {fighter.using_weapon.name}\n2 - поменять оружие\n3 - '
          f'приблизиться к врагу')
    user_choice = input('Ваш выбор: ')
    match user_choice:
        case '1':
            fighter.using_weapon.attack(monster)
            monster.attack(fighter)
        case '2':
            fighter.changeWeapon()
            monster.attack(fighter)
        case '3':
            fighter.move(monster)
            monster.attack(fighter)

















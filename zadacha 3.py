import random
class Voin(object):
    def __init__(self, x): #Создается юнит со значением здоровья, которое выберет пользователь.
        self._unit = x

    def get(self): #Возвращается значение здоровья юнита
        return self._unit

    def set(self, health): #Изменяется значение здоровья юнита
        self._unit = health
    def fight(self,obj): #Инцилизация боя
        print('Бой начался!')
        while self.get() > 0 and obj.get() > 0:
            a = random.randint(1,2) #Рандомный выбор юнита, который совершает удар
            if a == 1:
                obj.set(obj.get()-20)
                print('Ударил первый юнит. Оставшееся здоровье:')
                print('Юнит 1:', self.get() )
                print('Юнит 2:', obj.get() )
            if a == 2:
                self.set(self.get()-20)
                print('Ударил второй юнит. Оставшееся здоровье:')
                print('Первый юнит:', self.get() )
                print('Второй юнит:', obj.get() )
        if obj.get() == 0:
            print('Бой окончен. Победил первый юнит.')
        else:
            print('Бой окончен. Победил второй юнит.')
unit1 = Voin(100)
unit2 = Voin(100)
unit1.fight(unit2)
while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)

# Наследование
class Animal:
    engry = "Engry"

    def __init__(self,name,age): # метод инициализации класса
        self.name = name
        self.age = age

class Dog(Animal):

        def voice(self):
            print(f"{self.name} Gav !")


barsik = Dog("Barsik", 18)
barsik.name = "I am not Barsik"
print(Animal.engry)
barsik.voice()

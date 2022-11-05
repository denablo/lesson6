class Grandpatent:
    height = 160
    age = 60
    power = 100
class Parent(Grandpatent):
    height = 170
    age = 40
class Child(Parent):
    age = 13
    def __init__(self):
        print(self.height)
        print(self.power)
        print(self.age)
Deniska = Child()

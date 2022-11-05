class General:
    height = 170
    age = 60
    power = 150
class Sergant(General):
    height = 190
    age = 40
    power = 100
class Novichok(Sergant):
    age = 13
    def __init__(self):
        print(self.height)
        print(self.power)
        print(self.age)
Deniska = Novichok()

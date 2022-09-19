
'''
class Drink:
    def __init__(self, cup_volume, owner):
        self.volume = cup_volume 
        self.owner = owner
        self.cup_volume = cup_volume

    def whose_drink(self):
        return f'this drink belongs to {self}'
    
    def sip_drink(self, size):
        if size == 'gulp':
            self.volume -= 2.5
        elif size == 'chug':
            self.volume -= self.volume
        else:
            self.volume -= 0.1
        return self.volume

    def refill_drink(self, size):
        self.refill

drink = Drink(12, 'Zach')

print(drink.whose_drink())
'''

# text = open('text.txt')
# words = text.read()
# print(words)
with open('text.txt', 'r') as text:
    words = text.read()

print(words)
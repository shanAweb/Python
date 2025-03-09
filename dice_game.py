import random
class Dice:
    def roll(self):
        dec_x = random.randint(1, 6)
        dec_y = random.randint(1, 6)
        return dec_x, dec_y


dice1 = Dice()
result = dice1.roll()
print(result)

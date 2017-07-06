# Program: dice.py
# Class definition for an n-sided dice

from random import randrange

class MSDie:

    def __init__(self,n):
        self.sides = n
        self.value = 1

    def roll(self):
        self.value = randrange(1,self.sides+1)

    def getValue(self):
        return self.value

    def setValue(self,x):
        self.value = x

#!/usr/bin/env python
class Stats:
    def __init__(self, name):

        self.name = name
        self.hp = 100
        self.st = 100
        self.mag = 100

    def Display(self):

        print("Name : ", self.name,
            "\nhp = ", self.hp,
            "\nst =", self.st,
            "\nmag =", self.mag, "\n")
        self.Modify()

    def Modify(self):

        # edit user stats
        b = int(input("How many points would you like to add?"))

        if b > 5:
            print("Sorry, you can only add in max increments of 5.")
            self.Modify()


        c = input("Which Stat would you like to edit?"
                "\nst | hp | mag :")

        # User Options
        if c == "mag":

            self.mag += + b
            self.Display()

        elif c == "st":

            self.st += b
            self.Display()

        elif c == "hp":

            self.hp += b
            self.Display()

        else:
            
            print("invalid input")
            self.Modify()

class Hero(Stats):

    def __init__(self, name):
        Stats.__init__(self, name)
        self.Display()

amra = Hero("Amrasurion")

#!/usr/bin/env python3

class addList:
    def append():
        x = []
        try:
            y = input("Which number would you like to add to the list? :")
            y = int(y)
            if type(y) == int or type(y) == float:
                x.append(y)
                print(x)
                while True:
                    print('1. would you like to add another number? : ')
                    print('yes or no')
                    a = input()
                    yes = 'yes'
                    no = 'no'
                    if a == yes:
                        print('2. add another number : ')
                        z = input()
                        try:
                            z = int(z)
                            x.append(z)
                            print(x)
                        except:
                            print('invalid input, try again.')
                            while True:
                                print('add another number : ')
                                z = input()
                                try:
                                    z = int(z)
                                    x.append(z)
                                    print(x)
                                    break
                                except:
                                    print("invalid input.")
                                    break
                    else:
                         exit('goodbye')
        except ValueError:
            print('invalid number')
            addList.append()
addList.append()

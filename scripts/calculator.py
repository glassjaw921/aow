#!/usr/bin/env python

class calculator:

    def addition(x,y):
        return(x + y)

    def subtraction(x,y):
        return(x - y)

    def multiplication(x,y):
        return(x * y)

    def division(x,y):
        return(x / y)

    def average(x,y):
        return((x + y) / 2)

    def nextMod(x,y):
        print('What would you like to do?')
        print('add, sub, mult, div, or avg :')
        i = input()
        a = 'add'
        s = 'sub'
        m = 'mult'
        d = 'div'
        av = 'avg'
        if i == a:
            print(x, "+", y, "=", calculator.addition(x, y))
        if i == s:
            print(x, "-", y, "=", calculator.subtraction(x, y))
        if i == m:
            print(x, "*", y, "=", calculator.multiplication(x, y))
        if i == d:
            print(x, "/", y, "=", calculator.division(x, y))
        if i == av:
            print(x, "+", y, "/ 2", "=", calculator.average(x, y))

    def integers():
        #print('\n' * 50)
        x = int(input("X Must be a number : "))
        y = int(input("Y Must Number : "))
        print('add, sub, mult, div, or avg :')
        i = input()
        a = 'add'
        s = 'sub'
        m = 'mult'
        d = 'div'
        av = 'avg'

        if i == a:
            print(x,"+",y,"=", calculator.addition(x, y))
            while True:
                print('Would you like to use new numbers? yes or no')
                n = input()
                if n == 'yes':

                    calculator.integers()
                elif n == 'no':
                    calculator.nextMod(x,y)
                else :
                    print('Invalid Input choose from the following')
                    calculator.nextMod(x,y)
        elif i == s:
            print(x, "-", y, "=", calculator.subtraction(x, y))
            while True:
                print('Would you like to use new numbers? yes or no')
                n = input()
                if n == 'yes':

                    calculator.integers()
                elif n == 'no':
                    calculator.nextMod(x, y)
                else:
                    print('Invalid Input choose from the following')
                    calculator.nextMod(x, y)

        elif i == m:
            print(x, "*", y, "=", calculator.multiplication(x, y))
            while True:
                print('Would you like to use new numbers? yes or no')
                n = input()
                if n == 'yes':

                    calculator.integers()
                elif n == 'no':
                    calculator.nextMod(x, y)
                else:
                    print('Invalid Input choose from the following')
                    calculator.nextMod(x, y)

        elif i == d:
            print(x, "/", y, "=", calculator.division(x, y))
            while True:
                print('Would you like to use new numbers? yes or no')
                n = input()
                if n == 'yes':

                    calculator.integers()
                elif n == 'no':
                    calculator.nextMod(x, y)
                else:
                    print('Invalid Input choose from the following')
                    calculator.nextMod(x, y)

        elif i == av:
            print(x, "+", y, "/ 2", "=", calculator.average(x, y),"%")
            while True:
                print('Would you like to use new numbers? yes or no')
                n = input()
                if n == 'yes':
                    calculator.integers()
                elif n == 'no':
                    calculator.nextMod(x, y)
                else:
                    print('Invalid Input choose from the following')
                    calculator.nextMod(x, y)
        else :
            print('invalid input choose from the following')
            calculator.nextMod(x,y)
calculator.integers()

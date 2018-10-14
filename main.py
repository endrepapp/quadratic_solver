#!/usr/bin/python
# -*- coding: utf-8 -*-
#  Ez azért kell, mert így elfogadja az ékezetet. UTF-8-as betűkódolásra váltottunk

from math import *
# TASK: quadratic formula solver

# Example 1
# ax^2 + bx + c = 0
# a = 2 - input
# b = -3 - input
# c = 1 - input
# Equation: 2x^2 - 3x + 1 = 0. Press ENTER to start - input
# Result: x_1 = 1.0000; x_2 = 0.5000;

# Example 2
# a = 1 - input
# b = 2 - input
# c = 1 - input
# Equation: 1x^2 + 2x + 1 = 0. Press ENTER to start - input
# Result: x = -1.0000;

# Example 3
# Result: equation can not be solved

def main():
    print('ax^2 + bx + c = 0')
    a = szam_beker("a")
    # ha a nem nagyobb mint 0, akkor nincs értelme
    if a == 0:
        print("Ez nem másodfokú egyenlet!")
        return
    # a értékhez előjel kiíratás
    elif a < 0:
        s_a = "- {}".format(abs(a))
    else:
        s_a = a
    b = szam_beker("b")
    c = szam_beker("c")

    # b, c értékekhez előjel kiíratás
    if b < 0:
        s_b = "- {}".format(abs(b))
    else:
        s_b = "+ {}".format(b)
    if c < 0:
        s_c = "- {}".format(abs(c))
    else:
        s_c = "+ {}".format(c)

    # az egyenlet kiíratásánál figyelni kell az előjelre
    input("Equation: {}x^2 {}x {} = 0. Press ENTER to start".format(s_a,s_b,s_c))

    det = determinans(a,b,c)
    if det < 0:
        # ha nincs megoldása az egyenletnek, ki is lépünk
        print("Result: equation can not be solved")1
        return # kilépés
    elif det == 0:
        # ha csak egy megoldása van
        x = - b / (2 * a)
        print("Result: x = {}".format(x))
    else:
        # ha két megoldása van
        x_1 = (-b + sqrt(det)) / (2 * a)
        x_2 = (-b - sqrt(det)) / (2 * a)
        print("Result: x_1 = {}; x_2 = {};".format(x_1, x_2))
    return

def szam_beker(betu):
    return int(input("{} = ".format(betu)))

def determinans(a,b,c):
    return b * b - 4 * a * c

if __name__ == '__main__':
    main()
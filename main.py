
# TASK: quadratic formula solver

# Example 1
# ax^2 + bx + c = 0
# a = 2  - input
# b = -3 - input
# c = 1  - input
# Equation: 1x^2 + 2x + 3 = 0. Press ENTER to start - input
# Result: x_1 = 1.0000; x_2 = 0.5000;

# Example 2
# a = 1 - input
# b = 2 - input
# c = 1 - input
# Equation: 1x^2 + 2x + 1 = 0. Press ENTER to start - input
# Result: x = -1.0000;

# Example 3
# Result: equation can not be solved

from math import*
print "udvozlom az ekezet nelkuli fuggveny megoldoban."

a = int(input("Kerem adja meg az a - erteket: "))
b = int(input("Kerem adja meg az b - erteket: "))
c = int(input("Kerem adja meg az c - erteket: "))

#int tenyésztés folyott itt végbe, ne kérdezd miért csináltam , én se tudom...
szam1 = int
szam2 = int
szam3 = int
szam4 = int
szam5 = int
szam6 = int
szam7 = int
szam8 = int
szam9 = int
szam10 = int
szam11 = int
szam12 = int

if(a==0&b==0&c==0):
    print ("minek kezdett bele?! ")
else:
    szam1 = b * (-1)
    szam2 = b * b
    szam3 = 4 * a * c
    szam4 = (szam2) - (szam3)
if(szam4<0):
    print "gyok alatt a szammok fosast eredmenyeztek"
else:
#minuszos----------------
    szam5 = sqrt(szam4)
    szam6 = szam1 - szam5
    szam7 = 2 * a
    szam8 = szam6 / szam7
#pluszos-----------------
    szam10 = sqrt(szam4)
    szam11 = szam1+ szam10
    szam12 = szam10/szam7

    if(szam8==0):
        print "nop"
    else:
        print "x1: %s." % (szam8)
    if(szam12 == 0):
        print "nop"
    else:
        print "x2: %s." % (szam12)




def main():
    print('test')
    return

if __name__ == '__main__':
    main()
from math import *
print ("Equation: ax^2 - bx + c = 0. Press ENTER to start")




def szam_beker(betu):
    return int(input("Kerem adja meg az {} - erteket: ".format(betu)))


def neg_szamolas(a,b,c):
    if (a == 0 & b == 0 & c == 0):

        print ("nem angolozok , ilyen ertek nincs ")
    else:
        minusz_B = b * (-1)
        negyzet_B = b * b
        gyok_masodik = 4 * a * c
        gyok_muv = (negyzet_B) - (gyok_masodik)
    if (gyok_muv < 0):
        print "equation can not be solved"
    else:
        # minuszos----------------
        sqrt_muv = sqrt(gyok_muv)
        veg_muv = minusz_B - sqrt_muv
        oszto = 2 * a
        minusz_eredmeny = veg_muv / oszto
    return minusz_eredmeny


def main():
    print "udvozlom az ekezet nelkuli fuggveny megoldoban."

    a = szam_beker("a")
    b = szam_beker("b")
    c = szam_beker("c")
    print neg_szamolas(a,b,c)


if __name__ == '__main__':
    main()

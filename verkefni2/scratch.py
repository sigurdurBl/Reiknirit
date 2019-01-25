import math
"""
#verkefni 3
def summa(m):
    if m == 1:
        return 1
    else:
        return pow(m,2) + summa(m-1)

#verkefni 4
def runa(n):
    if n == 1:
        print 1,
    else:
        runa(n-1)
        print (n*(n+1)//2),
"""

#verkefni 5
def tversumma(n):
    if n ==  "":
        return 0
    else:
        return int(n[0]) + tversumma(n[1:])


def samnefari(n,m):
    if m == 0:
        return n
    else:
        return samnefari(m,n % m)


"""tala = input("Enter a number: ")

print tversumma(str(tala))"""
print (samnefari(3,19))

from math import *
class Vigur:

    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self,x,y):
        self.x = x
        self.y = y


    # Fall sem skrifar hnit vigurs á skjá

    def prenta(self):
        print("< %s, %s >" %(self.x,self.y))


    # Fall sem skilar lengd
    def lengd(self):
        return sqrt(self.x**2+self.y**2)

    # Fall sem skilar hallatölu
    def halli(self):
        return (self.y/self.x)


    # Fall sem skilar þvervigri
    def þvervigur(self):
        return Vigur(-self.y,self.x)

    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):
        if self.y < 0:
            return -degrees(acos(self.x/self.lengd()))
        else:
            return degrees(acos(self.x/self.lengd()))

    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self,v):
        innfelldi = self.x*v.x+self.y*v.y
        return abs(degrees(acos(innfelldi/(self.lengd() * v.lengd()))))


    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self,v):
        return Vigur(self.x +v.x,self.y + v.y)

# Keyrsluforrit
v1 = Vigur(-4,4)


v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())

vþ = v1.þvervigur()
print("tvervigur: "),
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(1,1)
print("Horn milli vigra: " , v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: "),
v3.prenta()


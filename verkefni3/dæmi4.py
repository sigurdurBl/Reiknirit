import  itertools
import string

def alfabet(m,n):
    return(itertools.combinations(m,n))

m = string.ascii_lowercase
n = 5


svar = itertools.combinations(m,5)

#for i in list(svar):
    #print("".join(i))

listi = []

for i in list(svar):
    listi.append("".join(i))


print(listi)

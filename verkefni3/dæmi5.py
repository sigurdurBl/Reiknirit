import  itertools
import string
def quicksort(x):
      if len(x) < 2:
          return x
      else:
          pivot = x[0]
          less = [i for i in x[1:] if i <= pivot]
          greater = [i for i in x[1:] if i > pivot]
          return quicksort(less) + [pivot] + quicksort(greater)

def alfabet(m,n):
    return(itertools.combinations(m,n))

m = string.ascii_lowercase
n = 5

svar = itertools.combinations(m,2)
cnt = 0




listi = []

for i in list(svar):
    listi.append("".join(i))
for x in listi:
    listi.reverse()
print(listi)
print(quicksort(listi))

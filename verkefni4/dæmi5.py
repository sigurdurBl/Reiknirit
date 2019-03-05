import bisect  
  
def sort(listi, n): 
    bisect.insort(listi, n)  
    return listi
  
listi = [1, 2, 4,5,6,7,8,9] 
a = int(input("slaðu in tölu"))
  
print(sort(listi, a)) 

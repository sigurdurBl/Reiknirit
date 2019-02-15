
def search(List,item):
    for i in range(len(List)):
        if List[i]==item:
            return i
    return -1

List = [1,7,6,5,8,9,4,5]
print("number in List :", List)
x = int(input("enter searching number :"))

result = search(List,x)
if result==-1:
     print("number not found in the list")
else:
     print( "number " + str(x) + " is found at position %d" %(result))

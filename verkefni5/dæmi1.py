class Node:
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None


    def append(self,d):
        if self.nxt:
            return self.nxt.append(d)
        else:
            curr = Node(d)
            self.nxt = curr
            curr.prv = self
            return True


    def printList(self):
        print(self.data),
        if self.nxt:
            self.nxt.printList()
        else:
            print("")



    def find(self, d):
        if self.data == d:
            return True
        else:
            if self.nxt:
                return self.nxt.find(d)
            else:
                return False



    def delete(self, d):
        # Ef aftasti hnútur
        if self.data == d and self.nxt is None:
            self.prv.nxt = None
            self.prv = None
            return True
        elif self.data == d:
            self.prv.nxt = self.nxt
            self.nxt.prv = self.prv
        # elif if self.data == d and self.nxt is None:
        else:
            if self.nxt:
                return self.nxt.delete(d)
            else:
                return False


class DLL: # DLL = Dobule Linked List
    def __init__(self):
        self.head = None


    def push(self,d):
        if self.head:
            temp_next = self.head
            self.head = Node(d)
            self.head.nxt = temp_next
        else:
            self.head = Node(d)



    def append(self, d):
        if self.head:
            return self.head.append(d)
        else:
            self.head = Node(d)
            return True


    def printList(self):
        if self.head:
            self.head.printList()
        else:
            print("Empty list!")


    def find(self, d):
        if self.head:
            return self.head.find(d)
        else:
            return False


    def delete(self, d):
        if self.head is None:
            return False
        elif self.head.data == d:
            self.head = self.head.nxt
            return True
        else:
            return self.head.delete(d)
dbl = DLL()
dbl.append(5)
dbl.append(6)
dbl.append(1)
dbl.printList()
print(dbl.delete(1))
dbl.printList()
dbl.push(2)
dbl.printList()
print(dbl.find(12))
"""
dbl.append(5)           # 5
dbl.append(7)           # 5 7
dbl.push(1)             # 1 5 7
dbl.push(0)             # 0 1 5 7
dbl.append(10)          # 0 1 5 7 10
dbl.printList()

dbl.push(7)
dbl.printList()

print(dbl.delete(7))
dbl.printList()
"""

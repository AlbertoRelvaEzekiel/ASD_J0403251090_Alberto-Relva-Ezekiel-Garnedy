#=================================================
#Nama   : Alberto Relva Ezekiel Garnedy
#Nim    : J0403251090
#kelas  : A1
#=================================================

#=================================================
#Implementasi dasar : Node pada linked list
#=================================================

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

current = head
while current is not None :
    print(current.data)
    current = current.next

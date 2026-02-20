#=================================================
#Nama   : Alberto Relva Ezekiel Garnedy
#Nim    : J0403251090
#kelas  : A1
#=================================================

#=================================================
#Implementasi dasar : Stack
#=================================================


class Node :
    def __init__(self,data) :
        self.data = data
        self.data = None



class stack : 
    def __init__(self) :
        self.top = None

    def push(self,data) : 
        nodeBaru = Node(data)

        nodeBaru.next = self.top

        self.top = nodeBaru

def tampilkan(self) :
    current = self.top
    print("Top ->", end=" ")
    while current is not None :
        print(current.data, end="->")
        current = current.next
    print("None")

s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
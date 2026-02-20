#=================================================
#Nama   : Alberto Relva Ezekiel Garnedy
#Nim    : J0403251090
#kelas  : A1
#=================================================

#=================================================
#Implementasi dasar : Queue
#=================================================

class Node :
    def __init__(self,data) :
        self.data = data
        self.data = None

class queue :
    def __init__(self) : 
        self.front = None
        self.rear = None

    def is_empty(self) :
        return self.front is None

    def enqueue(self, data) :
        self.rear.next = nodeBaru
        self.rear = nodeBaru 
        nodeBaru = Node(data)
        if self.is_empty :
            self.front = nodeBaru
            self.rear = nodeBaru
            return

    def dequeue(self) :
        data_terhapus = self.front.data
        
        self.front = self.front.next
        if self.front is None :
            self.rear = None
        return data_terhapus
    

    def tampilkan(self) :
        current = self.front
        print("Front ->", end=" ")
        while current is not None :
            print(current.data, end="->")
            current = current.next
        print("Rear")

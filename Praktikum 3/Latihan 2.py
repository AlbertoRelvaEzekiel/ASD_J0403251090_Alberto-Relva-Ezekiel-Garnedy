class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def _init_(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def cari(self, nilai):
        if self.head is None:
            print("List kosong.")
            return

        current = self.head
        posisi = 0

        while True:
            if current.data == nilai:
                print(f"Nilai ditemukan pada posisi ke-{posisi}")
                return

            current = current.next
            posisi += 1

            if current == self.head:
                break

        print("Nilai tidak ditemukan.")


# Contoh penggunaan
cll = CircularLinkedList()
cll.tambah(5)
cll.tambah(10)
cll.tambah(15)

cll.cari(10)
cll.cari(20)
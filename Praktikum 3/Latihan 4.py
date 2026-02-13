class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def _init_(self):
        self.head = None

    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def tampilkan(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def gabungkan(self, list_lain):
        list_baru = SingleLinkedList()

        # Salin list pertama
        current = self.head
        while current:
            list_baru.tambah_di_akhir(current.data)
            current = current.next

        # Salin list kedua
        current = list_lain.head
        while current:
            list_baru.tambah_di_akhir(current.data)
            current = current.next

        return list_baru


# Contoh penggunaan
list1 = SingleLinkedList()
list1.tambah_di_akhir(1)
list1.tambah_di_akhir(2)

list2 = SingleLinkedList()
list2.tambah_di_akhir(3)
list2.tambah_di_akhir(4)

hasil = list1.gabungkan(list2)
hasil.tampilkan()
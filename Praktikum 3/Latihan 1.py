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

    def hapus_nilai(self, nilai):
        if self.head is None:
            print("List kosong.")
            return

        # Jika node yang ingin dihapus adalah head
        if self.head.data == nilai:
            self.head = self.head.next
            print(f"Node dengan nilai {nilai} berhasil dihapus.")
            return

        current = self.head
        previous = None

        while current and current.data != nilai:
            previous = current
            current = current.next

        if current is None:
            print(f"Nilai {nilai} tidak ditemukan.")
            return

        previous.next = current.next
        print(f"Node dengan nilai {nilai} berhasil dihapus.")

    def tampilkan(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Contoh penggunaan
sll = SingleLinkedList()
sll.tambah_di_akhir(10)
sll.tambah_di_akhir(20)
sll.tambah_di_akhir(30)

sll.tampilkan()
sll.hapus_nilai(20)
sll.tampilkan()
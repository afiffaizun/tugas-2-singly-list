# ===============================
# CLASS NODE
# ===============================
class Node:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.next = None


# ===============================
# CLASS LINKED LIST
# ===============================
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0


    # INSERT DI AWAL
    def insert_beginning(self, nim, nama):
        new_node = Node(nim, nama)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        print("Data berhasil ditambahkan di awal.")


    # INSERT DI POSISI TERTENTU
    def insert_position(self, nim, nama, pos):

        if pos < 1 or pos > self.count + 1:
            print("Posisi tidak valid!")
            return

        if pos == 1:
            self.insert_beginning(nim, nama)
            return

        new_node = Node(nim, nama)
        temp = self.head

        for i in range(1, pos - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        self.count += 1

        print(f"Data berhasil ditambahkan di posisi {pos}.")


    # INSERT DI AKHIR
    def insert_end(self, nim, nama):

        new_node = Node(nim, nama)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        self.count += 1
        print("Data berhasil ditambahkan di akhir.")


    # DELETE AWAL
    def delete_beginning(self):

        if self.head is None:
            print("Linked List kosong!")
            return

        self.head = self.head.next
        self.count -= 1
        print("Data pertama berhasil dihapus.")


    # DELETE POSISI
    def delete_position(self, pos):

        if self.head is None:
            print("Linked List kosong!")
            return

        if pos < 1 or pos > self.count:
            print("Posisi tidak valid!")
            return

        if pos == 1:
            self.delete_beginning()
            return

        temp = self.head

        for i in range(1, pos - 1):
            temp = temp.next

        temp.next = temp.next.next
        self.count -= 1

        print(f"Data pada posisi {pos} berhasil dihapus.")


    # DELETE AKHIR
    def delete_end(self):

        if self.head is None:
            print("Linked List kosong!")
            return

        if self.head.next is None:
            self.head = None
        else:
            temp = self.head

            while temp.next.next:
                temp = temp.next

            temp.next = None

        self.count -= 1
        print("Data terakhir berhasil dihapus.")


    # DELETE BERDASARKAN NIM
    def delete_by_nim(self, nim):

        if self.head is None:
            print("Linked List kosong!")
            return

        temp = self.head

        if temp.nim == nim:
            self.head = temp.next
            self.count -= 1
            print("Data berhasil dihapus.")
            return

        prev = None

        while temp and temp.nim != nim:
            prev = temp
            temp = temp.next

        if temp is None:
            print("NIM tidak ditemukan.")
            return

        prev.next = temp.next
        self.count -= 1
        print("Data berhasil dihapus.")


    # MENAMPILKAN DATA
    def show(self):

        if self.head is None:
            print("\nLinked List kosong!\n")
            return

        print("\n===================================")
        print("        DATA MAHASISWA")
        print("===================================")
        print("{:<5} {:<12} {:<20}".format("No", "NIM", "Nama"))
        print("-----------------------------------")

        temp = self.head
        no = 1

        while temp:
            print("{:<5} {:<12} {:<20}".format(no, temp.nim, temp.nama))
            temp = temp.next
            no += 1

        print("-----------------------------------")
        print("Total Data :", self.count)
        print("===================================\n")


# ===============================
# MENU PROGRAM
# ===============================
def main():

    ll = LinkedList()

    while True:

        print("\n========== MENU ==========")
        print("1. Insert at Beginning")
        print("2. Insert at Given Position")
        print("3. Insert at End")
        print("4. Delete from Beginning")
        print("5. Delete Given Position")
        print("6. Delete from End")
        print("7. Delete First Occurrence (by NIM)")
        print("8. Show Data")
        print("9. Exit")
        print("==========================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim = input("Masukkan NIM  : ")
            nama = input("Masukkan Nama : ")
            ll.insert_beginning(nim, nama)

        elif pilihan == "2":
            nim = input("Masukkan NIM  : ")
            nama = input("Masukkan Nama : ")
            pos = int(input("Masukkan Posisi : "))
            ll.insert_position(nim, nama, pos)

        elif pilihan == "3":
            nim = input("Masukkan NIM  : ")
            nama = input("Masukkan Nama : ")
            ll.insert_end(nim, nama)

        elif pilihan == "4":
            ll.delete_beginning()

        elif pilihan == "5":
            pos = int(input("Masukkan Posisi yang akan dihapus : "))
            ll.delete_position(pos)

        elif pilihan == "6":
            ll.delete_end()

        elif pilihan == "7":
            nim = input("Masukkan NIM yang akan dihapus : ")
            ll.delete_by_nim(nim)

        elif pilihan == "8":
            ll.show()

        elif pilihan == "9":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


# ===============================
# PROGRAM DIJALANKAN
# ===============================
if __name__ == "__main__":
    main()
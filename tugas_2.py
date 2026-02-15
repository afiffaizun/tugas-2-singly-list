class Node:
    def __init__(self, nim, nama):
        self.nim = nim        # menyimpan NIM mahasiswa
        self.nama = nama      # menyimpan nama mahasiswa
        self.next = None      # pointer ke node berikutnya (awalnya None)


# Class LinkedList untuk mengatur seluruh operasi
class LinkedList:
    def __init__(self):
        self.head = None      # head menunjuk node pertama
        self.count = 0        # menghitung jumlah data dalam list

    # 1. INSERT AT BEGINNING
    def insert_beginning(self, nim, nama):
        new_node = Node(nim, nama)   # membuat node baru

        new_node.next = self.head    # node baru menunjuk ke head lama
        self.head = new_node         # head dipindahkan ke node baru

        self.count += 1              # setiap insert → count bertambah 1


    # 2. INSERT AT GIVEN POSITION
    def insert_position(self, nim, nama, pos):

        # jika posisi 1, sama seperti insert di depan
        if pos == 1:
            self.insert_beginning(nim, nama)
            return

        new_node = Node(nim, nama)   # membuat node baru
        current = self.head          # mulai dari head

        # bergerak sampai node sebelum posisi yang diinginkan
        for i in range(pos - 2):
            current = current.next

        new_node.next = current.next  # node baru menunjuk ke node setelahnya
        current.next = new_node       # node sebelumnya menunjuk ke node baru

        self.count += 1               # count bertambah

    # 3. INSERT AT END
    def insert_end(self, nim, nama):
        new_node = Node(nim, nama)   # membuat node baru

        # jika list kosong
        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            # bergerak sampai node terakhir
            while current.next:
                current = current.next

            current.next = new_node   # node terakhir menunjuk ke node baru

        self.count += 1               # count bertambah


    # 4. DELETE FROM BEGINNING
    def delete_beginning(self):

        if self.head:                 # jika list tidak kosong
            self.head = self.head.next  # head dipindahkan ke node kedua
            self.count -= 1           # count berkurang



    # 5. DELETE GIVEN POSITION
    def delete_position(self, pos):

        # jika hapus posisi pertama
        if pos == 1:
            self.delete_beginning()
            return

        current = self.head

        # bergerak ke node sebelum posisi yang akan dihapus
        for i in range(pos - 2):
            current = current.next

        # loncati node yang akan dihapus
        current.next = current.next.next

        self.count -= 1               # count berkurang


    # 6. DELETE FROM END
    def delete_end(self):

        if self.head is None:         # jika kosong
            return

        # jika hanya 1 node
        if self.head.next is None:
            self.head = None
        else:
            current = self.head

            # bergerak ke node sebelum terakhir
            while current.next.next:
                current = current.next

            current.next = None       # hapus node terakhir

        self.count -= 1               # count berkurang

    # 7. DELETE FIRST OCCURRENCE (BY NIM)
    def delete_by_nim(self, nim):

        if self.head is None:
            return

        # jika data yang dihapus ada di head
        if self.head.nim == nim:
            self.head = self.head.next
            self.count -= 1
            return

        current = self.head

        # mencari NIM yang cocok
        while current.next:
            if current.next.nim == nim:
                current.next = current.next.next  # lewati node tersebut
                self.count -= 1
                return
            current = current.next


    # 8. SHOW DATA
    def show(self):

        current = self.head           # mulai dari head

        print("\n===== DATA MAHASISWA =====")

        while current:                # selama belum None
            print("NIM:", current.nim, "| Nama:", current.nama)
            current = current.next    # pindah ke node berikutnya

        print("Total Data:", self.count)



# MENU PROGRAM (SWITCH CASE)
def main():

    data = LinkedList()   # membuat objek LinkedList

    while True:

        print("\n===== MENU =====")
        print("1. Insert at Beginning")
        print("2. Insert at Given Position")
        print("3. Insert at End")
        print("4. Delete from Beginning")
        print("5. Delete Given Position")
        print("6. Delete from End")
        print("7. Delete First Occurrence (by NIM)")
        print("8. Show Data")
        print("9. Exit")

        pilihan = int(input("Pilih menu: "))

        # menggunakan match-case sebagai switch
        match pilihan:

            case 1:
                nim = input("NIM  : ")
                nama = input("Nama : ")
                data.insert_beginning(nim, nama)

            case 2:
                nim = input("NIM  : ")
                nama = input("Nama : ")
                pos = int(input("Posisi: "))
                data.insert_position(nim, nama, pos)

            case 3:
                nim = input("NIM  : ")
                nama = input("Nama : ")
                data.insert_end(nim, nama)

            case 4:
                data.delete_beginning()

            case 5:
                pos = int(input("Posisi: "))
                data.delete_position(pos)
            case 6:
                data.delete_end()

            case 7:
                nim = input("NIM yang dihapus: ")
                data.delete_by_nim(nim)

            case 8:
                data.show()
            case 9:
                print("Program selesai.")
                break

            case _:
                print("Menu tidak tersedia.")


# menjalankan program
if __name__ == "__main__":
    main()

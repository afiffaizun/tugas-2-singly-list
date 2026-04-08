class Node:
    def __init__(self, nim, nama):
        self.nim = nim      
        self.nama = nama   
        self.next = None    # pointer ke node berikutnya 


class LinkedList:
    def __init__(self):
        self.head = None    # head menunjuk node pertama
        self.count = 0      

    
    def insert_beginning(self, nim, nama):
        new_node = Node(nim, nama)   # buat node baru
        new_node.next = self.head    # node baru menunjuk ke head lama
        self.head = new_node         # node baru jadikan head
        self.count += 1              # jumlah data bertambah
        print("Data berhasil ditambahkan di awal.")

    
    def insert_position(self, nim, nama, pos):

        if pos < 1 or pos > self.count + 1:
            print("Posisi tidak valid!")
            return

        # jika posisi pertama, gunakan insert_beginning
        if pos == 1:
            self.insert_beginning(nim, nama)
            return

        new_node = Node(nim, nama)
        current = self.head

        # bergerak ke node sebelum posisi yang diinginkan
        for _ in range(pos - 2):
            current = current.next

        # sambungkan node baru
        new_node.next = current.next
        current.next = new_node

        self.count += 1
        print(f"Data berhasil ditambahkan di posisi {pos}.")


    def insert_end(self, nim, nama):
        new_node = Node(nim, nama)

        # jika list kosong
        if self.head is None:
            self.head = new_node

        else:
            current = self.head

            # bergerak sampai node terakhir
            while current.next:
                current = current.next

            current.next = new_node

        self.count += 1
        print("Data berhasil ditambahkan di akhir.")


    def delete_beginning(self):

        # jika kosong
        if self.head is None:
            print("List kosong!")
            return

        self.head = self.head.next   # head pindah ke node kedua
        self.count -= 1
        print("Data awal berhasil dihapus.")


    def delete_position(self, pos):

        # cek posisi valid
        if pos < 1 or pos > self.count:
            print("Posisi tidak valid!")
            return

        if pos == 1:
            self.delete_beginning()
            return

        current = self.head

        # bergerak ke node sebelum yang dihapus
        for _ in range(pos - 2):
            current = current.next

        # lewati node yang dihapus
        current.next = current.next.next

        self.count -= 1
        print(f"Data posisi {pos} berhasil dihapus.")


    def delete_end(self):

        if self.head is None:
            print("List kosong!")
            return

        if self.head.next is None:
            self.head = None

        else:
            current = self.head

            # cari node sebelum terakhir
            while current.next.next:
                current = current.next #geser pointer ke node selanjutnya

            current.next = None #node pada ini hilang, tidak terhubung

        self.count -= 1
        print("Data terakhir berhasil dihapus.")


    def delete_by_nim(self, nim):

        if self.head is None:
            print("List kosong!")
            return

        # jika data ada di head
        if self.head.nim == nim:
            self.head = self.head.next
            self.count -= 1
            print(f"Data dengan NIM {nim} berhasil dihapus.")
            return

        current = self.head

        # cari NIM yang sesuai
        while current.next:
            if current.next.nim == nim:
                current.next = current.next.next
                self.count -= 1
                print(f"Data dengan NIM {nim} berhasil dihapus.")
                return
            current = current.next

        print("NIM tidak ditemukan!")


    def show(self):

        if self.head is None:
            print("\nData masih kosong.")
            return

        print("\n" + "=" * 50)
        print("              DATA MAHASISWA")
        print("=" * 50)
        print("{:<5} {:<15} {:<20}".format("No", "NIM", "Nama"))
        print("-" * 50)

        current = self.head
        no = 1

        # tampilkan semua node
        while current:
            print("{:<5} {:<15} {:<20}".format(no, current.nim, current.nama))
            current = current.next
            no += 1

        print("-" * 50)
        print("Total Data :", self.count)
        print("=" * 50)



def main():

    data = LinkedList()

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
            data.insert_beginning(nim, nama)

        elif pilihan == "2":
            nim = input("Masukkan NIM  : ")
            nama = input("Masukkan Nama : ")
            pos = int(input(f"Masukkan Posisi ( 1 - {data.count + 1} ): "))
            data.insert_position(nim, nama, pos)

        elif pilihan == "3":
            nim = input("Masukkan NIM  : ")
            nama = input("Masukkan Nama : ")
            data.insert_end(nim, nama)

        elif pilihan == "4":
            data.delete_beginning()

        elif pilihan == "5":
            pos = int(input("Masukkan Posisi yang akan dihapus : "))
            data.delete_position(pos)

        elif pilihan == "6":
            data.delete_end()

        elif pilihan == "7":
            nim = input("Masukkan NIM yang akan dihapus : ")
            data.delete_by_nim(nim)

        elif pilihan == "8":
            data.show()

        elif pilihan == "9":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
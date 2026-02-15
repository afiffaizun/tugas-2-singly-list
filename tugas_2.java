import java.util.Scanner;

// ===============================
// CLASS NODE (Menyimpan 1 data mahasiswa)
// ===============================
class Node {
    String nim;
    String nama;
    Node next;

    // Constructor
    Node(String nim, String nama) {
        this.nim = nim;
        this.nama = nama;
        this.next = null;
    }
}


// ===============================
// CLASS LINKED LIST
// ===============================
class LinkedList {

    Node head;     // menunjuk node pertama
    int count;     // menghitung jumlah data

    // Constructor
    LinkedList() {
        head = null;
        count = 0;
    }

    // ===============================
    // 1. INSERT DI AWAL
    // ===============================
    void insertBeginning(String nim, String nama) {
        Node newNode = new Node(nim, nama);
        newNode.next = head;
        head = newNode;
        count++;
        System.out.println("Data berhasil ditambahkan di awal.");
    }

    // ===============================
    // 2. INSERT DI POSISI TERTENTU
    // ===============================
    void insertPosition(String nim, String nama, int pos) {

        if (pos < 1 || pos > count + 1) {
            System.out.println("Posisi tidak valid!");
            return;
        }

        if (pos == 1) {
            insertBeginning(nim, nama);
            return;
        }

        Node newNode = new Node(nim, nama);
        Node current = head;

        for (int i = 0; i < pos - 2; i++) {
            current = current.next;
        }

        newNode.next = current.next;
        current.next = newNode;

        count++;
        System.out.println("Data berhasil ditambahkan di posisi " + pos);
    }

    // ===============================
    // 3. INSERT DI AKHIR
    // ===============================
    void insertEnd(String nim, String nama) {

        Node newNode = new Node(nim, nama);

        if (head == null) {
            head = newNode;
        } else {
            Node current = head;

            while (current.next != null) {
                current = current.next;
            }

            current.next = newNode;
        }

        count++;
        System.out.println("Data berhasil ditambahkan di akhir.");
    }

    // ===============================
    // 4. DELETE DI AWAL
    // ===============================
    void deleteBeginning() {

        if (head == null) {
            System.out.println("List kosong!");
            return;
        }

        head = head.next;
        count--;
        System.out.println("Data awal berhasil dihapus.");
    }

    // ===============================
    // 5. DELETE DI POSISI TERTENTU
    // ===============================
    void deletePosition(int pos) {

        if (pos < 1 || pos > count) {
            System.out.println("Posisi tidak valid!");
            return;
        }

        if (pos == 1) {
            deleteBeginning();
            return;
        }

        Node current = head;

        for (int i = 0; i < pos - 2; i++) {
            current = current.next;
        }

        current.next = current.next.next;
        count--;
        System.out.println("Data posisi " + pos + " berhasil dihapus.");
    }

    // ===============================
    // 6. DELETE DI AKHIR
    // ===============================
    void deleteEnd() {

        if (head == null) {
            System.out.println("List kosong!");
            return;
        }

        if (head.next == null) {
            head = null;
        } else {
            Node current = head;

            while (current.next.next != null) {
                current = current.next;
            }

            current.next = null;
        }

        count--;
        System.out.println("Data terakhir berhasil dihapus.");
    }

    // ===============================
    // 7. DELETE BERDASARKAN NIM
    // ===============================
    void deleteByNim(String nim) {

        if (head == null) {
            System.out.println("List kosong!");
            return;
        }

        if (head.nim.equals(nim)) {
            head = head.next;
            count--;
            System.out.println("Data dengan NIM " + nim + " berhasil dihapus.");
            return;
        }

        Node current = head;

        while (current.next != null) {
            if (current.next.nim.equals(nim)) {
                current.next = current.next.next;
                count--;
                System.out.println("Data dengan NIM " + nim + " berhasil dihapus.");
                return;
            }
            current = current.next;
        }

        System.out.println("NIM tidak ditemukan!");
    }

    // ===============================
    // 8. MENAMPILKAN DATA
    // ===============================
    void show() {

        if (head == null) {
            System.out.println("\nData masih kosong.");
            return;
        }

        System.out.println("\n=================================================");
        System.out.println("               DATA MAHASISWA");
        System.out.println("=================================================");
        System.out.printf("%-5s %-15s %-20s\n", "No", "NIM", "Nama");
        System.out.println("-------------------------------------------------");

        Node current = head;
        int no = 1;

        while (current != null) {
            System.out.printf("%-5d %-15s %-20s\n", no, current.nim, current.nama);
            current = current.next;
            no++;
        }

        System.out.println("-------------------------------------------------");
        System.out.println("Total Data : " + count);
        System.out.println("=================================================");
    }
}


// ===============================
// CLASS MAIN (Program Menu)
// ===============================
public class tugas_2 {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        LinkedList data = new LinkedList();

        while (true) {

            System.out.println("\n===== MENU =====");
            System.out.println("1. Insert at Beginning");
            System.out.println("2. Insert at Given Position");
            System.out.println("3. Insert at End");
            System.out.println("4. Delete from Beginning");
            System.out.println("5. Delete Given Position");
            System.out.println("6. Delete from End");
            System.out.println("7. Delete First Occurrence (by NIM)");
            System.out.println("8. Show Data");
            System.out.println("9. Exit");

            System.out.print("Pilih Opsi: ");
            int pilihan = input.nextInt();
            input.nextLine(); // membersihkan newline

            switch (pilihan) {

                case 1:
                    System.out.print("Masukan NIM  : ");
                    String nim1 = input.nextLine();
                    System.out.print("Masukan Nama : ");
                    String nama1 = input.nextLine();
                    data.insertBeginning(nim1, nama1);
                    break;

                case 2:
                    System.out.print("Masukan NIM  : ");
                    String nim2 = input.nextLine();
                    System.out.print("Masukan Nama : ");
                    String nama2 = input.nextLine();
                    System.out.print("Posisi: ");
                    int posInsert = input.nextInt();
                    input.nextLine();
                    data.insertPosition(nim2, nama2, posInsert);
                    break;

                case 3:
                    System.out.print("Masukan NIM  : ");
                    String nim3 = input.nextLine();
                    System.out.print("Masukan Nama : ");
                    String nama3 = input.nextLine();
                    data.insertEnd(nim3, nama3);
                    break;

                case 4:
                    data.deleteBeginning();
                    break;

                case 5:
                    System.out.print("Posisi: ");
                    int posDelete = input.nextInt();
                    input.nextLine();
                    data.deletePosition(posDelete);
                    break;

                case 6:
                    data.deleteEnd();
                    break;

                case 7:
                    System.out.print("NIM yang dihapus: ");
                    String nimDelete = input.nextLine();
                    data.deleteByNim(nimDelete);
                    break;

                case 8:
                    data.show();
                    break;

                case 9:
                    System.out.println("Program selesai.");
                    return;

                default:
                    System.out.println("Menu tidak tersedia.");
            }
        }
    }
}

import java.util.Scanner;

class Node {
    String nim;
    String nama;
    Node next;

    Node(String nim, String nama) {
        this.nim = nim;
        this.nama = nama;
        this.next = null;
    }
}

public class tugas_2 {

    static Node head = null;
    static int count = 0;

    // 1. Insert at Beginning
    static void insertBeginning(String nim, String nama) {
        Node newNode = new Node(nim, nama);
        newNode.next = head;
        head = newNode;
        count++;
    }

    // 2. Insert at Given Position
    static void insertPosition(String nim, String nama, int pos) {
        if (pos == 1) {
            insertBeginning(nim, nama);
            return;
        }

        Node newNode = new Node(nim, nama);
        Node current = head;

        for (int i = 1; i < pos - 1; i++) {
            current = current.next;
        }

        newNode.next = current.next;
        current.next = newNode;
        count++;
    }

    // 3. Insert at End
    static void insertEnd(String nim, String nama) {
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
    }

    // 4. Delete from Beginning
    static void deleteBeginning() {
        if (head != null) {
            head = head.next;
            count--;
        }
    }

    // 5. Delete Given Position
    static void deletePosition(int pos) {
        if (pos == 1) {
            deleteBeginning();
            return;
        }

        Node current = head;

        for (int i = 1; i < pos - 1; i++) {
            current = current.next;
        }

        current.next = current.next.next;
        count--;
    }

    // 6. Delete from End
    static void deleteEnd() {
        if (head == null) return;

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
    }

    // 7. Delete First Occurrence by NIM
    static void deleteByNim(String nim) {
        if (head == null) return;

        if (head.nim.equals(nim)) {
            head = head.next;
            count--;
            return;
        }

        Node current = head;

        while (current.next != null) {
            if (current.next.nim.equals(nim)) {
                current.next = current.next.next;
                count--;
                return;
            }
            current = current.next;
        }
    }

    // 8. Show Data
    static void showData() {
        Node current = head;
        int no = 1;

        System.out.println("\nData Mahasiswa:");
        while (current != null) {
            System.out.println(no + ". " + current.nim + " - " + current.nama);
            current = current.next;
            no++;
        }

        System.out.println("Total data: " + count);
    }

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int pilih;

        do {
            System.out.println("\n===== MENU =====");
            System.out.println("1. Insert Beginning");
            System.out.println("2. Insert Position");
            System.out.println("3. Insert End");
            System.out.println("4. Delete Beginning");
            System.out.println("5. Delete Position");
            System.out.println("6. Delete End");
            System.out.println("7. Delete by NIM");
            System.out.println("8. Show Data");
            System.out.println("9. Exit");

            System.out.print("Pilih: ");
            pilih = input.nextInt();
            input.nextLine();

            switch (pilih) {

                case 1:
                    System.out.print("NIM: ");
                    String nim1 = input.nextLine();
                    System.out.print("Nama: ");
                    String nama1 = input.nextLine();
                    insertBeginning(nim1, nama1);
                    break;

                case 2:
                    System.out.print("NIM: ");
                    String nim2 = input.nextLine();
                    System.out.print("Nama: ");
                    String nama2 = input.nextLine();
                    System.out.print("Posisi: ");
                    int pos2 = input.nextInt();
                    insertPosition(nim2, nama2, pos2);
                    break;

                case 3:
                    System.out.print("NIM: ");
                    String nim3 = input.nextLine();
                    System.out.print("Nama: ");
                    String nama3 = input.nextLine();
                    insertEnd(nim3, nama3);
                    break;

                case 4:
                    deleteBeginning();
                    break;

                case 5:
                    System.out.print("Posisi: ");
                    int pos5 = input.nextInt();
                    deletePosition(pos5);
                    break;

                case 6:
                    deleteEnd();
                    break;

                case 7:
                    System.out.print("NIM yang dihapus: ");
                    String nim7 = input.nextLine();
                    deleteByNim(nim7);
                    break;

                case 8:
                    showData();
                    break;

                case 9:
                    System.out.println("Program selesai.");
                    break;

                default:
                    System.out.println("Menu tidak ada.");
            }

        } while (pilih != 9);

        input.close();
    }
}

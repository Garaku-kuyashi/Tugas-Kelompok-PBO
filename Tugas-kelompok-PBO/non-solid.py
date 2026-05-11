import json

class Hewan:

    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis


    def makan(self):

        if self.jenis == "singa":
            print("Makan daging")

        elif self.jenis == "kambing":
            print("Makan rumput")

        elif self.jenis == "elang":
            print("Makan ikan")

        else:
            print("Makan apa saja")


    def suara(self):

        if self.jenis == "singa":
            print("AUMMMM")

        elif self.jenis == "kucing":
            print("Meong")

        elif self.jenis == "anjing":
            print("Guk guk")

        else:
            print("Suara tidak diketahui")


    def terbang(self):

        if self.jenis == "elang":
            print("Elang terbang tinggi")

        elif self.jenis == "burung":
            print("Burung terbang")

        else:
            raise Exception(f"{self.jenis} tidak bisa terbang")

    def berenang(self):

        if self.jenis == "ikan":
            print("Ikan berenang")

        elif self.jenis == "buaya":
            print("Buaya berenang")

        else:
            raise Exception(f"{self.jenis} tidak bisa berenang")

    def simpan_ke_file(self):

        data = {
            "nama": self.nama,
            "jenis": self.jenis
        }

        with open("hewan.json", "w") as file:
            json.dump(data, file)

        print("Data hewan disimpan")

    def cetak_laporan(self):

        print("\n=== LAPORAN HEWAN ===")
        print("Nama :", self.nama)
        print("Jenis:", self.jenis)

    def connect_server(self):

        print("Menghubungkan data hewan ke server...")

    def edit_video_hewan(self):
        print("Mengedit video hewan")

    def mining_crypto(self):
        print("Mining crypto dengan data hewan")


class Ikan(Hewan):

    def __init__(self, nama):
        super().__init__(nama, "ikan")

    def terbang(self):
        raise Exception("IKAN TIDAK BISA TERBANG")

class Burung(Hewan):

    def __init__(self, nama):
        super().__init__(nama, "burung")

class MySQLHewan:

    def simpan_mysql(self):
        print("Simpan data hewan ke MySQL")

class HewanService:
    def __init__(self):
        self.database = MySQLHewan()

    def simpan(self):
        self.database.simpan_mysql()

burung = Burung("Elang")
burung.makan()
burung.suara()
burung.terbang()
print()
ikan = Ikan("Nemo")
ikan.makan()
ikan.berenang()
ikan.terbang()
print()
service = HewanService()
service.simpan()

# kesalahan pada kode ini adalah class Hewan memiliki banyak tanggung jawab, seperti menyimpan data ke file, mencetak laporan, menghubungkan ke server, mengedit video, dan mining crypto. Hal ini melanggar prinsip Single Responsibility Principle (SRP) karena class tersebut memiliki lebih dari satu alasan untuk berubah. Selain itu, class Hewan juga bergantung pada implementasi konkret MySQLHewan, yang melanggar prinsip Dependency Inversion Principle (DIP).

# pelanggaran pada ocp adalah jika kita lihat method makan, suara, terbang, dan berenang semuanya menggunaan if-else untuk menentukan perilaku berdasarkan jenis hewan. Jika kita ingin menambahkan jenis hewan baru, kita harus mengubah kode pada method tersebut, yang melanggar prinsip Open/Closed Principle (OCP) karena kode tidak terbuka untuk ekstensi tetapi tertutup untuk modifikasi.

# pelanggaran pada lsp adalah jika kita lihat class Ikan yang mewarisi class Hewan, namun method terbang pada class Ikan tidak bisa diimplementasikan karena ikan tidak bisa terbang. Hal ini melanggar prinsip Liskov Substitution Principle (LSP) karena objek dari class Ikan tidak dapat menggantikan objek dari class Hewan tanpa mengubah perilaku yang diharapkan.
# pelanggaran pada isp adalah jika kita lihat class Hewan memiliki banyak method yang tidak semua hewan bisa lakukan, seperti terbang dan berenang. Hal ini melanggar prinsip Interface Segregation Principle (ISP) karena class tersebut memaksa implementasi method yang tidak relevan untuk semua jenis hewan.

# pelanggaran pada dip adalah jika kita lihat class HewanService bergantung pada implementasi konkret MySQLHewan, yang membuatnya sulit untuk mengganti database dengan implementasi lain tanpa mengubah kode pada class HewanService. Hal ini melanggar prinsip Dependency Inversion Principle (DIP) karena class tersebut bergantung pada detail implementasi daripada abstraksi.
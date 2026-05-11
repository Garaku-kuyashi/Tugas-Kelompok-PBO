from abc import ABC, abstractmethod
import json


# =========================================================
# S = SINGLE RESPONSIBILITY PRINCIPLE
# =========================================================
# Class Hewan hanya mengurus data dan perilaku hewan


# =========================================================
# ABSTRACT CLASS
# =========================================================
class Hewan(ABC):

    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def suara(self):
        pass

    @abstractmethod
    def makan(self):
        pass

# ISP = hanya hewan tertentu yang bisa terbang
class BisaTerbang(ABC):

    @abstractmethod
    def terbang(self):
        pass

class BisaBerenang(ABC):

    @abstractmethod
    def berenang(self):
        pass


# OCP = bisa tambah hewan baru tanpa ubah class lama
class Burung(Hewan, BisaTerbang):

    def suara(self):
        print("Cuit cuit")

    def makan(self):
        print("Burung makan biji-bijian")

    def terbang(self):
        print("Burung terbang di langit")

class Ikan(Hewan, BisaBerenang):

    def suara(self):
        print("Ikan tidak bersuara")

    def makan(self):
        print("Ikan makan pelet")

    def berenang(self):
        print("Ikan berenang di air")

class Kucing(Hewan):

    def suara(self):
        print("Meong")

    def makan(self):
        print("Kucing makan ikan")

# SRP = khusus simpan data

class FileHewan:

    def simpan(self, hewan):

        data = {
            "nama": hewan.nama,
            "jenis": hewan.__class__.__name__
        }

        with open("hewan.json", "w") as file:
            json.dump(data, file)

        print("Data hewan disimpan")


# DIP = abstraction database
class Database(ABC):

    @abstractmethod
    def simpan(self, hewan):
        pass

class MySQLDatabase(Database):

    def simpan(self, hewan):
        print(f"Data {hewan.nama} disimpan ke MySQL")

class MongoDatabase(Database):

    def simpan(self, hewan):
        print(f"Data {hewan.nama} disimpan ke MongoDB")

# DIP = bergantung pada abstraction, bukan class konkret
class HewanService:

    def __init__(self, database):
        self.database = database

    def simpan_hewan(self, hewan):
        self.database.simpan(hewan)


# MAIN PROGRAM
burung = Burung("Elang")

burung.suara()
burung.makan()
burung.terbang()

print()

ikan = Ikan("Nemo")

ikan.suara()
ikan.makan()
ikan.berenang()

print()

kucing = Kucing("Oyen")

kucing.suara()
kucing.makan()

print()

# simpan file
file_hewan = FileHewan()
file_hewan.simpan(kucing)

print()

# simpan database
mysql = MySQLDatabase()

service = HewanService(mysql)
service.simpan_hewan(burung)
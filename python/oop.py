# oop = object oriented programming
# oop = semuanya ialah object

# object punya properties -> manusia propertis spt name, tanggal lahir, asal
# object punta kemampuan => manusia bisa bicara, jalan, makanm, minum

class Mahasiswa:
    # init fungsi yang pertama kali dipanggil saat menciptakan object mahasiswa
    # self ialah parameter yang wajib ada bila ada fungsi di dalam class
    def __init__(self, nama_depan, nama_belakang, jurusan, tanggal_lahir, terdaftar):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.jurusan = jurusan
        self.tanggal_lahir = tanggal_lahir
        self.terdaftar = terdaftar

    # fungsi untuk mereprentasikan object string
    def __str__(self):
        return self.nama_depan + " " + self.nama_belakang
    
    def register(self):
        if self.terdaftar:
            print("sudah terdaftar")
        self.terdaftar = True
        print("pendaftaran berhasil")

budi = Mahasiswa(nama_depan="Budi", nama_belakang="Anwar", jurusan="Politik", terdaftar=False, tanggal_lahir="1999-02-14")

danu = Mahasiswa(nama_depan="danu", nama_belakang="wijaya", jurusan="informatika", terdaftar=True, tanggal_lahir="1986-10-01")

print(budi)
print(danu)

print(budi.terdaftar)
budi.register()

print(budi.nama_depan)


if budi.terdaftar:
    print("yes")
else:
    print("belum terdaftar")
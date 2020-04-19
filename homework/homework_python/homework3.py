# function untuk mengkalkulasi besarnya bayaran bulanan
# tanya user harga yang mau dibeli
# tanya user berapa lama mau melunasi

def cicilan():       
    harga = int(input("Masukan jumlah harga (contoh = 300000) : "))
    tenor = int(input("Masukan berapa bulan tenor pelunasan (contoh = 12): "))

    total = harga / tenor
    return round(total, 2)

hitung_cicilan = cicilan()
print("Jumlah cicilan anda perbulan adalah {angsuran} rupiah".format(angsuran = hitung_cicilan))
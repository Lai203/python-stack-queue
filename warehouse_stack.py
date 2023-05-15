stack = []

def tambah_barang (stack, barang_baru) :
    stack.append(barang_baru)
    print (f"{barang_baru} berhasil ditambahkan ke dalam stack.")

def hapus_barang_terakhir(stack) :
    if len(stack) == 0 :
        print ("Stack Kosong, Tidak Ada Barang Yang Dapat Dihapus.")
    else :
        barang_terakhir = stack.pop()
        print (f"{barang_terakhir} berhasil dihapus dari stack.")

def tampilkan_barang_teratas(stack):
    if len(stack) == 0 :
        print ("Stack Kosong, Tidak Ada Barang Yang Dapat Ditampilkan.")
    else :
        barang_teratas = stack[-1]
        print (f"Barang Teratas Di Dalam Stack Adalah {barang_teratas}.")

while True:
    print ("\nGudang Saat Ini : ", stack)
    print ("Menu : ")
    print ("1. Tambah Barang")
    print ("2. Hapus Barang Terakhir")
    print ("3. Tampilkan Barang Teratas")
    print ("4. Keluar")

    pilihan = input ("Masukkan Pilihan Anda (1/2/3/4) : ")

    if pilihan == "1" :
        barang_baru = input ("Masukkan Nama Barang Yang Akan Ditambahkan : ")
        tambah_barang(stack, barang_baru)
    elif pilihan == "2" :
        hapus_barang_terakhir(stack)
    elif pilihan == "3" :
        tampilkan_barang_teratas(stack)
    elif pilihan == "4" : 
        print ("Terima Kasih Telah Menggunakan Program Ini.")
        break
    else :
        print ("Pilihan Tidak Valid. Silahkan Masukkan Pilihan Yang Benar.")

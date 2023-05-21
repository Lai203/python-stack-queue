#Buatlah program untuk mengelola antrean transaksi pelanggan yang 
#berisi informasi nama pelanggan dan jenis transaksi. Program harus
#memungkinkan pelanggan untuk menambahkan transaksi ke dalam antrian
#dan menampilkan transaksi berikutnya yang akan dilayani. Program juga
#harus dapat menghapus transaksi yang telah dilayani

import time
from collections import deque
 
antrian = deque()

def tambah_queue (transaksi, nama) :
    antrian.append(nama)
    antrian.append(transaksi)

while True : 
    print ("Transaksi Sekarang : " )
    print (antrian)
    print ("Pilihan : ")
    print ("1. Tambah Antrian Transaksi")
    print ("2. Lihat Transaksi Selanjutnya")
    print ("3. Hapus Antrian")
    print ("4. Keluar")
    pilihan = int(input ("Pilih (1/2/3/4) : "))
    if pilihan == 1 :
        nama = input ("Nama : ")
        transaksi = input ("Transaksi : ")
        tambah_queue(transaksi, nama)
    elif pilihan == 2 :
        print ("Transaksi Selanjutnya : ", antrian[2] , " Jenisnya ", antrian[3] )
    elif pilihan == 3 :
        print ("Antrian Yang Dihapus Yaitu ", antrian[0] , " Jenisnya ", antrian[1])
        antrian.popleft()
        antrian.popleft()
    elif pilihan == 4 :
        break
    else : 
        print("Tidak Ada Pilihan")

    

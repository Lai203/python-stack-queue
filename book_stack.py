#Buatlah Program yang memungkinkan pengguna untuk menambahkkan buku
#dengan informasi nama buku dan pengarang ke dalam tumpukan, serta 
#menghapus buku terakhir jika diperlukan. Program juga harus dapat 
#menampilkan buku teratas dari tumpukan

stack = []

def Buku_Baru (stack, buku_baru, penulis_baru) :
    stack.append(buku_baru)
    stack.append(penulis_baru)
    print (f"{buku_baru} karya {penulis_baru} ditambahkan")

def buang_buku (stack) :
    if len(stack) == 0 :
        print ("Tumpukan Kosong")
    else : 
        buku_teratas = stack.pop()
        buku_teratas = stack.pop()
        print (f"{buku_teratas} Dihapus")

def tampilkan_buku(stack):
    if len(stack) == 0 :
        print (f"Tumpukan Kosong")
    else : 
        buku_teratas = stack [-2]
        penulis_teratas = stack [-1]
        print (f"Buku Teratas Yaitu {buku_teratas} Karya {penulis_teratas} ")

while True:
    print ("Tumpukan Buku : ", stack)
    print ("1. Tumpuk Buku")
    print ("2. Buang Buku")
    print ("3. Buku Teratas")
    print ("4. Keluar Aplikasi")
    
    opsi = int(input("Masukkan Pilihan (1/2/3/4) : "))
    if opsi == 1 :
        buku_baru = input ("Judul Buku : ")
        penulis_baru = input ("Pengarang : ")
        print("")
        Buku_Baru (stack, buku_baru, penulis_baru)
    elif opsi == 2 :
        print ("")
        buang_buku(stack)
    elif opsi == 3 :
        print("")
        tampilkan_buku(stack)
    elif opsi == 4 :
        print ("")
        print("Program Selesai")
        break
    else :
        print ("")
        print ("Opsi Salah")
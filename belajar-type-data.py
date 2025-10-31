#TYPE DATA STRING SEBARIS

string_1 = "Hello python"
print (string_1)

text ="a multiline string\rin python"
print (text)

text ="""a multiline string in python"""
print (text)

# (\) atau (""") kutip dua 3x, bisa jadi pengganti backspace seperti diatas
print ("\n==============================")
print ("\t\n\tBIODATA SISWA\t\n\t")
print ("==============================\n")
print ("Nama\t:\tMuhammad Fachry Meesa")
print ("NIS\t:\t17517")
print ("Jurusan\t:\tRekayasa Perangkaat Lunak")
print ("Umur\t:\t16")
print ("Hobi\t:\tBerenang\n")

#TYPE DATA BOOLEAN LEWAT

#TYPE DATA NONE

data = None
print (data)

Nama = "fachry"
if Nama is None:
  print("Nama belum diisi")
else:
    print("Nama kamu adalah:", Nama)
    
#TYPE DATA LIST 

list_1=[2,4,8,16,32]
print(list_1[0])

list_2 = ["grayson","jason","tim","damian"]
print(list_2[2])

list_3 = [24,False,"Hello Python"]
print(list_3[1])

#append(menambahkan satu elemen di akhir list)
buah = ["ungger","chinchin"]
buah.append("mangga")
print(buah)

#extend(menambahkan beberapa elemen sekaligus dari list lain ke akhir list)

buah = ["anomali pisang","jeruk jawa"]
buah.extend(["mangga","apel"])
print(buah)

#insert(menambahkan elemen pada posisi tertentu(bukan diakhir))

angka = [1, 2, 3]
angka.insert(4,3)
print(angka)

#pop(menghapus elemen berdasarkan indeks(atau terakhir jika tidak di sebutkan)).

buah = ["anomali pisang","jeruk jawa","manggis","pisang bali","duren"]
buah.pop(3)
print(buah)

#sort()

angka=[5,2,9,1]
angka.sort()
print(angka)

angka=[5,2,9,1]
angka.sort(reverse=True)
print(angka)

#clear()

data=[1,2,3]
data.clear()
print(data)

#remove (menghapus elemen berdasarkan nilai,bukan indek).

buah=["apel","jeruk","mangga"]
buah.remove("apel")
print(buah)

#index (menemukan posisi (indeks) dari elemen tertentu)

nama=["Muhammad","Fachry","Meesa"]
print(nama.index("Fachry"))

#reverse (membalik urutanelement list tanpa mengurutkan)

warna=["merah","kuning","hijau"]
warna.reverse()
print(warna)

#count(menghitungberapa kali suatu nilai muncul dalam list)

angka=[1,2,2,3,2,2,2,2,2]
print(angka.count(2))

#LATIHAN

print("\n========DAFTAR BELANJA=========\n")

print("\nNO.1 Tambah Barang")
barang=["tang","linggis","obeng"]
barang.append("gunting")
print(barang)

print("\nNO.2 Hapus Barang")
barang=["tang","obeng","linggis","gunting","botol","smartphone"]
barang.pop(3)
print(barang)

print("\nNO.3 Lihat Daftar")
barang=["tang","obeng","tangga","keyboard","charger","mouse"]
barang.sort()
print(barang)

print("\nNO.4 Hapus Semua")
barang=["tang","obeng","tangga","keyboard","charger","mouse"]
barang.remove("tang")
print(barang)

print("\nNO.5 keluar")
barang=["tang","obeng","tangga","keyboard","charger","mouse"]
barang.clear()
print(barang)










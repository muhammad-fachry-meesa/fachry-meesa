
print("membuat boolean and")
print(True and False)   
print(False and True)
print(True and True)        
print(False and False)        

print("membuat boolean or")
print(True or False)   
print(False or True)
print(True or True)        
print(False or False)  

print("membuat boolean not")
print(not False)   
print(not True)
print(not True)        
print(not False)  
print()
print()


print("Membuat Operator Perbandingan")
#< kurang dari
#> lebih dari
#>= lebih dari sama dengan
#<= kurang dari sama dengan
#== sama dengan
#!= tidak sama dengan
print()

print("nilai yang Benar/True")
print(7>3)
print(1<4)
print(10>=3)
print(10<=18)
print(3==3)
print(5!=10)
print()

print("nilai yang Salah/False")
print(7>13)
print(11<4)
print(10>=13)
print(18<=10)
print(11==18)
print(8!=8)
print()

print("Latihan Soal")
print("No.1 Materi input-Buatlah yang menghasilkan pengguna memasukan nama, umur, hobi, dan terakhir tampilan sapaan")
print("No.2 materi input number-Buatlah program yang meminta pengguna memasukan umur, lalu menampil umur 2 tahun lagi")
print("No.3 Materi perbandingan-Buatlah program yang mengecek apakah umur seseorang itu antara 10 sampai 17 tahun disebut (Remaja)")

print()
print("Jawaban")
print()
print("NO.1")
nama = input("masukkan nama:")
umur = input("masukkan umur:")
hobi = input("masukkan hobi:")
print()
print(f"halo,nama saya {nama}, umur saya {umur}, hobi saya  {hobi}")

print()
print("NO.2")
print("masukkan umur:")
umur = int(input())
tua = umur + 2
print(f"umur kamu {umur}, dua tahun lagi kamu umur {tua}")

print()
print("NO.3")

umur = int(input("masukkan umur"))
status = { True: "anda remaja", False:"Anda bukan remaja"}[(10<= umur <=17)]
    
print("status kamu:", status)
    

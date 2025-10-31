#belajar elif

menu_pilihan = input("masukan pilihan menu (1-3):")

if menu_pilihan =="1":
    print("anda memilih menu 1")

elif menu_pilihan =="2": 
    print("anda memilih menu 2")

elif menu_pilihan =="3": 
    print("anda memilih menu 3")

else:
    print("menu tidak tersedia")

# NO.1 Buat kode masukkan nilai

#nilai lebih besar sama dengan 90 nilainya A
#nilai lebih besar sama dengan 80 nilainya B
#nilai lebih besar sama dengan 70 nilainya C
#else nilainya D.

nilai = int(input("masukkan nilai:  "))

if nilai >= 90:
    print("nilai anda A")

elif nilai >= 80:
     print("nilai anda B")

elif nilai >= 70:
     print("nilai anda C")
    
else:
     print("nilai anda D")

# NO.2 Buat masukkan nilai suhu
#jika besar dari 35 suhunya panas banget
#jika suhu besar dari 25 suhunya hangat
#jika di bawah  25 maka suhunya dingin 

nilai_suhu = input("masukkan nilai suhu : ")
if nilai_suhu >= "35" :
    print("suhunya panas bangettt tauu ihh")
    
elif nilai_suhu >= "25" :
    print("suhunya hangat")
    
else: 
    print("suhunya dingin bangett tauu")
    
#SOALNYA NYA KAGA JAUH DARI LATIHANNYA MENDING GAUSH NGIDEEEE

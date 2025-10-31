#HARIII

Hari = 4
1
match Hari:

     case 1: 
         print("senin")

     case 2: 
         print("selasa")

     case 3: 
         print("rabu")

     case 4: 
         print("kamis")

     case 5: 
         print("jum'at")

     case 6: 
         print("sabtu")

     case 7: 
         print("minggu")

# BULANNN

Bulan = 5

match Bulan:
    
    case 1:
        print("january")

    case 2:
        print("february")

    case 3:
        print("maret")

    case 4:
        print("april")

    case 5:
        print("meiii")

    case 6:
        print("juni")

    case 7:
        print("juli")

    case 8:
        print("agustus")

    case 9:
        print("september")

    case 10:
        print("oktober")

    case 11:
        print("november")

    case 12:
        print("december")

bulan = 4
hari = 3 

match hari:
    
    case 1 | 2 | 3 | 4 | 5 if bulan ==4:
        print("sekolah di bulan april")

    case 1 | 2 | 3 | 4 | 5 if bulan ==5:
        print("sekolah di bulan mei")

    case _:
        print("no match")


hari = 6 

match hari:
    
    case 1 | 2 | 3 | 4 | 5 :
        print("masuk sekolah ahh maless bagett guehh")

    case 6 | 7 :
        print("aseekk bangett nih libur coyyy")


#mested

max = int(input("jumlah bintang: "))
for i in range(max):
    for j in range(i):
        print(" ", end= "*")
    print()


#BELAJAR BERHITUNG

a = int(input("masukan angka pertama: "))
b = int(input("masukan angka pertama: "))
operator = input("masukkan operator(=,-,*./): ")

match operator:
    case "+":
        hasil = a + b
        print(f"hasil dari {a} + {b} = {hasil}")

    case "-":
        hasil = a - b
        print(f"hasil dari {a} - {b} = {hasil}")

    case "*":
        hasil = a * b
        print(f"hasil dari {a} * {b} = {hasil}")

    case "/":
        if b != 0:
            hasil = a / b
            print(f"hasil dari {a} / {b} = {hasil}")
        else:
            print("error: pembagian dengan nol tidak bisa")

    case _:
        print("operator tidak di kenal")




































































































































































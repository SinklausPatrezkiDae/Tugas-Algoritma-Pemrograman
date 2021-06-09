'''
    program menampilkan nilai huruf
    created by sinklaus patrezki dae (20083000013)
    kelas 2A
'''
import os
clear = lambda : os.system("cls")
jwb = "y"
while jwb == "y" or jwb == "Y":
    clear()
    print("--- PROGRAM MENAMPILKAN NILAI HURUF ---")
    print("---------------------------------------")
    print()
    a = input("Masukkan Nilai = ")
    n = int(a)
    if n < 0 or n > 100 :
        sts = "Inputan hanya boleh 0 sampai 100 saja "
    elif n > 80 :
        sts = "BAIK SEKALI"
    elif n >= 65 :
        sts = "BAIK"
    elif n >= 55 :
        sts = "CUKUP"
    elif n >= 40 :
        sts = "KURANG"
    else :
        sts = "KURANG SEKALI"
    print()
    print(sts)
    print()
    jwb = input("Cek lagi? (Y/T) = ")
    if jwb == "t" or jwb == "T":
        break
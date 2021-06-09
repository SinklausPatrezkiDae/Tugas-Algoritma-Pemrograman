'''
    program cek tingkat usia
    created by sinklaus patrezki dae (20083000013)
    kelas 2A
'''
import os
clear = lambda : os.system("cls")
jwb = "y"
while jwb == "y" or jwb == "Y":
    clear()
    print("-- PROGRAM CEK TINGKAT USIA --")
    print("------------------------------")
    print()
    n = input("Masukkan Nilai Usia = ")
    u = int(n)
    if u < 0 or u > 100 :
        sts = "Nilai Usia hanya boleh 1 Sampai 100 saja"
    elif u >= 60 :
        sts = "Lansia"
    elif u>=35 and u<=59 :
        sts = "Dewasa"
    elif u>=18 and u<=34 :
        sts = "Pemuda"
    elif u>=15 and u<=17 :
        sts = "Remaja"
    else :
        sts = "Anak-Anak"
    print()
    print(sts)
    print()
    jwb = input("Cek Lagi? (Y/T) = ")
    if jwb == "t" or jwb == "T":
        break
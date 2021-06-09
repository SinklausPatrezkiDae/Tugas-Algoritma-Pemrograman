'''
    program cek kelulusan
    created by sinklaus patrezki dae (20083000013)
    kelas 2A
'''
import os
clear = lambda : os.system("cls")
jwb = "y"
while jwb == "y"or jwb == "Y":
    clear()
    print("-- PROGRAM CEK KELULUSAN --")
    print("---------------------------")
    print()
    n = input("Masukkan Nilai = ")
    int_n = int(n)
    if int_n > 100 or int_n < 0 :
        int_n = 0
        sts = "Nilai yang dimasukkan hanya boleh 0 sampai 100 saja"
    elif int_n > 60 :
        sts = "LULUS"
    else:
        sts = "TIDAK LULUS"
    print()
    print(sts)
    print()
    jwb = input("Cek Lagi (Y/T) = ")
    if jwb == "t" or jwb == "T":
        break


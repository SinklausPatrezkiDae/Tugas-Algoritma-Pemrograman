'''
    program hitung nilai total transaksi printer epson T20
    created by sinklaus patrezki dae (20083000013)
    kelas 2A
'''
import os 
clear = lambda : os.system('cls')
jwb = "y"
while jwb == "y" or jwb == "Y" :
    clear()
    print("--- PROGRAM HITUNG NILAI TOTAL TRANSAKSI PRINTER EPSON T20 ---")
    print("--------------------------------------------------------------")
    hrg = 660000
    a = input("Masukkan Jumlah Printer = ")
    n = int(a)
    totHrg = n * hrg
    print("Total Harga = ",format(totHrg,",.2f"))
    print()
    jwb = input("Hitung Lagi? (Y/T) = ")
    if jwb == "t" or jwb == "T":
        break

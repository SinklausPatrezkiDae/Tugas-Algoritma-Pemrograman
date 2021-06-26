'''
SINKLAUS PATREZKI DAE
KELAS 2A
'''
import os
clear = lambda : os.system('cls')
#Perulangan untuk merestart program
jwb = 'y'
while jwb == 'y' or jwb == 'Y' :
    clear()
    Kode_Kota = ['a','b']
    kota = ['Surabaya','Bandung']

    jarak = [169,452]
    ongkirperkm = [2500,4000]

    #tampilkan List Kota Menggunakan While
    idx = 0
    print("------- PILIHAN KOTA TUJUAN ---------")
    while idx < len(Kode_Kota):
        print("----------------------------")
        print("Kode Kota     = " + Kode_Kota[idx])
        print("Kota Tujuan   = " + kota[idx])
        print("Jarak         = " + str(jarak[idx]),"Km")
        print("Ongkir Per Km = Rp." + str(format(ongkirperkm[idx],',.2f')))
        idx = idx + 1
    #buat inputan
    print("============================")
    pilihan = input("Masukkan Pilihan Kode Kota = ")

    '''
    Identifikasi Index berdasarkan pilihan 
    baca berulang index dalam list kode Kota
    jika valuenya sama dengan value pilihan maka tampilkan rincian Pengiriman
    '''
    idx = 0
    while idx < len(Kode_Kota):
        if Kode_Kota[idx] == pilihan :
            print("============================")
            print("---- RINCIAN PENGIRIMAN ----")
            print("Kota Tujuan   = " + kota[idx])
            print("Jarak         = " + str(jarak[idx]),"Km")
            print("Ongkir Per Km = Rp." + str(format(ongkirperkm[idx],',.2f')))
            #tahap hitung
            totbiaya = jarak[idx] * ongkirperkm[idx]
            #Tampilkan total Biaya
            print("----------------------------")
            print("Total Biaya Pengiriman = Rp." + str(format(totbiaya,',.2f')))
            print("----------------------------")
        idx = idx + 1
    print("=============================================")
    jwb = input("Hitung Lagi ? (y/t) : ")
    if jwb == "t" or jwb == "T" :
        break
            



    
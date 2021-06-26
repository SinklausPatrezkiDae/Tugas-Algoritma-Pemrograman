'''
SINKLAUS PATREZKI DAE
KELAS 2A
'''
import os
clear = lambda : os.system('cls')
jwb = 'y'
#Perulangan untuk merestart program
while jwb == 'y' or jwb == 'Y' :
    #List Barang
    clear()
    kode_barang = ['a','b','c','d','e']
        
    namaBarang = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]
    #Set Nilai PPN dan Diskon  
    ppn = 0.01
    diskon = 0.05

    #tampilkan List Barang Menggunakan While
    idx = 0
    print("------------ DAFTAR BARANG ---------------")
    while idx < len(kode_barang):
        print("-------------------------------------")
        print("> Kode Barang  = " + kode_barang[idx])
        print("> Nama Barang  = " + namaBarang[idx])
        print("> Harga Barang = Rp." + str(format(harga[idx],',.2f')))
        idx = idx + 1

    #buat inputan
    print("-------------------------------------")
    print("-------------------------------------")
    pilihan = input("Masukkan Pilihan Kode Barang = ")
    Qty = int(input("Masukkan Kuantitas Barang = "))

    '''
    Identifikasi Index berdasarkan pilihan 
    baca berulang index dalam list kode barang
    jika valuenya sama dengan value pilihan maka tampilkan rincian pembelian
    '''
    idx = 0
    while idx < len(kode_barang) :
        if kode_barang[idx] == pilihan :
            print("-------------------------------------")
            print("-------------------------------------")
            print("************ RINCIAN PEMBELIAN ************")
            print(">>> Nama Barang      = " + namaBarang[idx])
            print(">>> Harga Barang     = Rp." + str(format(harga[idx],',.2f')))
            print(">>> Kuantitas Barang = " + str(Qty)+" Buah")
            #tahap hitung biaya Awal
            totsebelumdiskon = harga[idx] * Qty
            if totsebelumdiskon >= 200000 :
                totdiskon = diskon * totsebelumdiskon
                totstlhdiskon = totsebelumdiskon - totdiskon
            else :
                totdiskon = 0
                totstlhdiskon = totsebelumdiskon
            #tahap Hitung PPN
            totppn = ppn * totstlhdiskon
            totbyr = totstlhdiskon + ppn
            #Tampilkan hasil
            print("=============================================")
            print("Total Harga Sebelum Diskon = Rp." + str(format(totsebelumdiskon,',.2f')))
            print("Total Diskon               = Rp " + str(format(totdiskon,',.2f')))
            print("Total Harga Setelah Diskon = Rp." + str(format(totstlhdiskon,',.2f')))
            print("Total PPN                  = Rp." + str(format(totppn,',.2f')))
            print("=============================================")
            print("Total Biaya                = Rp." + str(format(totbyr,',.2f')))
        idx = idx + 1
    print("=============================================")
    jwb = input("Hitung Lagi ? (y/t) : ")
    if jwb == "t" or jwb == "T" :
        break

    
    

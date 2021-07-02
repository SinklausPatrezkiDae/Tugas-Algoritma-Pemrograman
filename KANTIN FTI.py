'''
Sinklaus Patrezki Dae
Kelas 2A
'''
import os
jwb = 'y'
while jwb == 'y' or jwb == 'Y':
    #siapkan Variabel
    kode=['a','b','c','d','e','f','g','h','i','j','k']
    namabarang=['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel',
                'Teh Dingin/Hangat/panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    harga = [15000,14900,12900,13000,15000,17000,2500,5000,6500,3500,5000]
    #Interfaces
    os.system('cls')
    print("===================================")
    print("KANTIN FAKULTAS TEKNOLOGI INFORMASI")
    idx = 0
    #Tampilkan List menggunakan Perulangan
    print("===================================")
    print("Daftar Barang")
    while idx < len(kode):
        print(kode[idx],".", namabarang[idx]," = Rp.", format(harga[idx],',.2f'))
        idx = idx + 1
    #Input Barang dan qty
    print("===================================")
    pil = input(">> Masukkan Kode Barang = ")
    pilihan = pil.lower()
    qty     = int(input(">> Masukkan Jumlah Pesanan  = "))
    #baca berulang kali idx dalam list jika sama dengan pilihan ambil idxnya    
    idx = 0;
    while idx < len(namabarang):
            #jika value pada list kode[idx] == pilihan
                if kode[idx] == pilihan:
                #ambil nama barang
                    nm_brg = namabarang[idx]
                #ambil harga satuan
                    hrgsatuan = harga[idx]
                    #Hitung Total Harga
                    totHargaBrng = qty * hrgsatuan
                    #Membedakan Makanan dan minuman
                    if idx <= 5 :
                        print("=================================")
                        print("RINCIAN PEMBELIAN")
                        print("=================================")
                        print("Makanan             = " + nm_brg)
                        print("Jumlah yang dipesan = " + str(qty) + " Porsi")
                        print("Harga per porsi     = Rp." + str(format(hrgsatuan,',.2f')))
                        print("Totall harga        = Rp. " + format(totHargaBrng,',.2f'))
                    else :
                        print("=================================")
                        print("RINCIAN PEMBELIAN")
                        print("=================================")
                        print("Minuman             = " + nm_brg)
                        print("Jumlah yang dipesan = " + str(qty) + " Gelas")
                        print("Harga per Gelas     = Rp." + str(format(hrgsatuan,',.2f')))
                        print("Total harga         = Rp." + format(totHargaBrng,',.2f'))
                    #Inputan Bayar
                    print("=================================")
                    bayar = int(input("Jumlah bayar = "))  
                    #HITUNG kembalian
                    kembalian    = bayar - totHargaBrng
                    #TAMPILKAN hasil
                    print("=================================")
                    print("TOTAL BAYAR")
                    print("=================================")
                    print("Total Harga  = Rp." + format(totHargaBrng,',.2f'))
                    print("Kembalian    = Rp." + format(kembalian,',.2f'))
                #jika tidak cocok, lanjut ke i berikutnya
                idx = idx + 1  
    #Buat Inputan untuk mengulangi program
    print("=================================")
    jwb = input("Ulangi Program ? = ")
    if jwb == "t" or jwb == "T" :
        break
                    


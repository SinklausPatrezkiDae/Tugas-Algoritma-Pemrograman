'''
SINKLAUS PATREZKI DAE
KELAS 2A
'''
import os
clear = lambda : os.system('cls')
jwb = 'y'
while jwb == 'y' or jwb == 'Y' :
    clear()
    print('-------------------------------------------------------')   
    print('          BENGKEL MOTOR UD')
    print('-------------------------------------------------------')
    merek_oli = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]
    ppn = 0.01
    diskon = 0.05
    print('PILIHAN BARANG')
    print('-------------------------------------------------------')
    print('>> 1 = ',merek_oli[0],'Harga = ',format(harga[0],',.2f'))
    print('>> 2 = ',merek_oli[1],'Harga = ',format(harga[1],',.2f'))
    print('>> 3 = ',merek_oli[2],'Harga = ',format(harga[2],',.2f'))
    print('>> 4 = ',merek_oli[3],'Harga = ',format(harga[3],',.2f'))
    print('>> 5 = ',merek_oli[4],'Harga = ',format(harga[4],',.2f'))
    print('-------------------------------------------------------')
    pil = int(input("Masukan Pilihan = "))   
    jmlh = int(input("Masukkan Jumlah Pembelian = "))
    idx = 0
    while idx >=0 and idx < 5 :
        idx = idx + 1
        if (pil - 1) == idx :
            break 
        elif pil == 1 :
            idx = 0
            break
    totHrgsblmppn = jmlh * harga[idx]
    totppn = totHrgsblmppn * ppn
    totHrg = totHrgsblmppn + totppn
    if totHrgsblmppn >= 200000 :
        totdiskon = totHrg * diskon
        totHrgsesudahDiskon = totHrg - totdiskon
        print('-------------------------------------------------------')
        print('DISKON 5%')
        print('PPN 1%')
        print('-------------------------------------------------------')
        print('Merek Oli                  = ',merek_oli[idx])
        print('Harga                      = ',format(harga[idx],',.2f'))
        print('Total Harga                = ',format(totHrgsblmppn,',.2f'))
        print('Total Harga Setelah PPN    = ',format(totHrg,',.2f'))
        print('Total Harga Setelah Diskon = ',format(totHrgsesudahDiskon,',.2f'))
    else :
        print('-------------------------------------------------------')
        print('PPN 1%')
        print('-------------------------------------------------------')
        print('Merek Oli                  = ',merek_oli[idx])
        print('Harga                      = ',format(harga[idx],',.2f'))
        print('Total Harga                = ',format(totHrgsblmppn,',.2f'))      
        print('Total Harga Setelah PPN    = ',format(totHrg,',.2f'))
    print('-------------------------------------------------------')
    jwb = input('Beli Lagi? (y/t) : ')
    if jwb == 't' or jwb == 'T':
        break
    






    



        






    


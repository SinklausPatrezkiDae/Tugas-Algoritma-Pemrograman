'''
SINKLAUS PATREZKI DAE
KELAS 2A
'''
import os
clear = lambda : os.system('cls')
jwb = 'y'
while jwb == 'y' or jwb == 'Y' :
    kota = ['Surabaya','Bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]
    b = 't'
    while b == 't' or b == 'T' :
        clear()
        print('-------------------------------------------------------')   
        print('TRANSAKSI BIAYA EKSPEDISI')
        print('-------------------------------------------------------')
        print('PILIHAN KOTA')   
        print('-------------------------------------------------------')
        print('>> 1 = ',kota[0],'Jarak = ',jarak[0],'Ongkir PerKm = ',ongkirperkm[0])   
        print('>> 2 = ',kota[1],'Jarak = ',jarak[1],'Ongkir PerKm = ',ongkirperkm[1])   
        print('-------------------------------------------------------')
        pil = int(input('Masukan Pilihan Kota = '))      
        print('-------------------------------------------------------')
        b = input('Lakukan Transaksi? (y/t) : ')
        if b == 'y' or b == 'Y' :
            break
    idx = 0
    while idx >=0 and idx < 2 :
        idx = idx + 1
        if idx == 0 :
            pil = 1
            break
        else:
            idx = pil - 1
            break 
    ongkir = jarak[idx]*ongkirperkm[idx]         
    print('-------------------------------------------------------')
    print('>> Kota         = ',kota[idx])
    print('>> Jarak        = ',jarak[idx],'Km')
    print('>> Ongkir PerKm = ',format(ongkirperkm[idx],',.2f'))
    print('-------------------------------------------------------')
    print('>> Total Harga  = ',format(ongkir,',.2f'))          
    print('-------------------------------------------------------')
    jwb = input('Beli Lagi? (y/t) : ')
    if jwb == 't' or jwb == 'T':
        break
    

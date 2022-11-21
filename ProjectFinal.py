dataPasien = [
    {
        'nama': 'Rara Widjaja',
        'umur': 19,
        'jenis_kelamin': 'P',
        'lokasi' : 'ICU, Lt.1\t',
        'keterangan' : 'Asma'
        
    },
    {
        'nama': 'Bima Rahmat',
        'umur': 55,
        'jenis_kelamin' : 'L',
        'lokasi': '301, Lt.3, Kenanga',
        'keterangan' : 'Diabetes'
    },
    {
        'nama': 'Sena Ahmad',
        'umur': 22,
        'jenis_kelamin': 'L',
        'lokasi' : '505, Lt.5, Kamboja',
        'keterangan' : ''
    }
]

pasien = []

######### OPSI MENAMPILKAN DAFTAR PASIEN #########
def menampilkanDaftarPasien() :
    print('Daftar Pasien Rawat Inap\n')
    print('ID\t| Nama\t\t| Umur\t| P/L\t| Lokasi Rawat Inap\t| keretangan\t')
    for i in range(len(dataPasien)) :
        print('{}\t| {} \t| {}\t| {}\t| {}\t| {}\t'.format(i,dataPasien[i]['nama'],dataPasien[i]['umur'],dataPasien[i]['jenis_kelamin'], dataPasien[i]['lokasi'],dataPasien[i]['keterangan']))

def menuUtamaDaftarPasien():
    while True:
        menuDaftarPasien = str(input('''
            Selamat datang di RS Bunda
        
            Pilih opsi berikut:
                1. Tampilkan data pasien keseluruhan
                2. Cari Data Pasien
                3. Kembali

                Jawab : ''')) 

        if (menuDaftarPasien == '1') :
            menampilkanDaftarPasien()
            while True: 
                menuKembali = str(input('Ketik \'X\' untuk Kembali: '))           
                if menuKembali == 'X' :
                    menuUtamaDaftarPasien()     
                else :
                    False
                    print('Tidak Ada pilihan {}. Ulangi kembali'.format(menuKembali))
                
        elif (menuDaftarPasien == '2') :
            for findData in range(len(dataPasien)):          
                findData = int(input('Masukkan ID data pasien : '))
                if findData >= len(dataPasien):
                    print('Tidak ada data')
                elif findData <= len(dataPasien) :
                    print('ID\t| Nama\t\t| Umur\t| P/L\t| Lokasi Rawat Inap\t| keretangan\t')
                    print('{}\t| {} \t| {}\t| {}\t| {}\t| {}\t'.format(findData,dataPasien[findData]['nama'],dataPasien[findData]['umur'],dataPasien[findData]['jenis_kelamin'], dataPasien[findData]['lokasi'],dataPasien[findData]['keterangan']))

                    menuKembali = input('Tekan \'X\' untuk Kembali : ')
                    if menuKembali == 'X':
                        menuUtamaDaftarPasien()
                    else :
                        False
                        print('Tidak ada opsi {}. Ulangi kembali'.format(menuKembali))
                else:
                    False
                    print('Tidak ada opsi {}. Ulangi kembali'.format(menuDaftarPasien))
                    menuDaftarPasien
        elif (menuDaftarPasien == '3'):
            menuUtamaCapstone()
              
        
                 
         
######### OPSI MENAMBAH DAFTAR PASIEN #########
def menambahDataPasien() :
    menampilkanDaftarPasien() 
    menambahDataPasien_Back = str(input('Anda yakin ingin menambah data? Ketik \'X\' apabila ingin kembali dan \'1\' apabila ingin menambahkan data: '))
    while True: 
        if menambahDataPasien_Back == '1' :
            namaPasien = input('Masukkan Nama Pasien : ') 
            umurPasien = int(input('Masukkan Umur Pasien : '))
            jenisKelamin = input('Masukkan Jenis Kelamin Pasien : ')
            lokasi = input('Masukkan Lokasi Rawat Inap (Ruangan, Lantai, Cluster) : ')
            keterangan = input('Tekan \'Enter\' apabila belum ada keterangan : ')
            dataPasien.append({
                'nama': namaPasien,
                'umur': umurPasien,
                'jenis_kelamin': jenisKelamin,
                'lokasi' : lokasi,
                'keterangan' : keterangan
            })
               
            data = set()
            pasien = []
            for d in dataPasien:
                t = tuple(d.items())
                if t not in data:
                    data.add(t)
                    pasien.append(d)
            print('Data pasien sudah diperbaharui')
            print('Daftar Pasien Rawat Inap\n')
            print('ID\t| Nama\t\t| Umur\t| P/L\t| Lokasi Rawat Inap\t| keretangan\t')        
            for i in range(len(dataPasien)) :
                print('{}\t| {} \t| {}\t| {}\t| {}\t| {}\t'.format(i,pasien[i]['nama'],pasien[i]['umur'],pasien[i]['jenis_kelamin'], pasien[i]['lokasi'], pasien[i]['keterangan'])) 

            break       

        elif menambahDataPasien_Back == 'X':
            menuUtamaCapstone()
        else:
            False
            print('Tidak ada pilihan. ulangi kembali')
            menambahDataPasien()

        
            
######### OPSI MENGHAPUS DAFTAR PASIEN #########
def menghapusDataPasien() :
    hapusData = str(input(''' Menu Menghapus Data Pasien
        1. Hapus data Pasien
        2. Kembali

    Pilih : '''))
    while True: 
        if hapusData == '1':
            menampilkanDaftarPasien()
            for findData in range(len(dataPasien)):   
                findData = int(input('Masukkan ID data pasien : '))
                if findData >= len(dataPasien):
                    print('Tidak ada data pasien')
                elif findData <= len(dataPasien):
                    print('ID\t| Nama\t\t| Umur\t| P/L\t| Lokasi Rawat Inap\t| keretangan\t')
                    print('{}\t| {} \t| {}\t| {}\t| {}\t| {}\t'.format(findData,dataPasien[findData]['nama'],dataPasien[findData]['umur'],dataPasien[findData]['jenis_kelamin'], dataPasien[findData]['lokasi'],dataPasien[findData]['keterangan']))
                    del dataPasien[findData]
                    print('Data berikut sudah dihapus')

                    menuKembali = input('Tekan \'X\' untuk Kembali : ')
                    if menuKembali == 'X':
                        menuUtamaCapstone() 
                    else :
                        False
                        print('Tidak ada opsi {}. Ulangi kembali'.format(menuKembali))
                    
                else:
                    False
                    print('Tidak ada data pasien')
                    break

        elif hapusData == '2':
            menuUtamaCapstone()
        else:
            False
            print('Tidak ada pilihan {}. Ulangi kembali'.format(hapusData))
            menghapusDataPasien()


######### OPSI MENGUPDATE DAFTAR PASIEN #########
def mengupdateDataPasien() :
    yangInginDiubah = str(input('''
    Pilih data yang ingin diubah:
        1. Nama
        2. Umur
        3. Jenis Kelamin
        4. Lokasi
        5. Keterangan
        6. Kembali

    Pilihan: '''))
    while True:
        if yangInginDiubah == '1':
            for findData in range(len(dataPasien)):   
                findData = int(input('Masukkan ID data pasien : '))
                gantiDengan = input('Ganti dengan : ')
                if findData >= len(dataPasien):
                    print('Tidak ada data pasien')
                elif findData <= len(dataPasien):
                    dataPasien[findData].update(dict(nama = gantiDengan))
                    menampilkanDaftarPasien()
                    print('Data sudah terupdate')
                    while True:
                        menuKembali = input('Tekan \'X\' untuk Kembali : ')
                        if menuKembali == 'X':
                            menuUtamaCapstone() 
                        else:
                            False
                            print('Tidak ada pilihan {}, ulangi kembali'.format(menuKembali))

        elif yangInginDiubah == '2': 
            for findData in range(len(dataPasien)):   
                findData = int(input('Masukkan ID data pasien : '))
                gantiDengan = input('Ganti dengan : ')
                if findData >= len(dataPasien):
                    print('Tidak ada data pasien')
                elif findData <= len(dataPasien):
                    dataPasien[findData].update(dict(umur = gantiDengan))
                    menampilkanDaftarPasien()
                    print('Data sudah terupdate')
                    while True:
                        menuKembali = input('Tekan \'X\' untuk Kembali : ')
                        if menuKembali == 'X':
                            menuUtamaCapstone() 
                        else:
                            False
                            print('Tidak ada pilihan {}, ulangi kembali'.format(menuKembali))
        
        elif yangInginDiubah == '3':
            for findData in range(len(dataPasien)):   
                findData = int(input('Masukkan ID data pasien : '))
                gantiDengan = input('Ganti dengan : ')
                if findData >= len(dataPasien):
                    print('Tidak ada data pasien')
                elif findData <= len(dataPasien):
                    dataPasien[findData].update(dict(jenis_kelamin = gantiDengan))
                    menampilkanDaftarPasien()
                    print('Data sudah terupdate')
                    while True:
                        menuKembali = input('Tekan \'X\' untuk Kembali : ')
                        if menuKembali == 'X':
                            menuUtamaCapstone() 
                        else:
                            False
                            print('Tidak ada pilihan {}, ulangi kembali'.format(menuKembali))

        elif yangInginDiubah == '4':
            for findData in range(len(dataPasien)):   
                findData = int(input('Masukkan ID data pasien : '))
                gantiDengan = input('Ganti dengan : ')
                if findData >= len(dataPasien):
                    print('Tidak ada data pasien')
                elif findData <= len(dataPasien):
                    dataPasien[findData].update(dict(lokasi = gantiDengan))
                    menampilkanDaftarPasien()
                    print('Data sudah terupdate')
                    while True:
                        menuKembali = input('Tekan \'X\' untuk Kembali : ')
                        if menuKembali == 'X':
                            menuUtamaCapstone() 
                        else:
                            False
                            print('Tidak ada pilihan {}, ulangi kembali'.format(menuKembali))

        elif yangInginDiubah == '5':
            for findData in range(len(dataPasien)):   
                findData = int(input('Masukkan ID data pasien : '))
                gantiDengan = input('Ganti dengan : ')
                if findData >= len(dataPasien):
                    print('Tidak ada data pasien')
                elif findData <= len(dataPasien):
                    dataPasien[findData].update(dict(keterangan = gantiDengan))
                    menampilkanDaftarPasien()
                    print('Data sudah terupdate')
                    while True:
                        menuKembali = input('Tekan \'X\' untuk Kembali : ')
                        if menuKembali == 'X':
                            menuUtamaCapstone() 
                        else:
                            False
                            print('Tidak ada pilihan {}, ulangi kembali'.format(menuKembali))

        elif yangInginDiubah == '6':
            menuUtamaCapstone()

        else:
            False
            print('Tidak ada pilihan {}. Ulangi kembali'.format(yangInginDiubah)) 


def exitProgram():
    print('\n Terima kasih sudah menggunakan aplikasi ini')
    exit()


def menuUtamaCapstone():
    while True:
        pilihanMenu = str(input('''
            
        Selamat Datang di Rumah Sakit

        List Menu :
        1. Menampilkan Daftar Pasien
        2. Menambah Data Pasien Baru
        3. Menghapus Data Pasien Rawat Inap
        4. Mengubah Data Pasien
        5. Exit

        Masukkan angka Menu yang ingin dijalankan : '''))                    
        if(pilihanMenu == '1') :
            menuUtamaDaftarPasien()
        elif(pilihanMenu == '2') :
            menambahDataPasien()
        elif(pilihanMenu == '3') :
            menghapusDataPasien()
        elif(pilihanMenu == '4') :
            mengupdateDataPasien()
        elif(pilihanMenu == '5') :
            exitProgram()
        else:
            False 
            print('Tidak ada pilihan {}. Ulangi kembali'.format(pilihanMenu))  

######### OPSI MENU UTAMA CAPSTONE #########
print('CAPSTONE : Data Pasien Rumah Sakit - Niken')
while True:
    mulai = str(input('''
    
        1. Untuk mulai program:
        2. Exit Program 
        
        pilih: '''))
    if mulai == '1':
        menuUtamaCapstone()
    elif mulai == '2':
        exitProgram()
    else:
        False
        print('Tidak ada pilihan {mulai}. ulangi kembali')
    


            


        

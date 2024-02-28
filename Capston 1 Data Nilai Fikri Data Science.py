#Capton Default Data Nilai Siswa

mataKuliah = ['Logika Matematika','Machine Learning','Dasar Pemograman']
wali = [[1,'Bobi'],[2,'Jafar']]
siswa = [[1001,'Bob',{mataKuliah[0]: 70,mataKuliah[1]: 85,mataKuliah[2]: 93},wali[0][0]],
         [1002,'Budi',{mataKuliah[0]: 75,mataKuliah[1]: 82,mataKuliah[2]: 78},wali[0][0]],
         [1003,'Rana',{mataKuliah[0]: 70,mataKuliah[1]: 95,mataKuliah[2]: 80},wali[0][0]],
         [2001,'Leo',{mataKuliah[0]: 80,mataKuliah[1]: 70,mataKuliah[2]: 50},wali[1][0]],
         [2002,'Lala',{mataKuliah[0]: 90,mataKuliah[1]: 99,mataKuliah[2]: 88},wali[1][0]],
         [1004,'Kana',{mataKuliah[0]: 77,mataKuliah[1]: 66,mataKuliah[2]: 55},wali[1][0]]
        ]

# siswa = []


#Menu Wali Kelas

def cekKode(id):                #Fungsi cek kode wali di list, jika ada akan me-return True selainnya False
    for i in range(len(wali)):
        if id == wali[i][0]:
            return True
    return False

def cekIndexWali(id):           #Fungsi cek kode wali di list, jika ada akan me-return i
    for i in range(len(wali)):
        if id == wali[i][0]:
            return i
        else :
            return False

def tampilWaliIndex(kd):        #Fungsi menampilkan data wali berdasarkan kode wali
    print('Kode Wali Kelas\t|Nama\t\t')
    print(str(wali[kd][0])+'\t\t|'+wali[kd][1])

def tampilSemuaDaftarWali():    #Fungsi menampilkan semua daftar Wali
    if wali == [] :
        print('Data Wali Masih Kosong')
        print()
    else :
        print('Daftar Wali')
        print('Nama\t\t|'+'Kode\t\t|')
        for i in range(len(wali)):
            print(wali[i][1],'\t\t|'+ str(wali[i][0])+'\t\t|')
    
def cekBanyakSiswa(kd):         #Fungsi untuk mengecek banyaknya siswa yang dimiliki wali menggunakan kode wali
    count = 0
    for i in range(len(siswa)):
        kode = int(str(siswa[i][0])[:1])
        if kode == kd :
            count+=1
        else :
            continue
    return count

def hapusSiswaKode(kd):         #Fungsi untuk menghapus semua siswa yang memiliki kode dosen yang sama
    templist = []
    for i in range(len(siswa)):
        kode = int(str(siswa[i][0])[:1])
        if kode != kd :
            templist.append(siswa[i])
    return templist

def hapusWaliKode(kd):          #Fungsi untuk menghapus atribut kode wali pada list siswa menggunakan kode wali
    for i in range(len(siswa)):
        kode = int(str(siswa[i][0])[:1])
        if kode == kd :
            siswa[i][3] = 0
        else :
            continue

        
def verifikasiHapusWali(kd):    #Fungsi untuk verifikasi apakah user yakin akan melanjutkan 
    while True :                #operasi hapus data wali atau tidak
        verification = input('Akan dihapus apakah anda yakin (ya/tidak) : ')
        if verification.upper() == 'YA':
            hapusWaliKode(kd+1)
            wali.pop(kd)
            print('Data Berhasil Dihapus')
            print()
            break
        elif verification.upper() == 'TIDAK':
            print()
            break
        else :
            print('Opsi yang dimasukkan salah')
            print()


#====================================================================================

def ListSiswaKosong(kd):        #Cek apakah list siswa kosong berdasarkan kode wali nya
    if siswa == [] :
        return True
    cekSiswa = 0
    for i in range(len(siswa)):
        if int(str(siswa[i][0])[:1]) == kd :
            cekSiswa += 1
    if cekSiswa < 1 :
        return True
    return False


def cekNIM(nim):                #Cek apakah nim sudah ada atau belum
    for i in range(len(siswa)):
        if nim == siswa[i][0]:
            return True
    return False

def cekIndexSiswa(nim):         #Cek nim mahasiswa dan me return index mahasiswa tersebut
    for i in range(len(siswa)):
        if nim == siswa[i][0]:
            return i

def tampilSiswa(nim):           #Tampil data siswa berdasarkan nim
    i = cekIndexSiswa(nim)
    print('Data Mahasiswa')
    print('Nama\t\t:',siswa[i][1])
    print('NIM\t\t:',siswa[i][0])
    print()

def tampilNilai(nim):           #Tampil data nilai berdasarkan NIM
    i = cekIndexSiswa(nim)
    for j in range(0,len(mataKuliah)):
        print(list(siswa[i][2].keys())[j],'\t:',list(siswa[i][2].values())[j])

def tampilDaftarSiswa(kd):      #Tampil semua data mahasiswa berdasarkan kode wali-nya
    if siswa == [] :
        print('Data Siswa Masih Kosong')
        print()
    else :
        print('Daftar Mahasiwa')
        print('Nama\t\t\t|'+'NIM\t\t|')
        for i in range(len(siswa)):
            kode = int(str(siswa[i][0])[:1])
            if kode == kd :
                print(siswa[i][1],'    \t\t|'+ str(siswa[i][0])+'\t\t|')
            else :
                continue

def tampilSemuaDaftarSiswa():   #Tampil semua data mahasiswa
    if siswa == [] :
        print('Data Siswa Masih Kosong')
        print()
    else :
        print('Daftar Mahasiwa')
        print('Nama\t\t|'+'NIM\t\t|')
        for i in range(len(siswa)):
            print(siswa[i][1],'\t\t|'+ str(siswa[i][0])+'\t\t|')

def tampilNamaNIM(index):       #Menampilkan nama dan nim mahasiswa berdasarkan index yang diberikan
    print('Data Mahasiswa')
    print('Nama\t :',siswa[index][1])
    print('NIM\t :',siswa[index][0])

def tambahDataSiswa(nama,nim,kodeWali): #Fungsi untuk menambahkan data mahasiswa dengan parameter nama,nim, dan kode wali
    i = cekIndexWali(kodeWali)
    nilaiAwal = {}
    for x in range(len(mataKuliah)):
        nilaiAwal[mataKuliah[x]] = 0
    nama = nama.title()
    listSiswaBaru = [nim,nama,nilaiAwal,wali[i][0]]
    siswa.append(listSiswaBaru)

def verifikasiHapus(index):     #Fungsi untuk mengverifikasi apakah user akan melanjutkan fungsi atau tidak
    while True :
        verification = input('Akan dihapus apakah anda yakin (ya/tidak) : ')
        if verification.upper() == 'YA':
            siswa.pop(index)
            print('Data Berhasil Dihapus')
            print()
            break
        elif verification.upper() == 'TIDAK':
            print()
            break
        else :
            print('Opsi yang dimasukkan salah')
            print()

#====================================================================================

def editNilaiMatkul(opsi,indexSiswa):   #Fungsi untuk mengubah nilai mahasiswa berdasarkan index mahasiswanya dan index matakuliah
    while True :
        editNilai = input(f'Masukkan nilai baru untuk matakuliah {mataKuliah[opsi-1]} : ')
        if editNilai == '' or editNilai.isdigit() == False or (int(editNilai) < 0 or int(editNilai) >100):
            print('Nilai yang dimasukkan salah')
            print()
        else :
            while True :
                inputEditData = input(f'Nilai {mataKuliah[opsi-1]} Akan Dirubah Menjadi {editNilai} (Ya/Tidak)? ')
                if inputEditData.upper() == 'YA':
                    siswa[indexSiswa][2][mataKuliah[opsi-1]] = int(editNilai)
                    print('Nilai Mahasiswa Berhasil Diubah')
                    print()
                    break
                elif inputEditData.upper() == 'TIDAK':
                    print()
                    continue
                else :
                    print('Opsi yang dimasukkan salah')
                    print()
            break

def editSemuaNilaiMatkul(indexSiswa):   #Fungsi menampilkan semua nilai mahasiswa berdasarkan index mahasiswa tersebut
    for i in range(len(mataKuliah)):
        while True :
            editNilai = input(f'Masukkan nilai baru untuk matakuliah {mataKuliah[i]} : ')
            if editNilai == '' or editNilai.isdigit() == False or (int(editNilai) < 0 or int(editNilai) >100):
                print('Nilai yang dimasukkan salah')
                print()
            else :
                while True :
                    inputEditData = input(f'Nilai {mataKuliah[i]} Akan Dirubah Menjadi {editNilai} (Ya/Tidak)? ')
                    if inputEditData.upper() == 'YA':
                        siswa[indexSiswa][2][mataKuliah[i]] = int(editNilai)
                        print('Nilai Mahasiswa Berhasil Diubah')
                        print()
                        break
                    elif inputEditData.upper() == 'TIDAK':
                        print()
                        break
                    else :
                        print('Opsi yang dimasukkan salah')
                        print()
                break

def tampilSemuaDaftarMatakuliah():  #Fungsi untuk menampilkan semua data nilai
    if mataKuliah == [] :
        print('Data Matakuliah Masih Kosong')
        print()
    else :
        print('Daftar Matakuliah')
        for i in range(len(mataKuliah)):
            print(f'{i+1}. {mataKuliah[i]}')

def verifikasiHapusMatakuliah(index):   #Fungsi untuk mengverifikasi apakah user akan menghapus 
    while True :                        #data matakuliah berdasarkan index matakuliah tersebut
        verification = input(f'{mataKuliah[index]} akan dihapus apakah anda yakin (ya/tidak) : ')
        if verification.upper() == 'YA':
            for i in range(len(siswa)):
                del siswa[i][2][mataKuliah[index]]
            mataKuliah.pop(index)
            print('Data Berhasil Dihapus')
            print()
            break
        elif verification.upper() == 'TIDAK':
            print()
            break
        else :
            print('Opsi yang dimasukkan salah')
            print()

def cekMK(nama):                        #Fungsi untuk cek nama matakuliah di dalam list matakuliah
    for i in range(len(mataKuliah)):    #jika ada maka akan return True jika tidak ada akan return False
        if nama.title() == mataKuliah[i]:
            return True
    return False

#====================================================================================

def sortRanking(listRank):              #Fungsi untuk sorting ranking mahasiswa dari terkecil ke terbesar
    l = (len(listRank))
    for i in range(l):
        for j in range(0, l-i-1):
            if listRank[j][1] < listRank[j+1][1]:
                listRank[j], listRank[j+1] = listRank[j+1], listRank[j]

def listRangking(nim):                  #Fungsi untuk membuat list ranking berdasarkan daftar nim
    tempList = []
    j = cekIndexSiswa(nim)
    for i in range(len(siswa)):
        total = 0
        if siswa[i][3] == siswa[j][3]:
            for x in range(0,len(mataKuliah)):
                total = total + siswa[i][2][mataKuliah[x]]
            avg = total/len(mataKuliah)
            tempList.append([siswa[i][0],round(avg,2)])
    sortRanking(tempList)
    return tempList

def dosenDisplayRangking(kd):           #Fungsi untuk display list ranking berdasarkan kode wali-nya
    tempList = []
    for i in range(len(siswa)):
        total = 0
        if int(str(siswa[i][0])[:1]) == kd:
            for x in range(0,len(mataKuliah)):
                total = total + siswa[i][2][mataKuliah[x]]
            avg = total/len(mataKuliah)
            tempList.append([siswa[i][0],round(avg,2)])
    sortRanking(tempList)
    print('NIM\t\t |Nama\t\t |Nilai Akhir\t |Ranking')
    for i in range(len(tempList)):
        indexSiswa = cekIndexSiswa(tempList[i][0])
        print(str(tempList[i][0])+'\t\t |'+siswa[indexSiswa][1]+'\t\t |'+str(tempList[i][1])+'\t\t |'+ str(i+1))

def cekRankSiswa(nim):                  #Fungsi untuk mengembalikan index ranking
    listRank = listRangking(nim)        #mahasiswa berdasarkan nim mahasiswa
    for i in range(len(listRank)):
        if nim == listRank[i][0]:
            return i+1
    return 0


########################################## MAIN MENU ############################################################

while True :
    print()
    print('Selamat Datang')
    print('Pilih Menu :')
    print('1. Mahasiswa')
    print('2. Dosen')
    print('3. Admin')
    print('4. Keluar')
    inputMainMenu = input('Input opsi (1-4) : ')
    if inputMainMenu.isdigit() == False or (int(inputMainMenu) < 1 or int(inputMainMenu) > 4):
        print('Opsi yang dimasukkan salah')
        print()
    

########################################## MENU SISWA ############################################################
    elif int(inputMainMenu) == 1 :   
        if siswa == []:
            print('Data mahasiswa masih kosong') 
            print()
            continue
        menuSiswa = True
        while menuSiswa == True:
            while True:
                inputNIM = input('Masukkan NIM anda (input cancel untuk batal): ')
                if inputNIM.isdigit() == False or cekNIM(int(inputNIM)) == False :
                    print('NIM yang anda masukkan salah')
                else :
                    break
            nim = int(inputNIM)
            if cekNIM(nim) == True:
                print()
                print('Selamat Datang')
                indexNIM = cekIndexSiswa(nim)
                print(siswa[indexNIM][1])
                print('NIM :',nim)
                print('1. Lihat Nilai')
                print('2. Kembali ke halaman Login')
                while True :
                    inputSiswaMenu = input('Input opsi (1/2) : ')
                    if inputSiswaMenu.isdigit() == False or int(inputSiswaMenu) < 1 or int(inputSiswaMenu) > 2:
                        print('Opsi yang dimasukkan salah')
                        print()
                    else :
                        break
                if int(inputSiswaMenu) == 1:
                    print()
                    tampilNilai(nim)
                    print('1. Lihat Ranking Anda')
                    print('2. Kembali ke halaman Login')
                    while True :
                        inputSiswaMenu = input('Input opsi (1/2) : ')
                        if inputSiswaMenu.isdigit() == False or int(inputSiswaMenu) < 1 or int(inputSiswaMenu) > 2: 
                            print('Opsi yang dimasukkan salah')
                            print()
                        else :
                            break
                    if int(inputSiswaMenu) == 1 :
                        total = 0
                        for x in range(0,len(mataKuliah)):
                            total = total + siswa[indexNIM][2][mataKuliah[x]]
                        nilaiAkhir = total/len(mataKuliah)
                        print()
                        print(siswa[indexNIM][1])
                        print('NIM :',nim)
                        print('Nilai Akhir\t :',round(nilaiAkhir,2))
                        print('Rangking Kelas\t :',cekRankSiswa(nim))
                        print('1. Kembali ke halaman Login')
                        print()
                        while True :
                            inputSiswaMenu = input('Input opsi 1 untuk keluar : ')
                            if inputSiswaMenu.isdigit() == False or int(inputSiswaMenu) < 1 or int(inputSiswaMenu) > 2: 
                                print('Opsi yang dimasukkan salah')
                                print()
                            else :
                                break
                    else :
                        break
                else :
                    break
                menuSiswa = False
            else :
                print('NIM yang anda masukkan salah')
                menuSiswa = False
    


########################################## MENU DOSEN ############################################################

    elif int(inputMainMenu) == 2 :
        Loop1 = True
        while True:
            inputNDosen = input('Masukkan Kode Dosen anda : ')
            if inputNDosen.isdigit() == False or cekKode(int(inputNDosen)) == False:
                print('Kode yang anda masukkan salah')
                print()
                break

            else :
                kd = int(inputNDosen)
                print()
                print('Selamat Datang')
                indexKode = cekIndexWali(kd)
                print(wali[indexKode][1])
                print('Kode Dosen Anda',kd)
                while True :
                    print()
                    print('1. Lihat Data Mahasiswa')
                    print('2. Input Data Mahasiswa Baru')
                    print('3. Edit Data Mahasiswa')
                    print('4. Hapus Data Mahasiswa')
                    print('5. Kembali ke halaman Login')
                    print()

                    inputWaliMenu = input('Input opsi (1-4) : ')
                    if inputWaliMenu.isdigit() == False or (int(inputWaliMenu) < 1 or int(inputWaliMenu) > 5):
                        print('Opsi yang dimasukkan salah')

#--------------------------------------------- MENU DISPLAY ---------------------------------------------------------------------------------------------------------               
                    elif int(inputWaliMenu) == 1:
                        if ListSiswaKosong(kd) == True:
                            print('Belum ada Daftar Mahasiswa')
                            print()
                            continue
                        tampilDaftarSiswa(kd)
                        print()
                        print('1. Lihat Nilai')
                        print('2. Lihat Ranking')
                        print('3. Kembali')
                        while True :
                            inputLihatMenu = input('Input opsi (1-2) : ')
                            if inputLihatMenu.isdigit() == False or int(inputLihatMenu) < 1 or int(inputLihatMenu) > 3:
                                print('Opsi yang dimasukkan salah')
                                print()
                            elif int(inputLihatMenu) == 1 :
                                while Loop1 == True:
                                    LihatSiswa = input('Input NIM data mahasiswa : ')
                                    if cekNIM(int(LihatSiswa)) == False or LihatSiswa.isdigit() == False or int(str(LihatSiswa)[:1]) != kd :
                                        print('NIM yang dimasukkan salah')
                                    else :
                                        LihatSiswa = int(LihatSiswa)
                                        indexLihatSiswa = cekIndexSiswa(LihatSiswa)
                                        print()
                                        tampilNamaNIM(indexLihatSiswa)
                                        print()
                                        print('Daftar Nilai')
                                        tampilNilai(LihatSiswa)
                                        print('1. Lihat Nilai')
                                        print('2. Kembali')
                                        inputLihatMenu = input('Input opsi (1-2) : ')
                                        if inputLihatMenu.isdigit() == False or int(inputLihatMenu) < 1 or int(inputLihatMenu) > 2:
                                            print('Opsi yang dimasukkan salah')
                                            print()
                                        elif int(inputLihatMenu) == 2 :
                                            Loop1 = False
                                            break
                                break

                            elif int(inputLihatMenu) == 2 :
                                dosenDisplayRangking(kd)
                                print()
                                break
                            else :
                                break

#--------------------------------------------- MENU CREATE ---------------------------------------------------------------------------------------------------------
                    elif int(inputWaliMenu) == 2:
                        while True :
                            nimBaru = input('Masukkan NIM Mahasiswa Baru: ')
                            if nimBaru.isdigit() == False :
                                print('NIM yang dimasukkan salah')
                                print()
                            elif int(str(nimBaru)[:1]) != kd:
                                print('Nomor Awal Harus Serupa dengan Kode Dosen Anda !')
                                print()
                            elif cekNIM(int(nimBaru)) == True:
                                print('NIM yang dimasukkan sudah terdaftar')
                                print()
                            elif len(nimBaru) != 4:
                                print('NIM yang dimasukkan harus 4 digit')
                                print()
                            elif int(nimBaru) < 1:
                                print('NIM yang dimasukkan tidak boleh negatif')
                                print()
                            else :
                                break
                        
                        while True :
                            namaBaru = input('Masukkan Nama : ')
                            tempNama = namaBaru.replace(' ','')
                            if tempNama.isalpha() == False :
                                print('Nama harus alphabet')
                                print()
                            else :
                                break
                        print()
                        print('Data Baru Mahasiswa')
                        print('Nama Mahasiswa\t:',namaBaru.title())
                        print('NIM Mahasiswa\t:',nimBaru)
                        while True:
                            inputDataBaru = input('Data Mahasiswa Akan Ditambahkan (Ya/Tidak)? ')
                            if inputDataBaru.upper() == 'YA':
                                tambahDataSiswa(namaBaru,int(nimBaru),kd)
                                print('Data Mahasiswa Berhasil Ditambah')
                                print()
                                break
                            elif inputDataBaru.upper() == 'TIDAK':
                                print()
                                break
                            else :
                                print('Opsi yang dimasukkan salah')
                                print()

#--------------------------------------------- MENU EDIT ---------------------------------------------------------------------------------------------------------
                    elif int(inputWaliMenu) == 3:
                        if ListSiswaKosong(kd) == True:
                            print('Belum ada Daftar Mahasiswa')
                            print()
                            continue
                        while True:
                            print()
                            tampilDaftarSiswa(kd)
                            print('1. Lihat Nilai Mahasiswa')
                            print('2. Edit Data Mahasiswa')
                            print('3. Kembali')
                            while True :
                                inputEditMainMenu = input('Input opsi (1-3) : ')
                                if inputEditMainMenu.isdigit() == False or int(inputEditMainMenu) < 1 or int(inputEditMainMenu) > 3:
                                    print('Opsi yang dimasukkan salah')
                                    print()
                                else :
                                    break
                            if int(inputEditMainMenu) == 1:
                                while True :
                                    editSiswa = input('Input NIM mahasiswa: ')
                                    if editSiswa.isdigit() == False or cekNIM(int(editSiswa)) == False or int(str(editSiswa)[:1]) != kd :
                                        print('NIM yang dimasukkan salah')
                                        print()
                                    else :
                                        editSiswa = int(editSiswa)
                                        indexEditSiswa = cekIndexSiswa(editSiswa)
                                        print()
                                        tampilNamaNIM(indexEditSiswa)
                                        print('Daftar Nilai')
                                        tampilNilai(editSiswa)
                                        print()
                                        break
                            
                            elif int(inputEditMainMenu) == 2:
                                while True:
                                    editSiswa = input('Input NIM data siswa yang ingin diubah : ')
                                    if editSiswa.isdigit() == False or cekNIM(int(editSiswa)) == False :
                                        print('NIM yang dimasukkan salah')
                                    else :
                                        break
                                
                                editSiswa = int(editSiswa)
                                indexEditSiswa = cekIndexSiswa(editSiswa)
                                print()
                                tampilNamaNIM(indexEditSiswa)
                                print('1. Edit Nama')
                                print('2. Edit NIM')
                                print('3. Edit Nilai')
                                print('4. Kembali')
                                while True:
                                    inputEditMenu = input('Input opsi (1-4) : ')
                                    if inputEditMenu.isdigit() == False or int(inputEditMenu) < 1 or int(inputEditMenu) > 4:
                                        print('Opsi yang dimasukkan salah')
                                    else:
                                        break

                                if int(inputEditMenu) == 1 :
                                    print()
                                    tampilNamaNIM(indexEditSiswa)
                                    while True :
                                        editNama = input('Masukkan Nama Baru : ')
                                        if editNama == '':
                                            print('Nama tidak boleh kosong')
                                            print()
                                        else :
                                            break
                                    while True :
                                        inputEditData = input(f'Nama Mahasiswa {siswa[indexEditSiswa][1]} Akan Dirubah Menjadi {editNama} (Ya/Tidak)?')
                                        if inputEditData.upper() == 'YA':
                                            siswa[indexEditSiswa][1] = editNama
                                            print('Nama Mahasiswa Berhasil Diubah')
                                            print()
                                            break
                                        elif inputEditData.upper() == 'TIDAK':
                                            print()
                                            break
                                        else :
                                            print('Opsi yang dimasukkan salah')
                                            print()

                                elif int(inputEditMenu) == 2 :
                                    print()
                                    tampilNamaNIM(indexEditSiswa)
                                    while True :
                                        editNIM = input('Masukkan NIM Baru : ')
                                        if editNIM.isdigit() == False :
                                            print('NIM yang dimasukkan salah')
                                            print()
                                        elif int(str(editNIM)[:1]) != kd:
                                            print('Nomor Awal Harus Serupa dengan Kode Dosen Anda !')
                                            print()
                                        elif cekNIM(int(editNIM)) == True:
                                            print('NIM yang dimasukkan sudah terdaftar')
                                            print()
                                        elif len(editNIM) != 4:
                                            print('NIM yang dimasukkan harus 4 digit')
                                            print()
                                        else :
                                            break
                                    while True :
                                        inputEditData = input(f'NIM {siswa[indexEditSiswa][1]} {siswa[indexEditSiswa][0]} Akan Dirubah Menjadi {editNIM} (Ya/Tidak)?')
                                        if inputEditData.upper() == 'YA':
                                            siswa[indexEditSiswa][0] = int(editNIM)
                                            print('NIM Mahasiswa Berhasil Diubah')
                                            print()
                                            break
                                        elif inputEditData.upper() == 'TIDAK':
                                            print()
                                            break
                                        else :
                                            print('Opsi yang dimasukkan salah')
                                            print()

                                elif int(inputEditMenu) == 3 :
                                    print()
                                    tampilNamaNIM(indexEditSiswa)
                                    print('Daftar Nilai')
                                    tampilNilai(editSiswa)
                                    print()
                                    print('Nilai matakuliah yang akan dirubah')
                                    while True :
                                        for i in range(len(mataKuliah)):
                                            print(f'{i+1}. {mataKuliah[i]}')
                                        print(f'{len(mataKuliah)+1}. Edit Semua Nilai')
                                        print(f'{len(mataKuliah)+2}. Kembali')
                                        print()    
                                        break
                                    while True :
                                        editMatkul = input(f'Input opsi matakuliah yang ingin dirubah (1-{len(mataKuliah)+2}) : ')
                                        if editMatkul.isdigit() == False or int(editMatkul) < 1 or int(editMatkul) > len(mataKuliah)+2:
                                            print('Opsi yang dimasukkan salah')
                                        elif int(editMatkul) == len(mataKuliah)+1:
                                            editSemuaNilaiMatkul(indexEditSiswa)
                                            break
                                        elif int(editMatkul) == len(mataKuliah)+2:
                                            break
                                        else :
                                            editNilaiMatkul(int(editMatkul),indexEditSiswa)
                                            break
                            else :
                                break                    

#--------------------------------------------- MENU HAPUS ---------------------------------------------------------------------------------------------------------
                    elif int(inputWaliMenu) == 4:
                        if ListSiswaKosong(kd) == True:
                            print('Belum ada Daftar Mahasiswa')
                            print()
                            continue
                        while True:
                            if ListSiswaKosong(kd) == True:
                                print('Belum ada Daftar Mahasiswa')
                                print()
                                break
                            tampilDaftarSiswa(kd)
                            print('1. Hapus Data Mahasiswa')
                            print('2. Kembali')
                            inputHapusMenu = input('Input opsi (1-2) : ')
                            if inputHapusMenu.isdigit() == False or int(inputHapusMenu) < 1 or int(inputHapusMenu) > 2:
                                print('Opsi yang dimasukkan salah')
                                print()
                            
                            elif int(inputHapusMenu) == 1:
                                while True :
                                    HapusSiswa = input('Input NIM data mahasiswa : ')
                                    if HapusSiswa.isdigit() == False or cekNIM(int(HapusSiswa)) == False or int(str(HapusSiswa)[:1]) != kd :
                                        print('NIM yang dimasukkan salah')
                                        print()
                                    else :
                                        break
                                HapusSiswa = int(HapusSiswa)
                                indexHapusSiswa = cekIndexSiswa(HapusSiswa)
                                print()
                                tampilNamaNIM(indexHapusSiswa)
                                print('Daftar Nilai')
                                tampilNilai(HapusSiswa)
                                print()
                                print('1. Drop Data Mahasiswa')
                                print('2. Hapus Nilai Mahasiswa')
                                print('3. kembali')
                                while True:
                                    inputHapusMenu = input('Input opsi (1-3) : ')
                                    if inputHapusMenu.isdigit() == False or int(inputHapusMenu) < 1 or int(inputHapusMenu) > 3:
                                        print('Opsi yang dimasukkan salah')
                                    else:
                                        break
                                if int(inputHapusMenu) == 1 :
                                    print()
                                    tampilNamaNIM(indexHapusSiswa)
                                    verifikasiHapus(indexHapusSiswa)                                   
                                elif int(inputHapusMenu) == 2 :
                                    print()
                                    tampilNamaNIM(indexHapusSiswa)
                                    print('Daftar Nilai')
                                    tampilNilai(HapusSiswa)
                                    print('Pilih matakuliah yang akan dihapus : ')
                                    while True :
                                        for i in range(len(mataKuliah)):
                                            print(f'{i+1}. {mataKuliah[i]}')
                                        print(f'{len(mataKuliah)+1}. Hapus Semua Nilai')
                                        print(f'{len(mataKuliah)+2}. Kembali')
                                        print()    
                                        break
                                    while True :
                                        HapusMatkul = input(f'Input opsi matakuliah yang ingin dirubah (1-{len(mataKuliah)+2}) : ')
                                        if HapusMatkul.isdigit() == False or int(HapusMatkul) < 1 or int(HapusMatkul) > len(mataKuliah)+2:
                                            print('Opsi yang dimasukkan salah')
                                        elif int(HapusMatkul) == len(mataKuliah)+1:
                                            while True :
                                                verification = input('Semua Nilai dihapus apakah anda yakin (ya/tidak) : ')
                                                if verification.upper() == 'YA':
                                                    for i in range(1,len(mataKuliah)+1):
                                                        siswa[indexHapusSiswa][2][mataKuliah[i-1]] = 0
                                                    print('Data Nilai Mahasiswa Berhasil Dihapus')
                                                    print()
                                                    break
                                                elif verification.upper() == 'TIDAK':
                                                    print()
                                                    break
                                                else :
                                                    print('Opsi yang dimasukkan salah')
                                                    print()
                                            break
                                        elif int(HapusMatkul) == len(mataKuliah)+2:
                                            break
                                        else :
                                            while True :
                                                verification = input(f'Nilai {mataKuliah[int(HapusMatkul)-1]} akan dihapus apakah anda yakin (ya/tidak) : ')
                                                if verification.upper() == 'YA':
                                                    siswa[indexHapusSiswa][2][mataKuliah[int(HapusMatkul)-1]] = 0
                                                    print('Nilai Mahasiswa Berhasil Dihapus')
                                                    print()
                                                    break
                                                elif verification.upper() == 'TIDAK':
                                                    print()
                                                    break
                                                else :
                                                    print('Opsi yang dimasukkan salah')
                                                    print()
                                            break
                            else :
                                break
                    else :
                        break
                break
########################################## MENU ADMIN ############################################################  

    elif int(inputMainMenu) == 3 :
        kodeAdmin = input('Masukkan Kode Admin : ')
        if kodeAdmin != 'Admin':
            print('Kode Admin Salah')
            print()
            continue
        while True:
            print()
            print('Daftar Menu Admin')
            print('1. Lihat Data Mahasiswa')
            print('2. Lihat Data Dosen')
            print('3. Lihat Data Matakuliah')
            print('4. Tambah Data')
            print('5. Edit Data')
            print('6. Hapus Data')
            print('7. Kembali ke halaman Login')
            inputAdminMenu = input('Input opsi (1-7) : ')
            if inputAdminMenu.isdigit() == False or (int(inputAdminMenu) < 1 or int(inputAdminMenu) > 7):
                print('Opsi yang dimasukkan salah')
                print()

#--------------------------------------------- MENU TAMPIL ADMIN ---------------------------------------------------------------------------------------------------------
            elif int(inputAdminMenu) == 1:
                print()
                tampilSemuaDaftarSiswa()
                continue

            elif int(inputAdminMenu) == 2:
                print()
                tampilSemuaDaftarWali()
                continue

            elif int(inputAdminMenu) == 3:
                print()
                tampilSemuaDaftarMatakuliah()
                continue
#--------------------------------------------- MENU ADD ADMIN ---------------------------------------------------------------------------------------------------------
            elif int(inputAdminMenu) == 4:
                print()
                print('Daftar Menu Tambah')
                print('1. Tambah Mahasiswa')
                print('2. Tambah Dosen')
                print('3. Tambah Matakuliah')
                print('4. Kembali')
                inputTambahMenu = input('Input opsi (1-4) : ')
                if inputTambahMenu.isdigit() == False or (int(inputTambahMenu) < 1 or int(inputTambahMenu) > 4):
                    print('Opsi yang dimasukkan salah')
                    print()
                
                if int(inputTambahMenu) == 1:
                    while True :
                        kodeWali = input('Masukkan Kode Wali Mahasiswa : ')
                        if kodeWali.isdigit() == False :
                            print('Kode yang dimasukkan salah')
                            print()
                        elif cekKode(int(kodeWali)) == False:
                            print('Kode wali belum terdaftar')
                            print()
                        else :
                            break
                    kd = int(kodeWali)   

                    while True :
                        nimBaru = input('Masukkan NIM Mahasiswa Baru: ')
                        if nimBaru.isdigit() == False :
                            print('NIM yang dimasukkan salah')
                            print()
                        elif int(str(nimBaru)[:1]) != kd:
                            print('Nomor Awal Harus Serupa dengan Kode Dosen Anda !')
                            print()
                        elif cekNIM(int(nimBaru)) == True:
                            print('NIM yang dimasukkan sudah terdaftar')
                            print()
                        elif len(nimBaru) != 4:
                            print('NIM yang dimasukkan harus 4 digit')
                            print()
                        else :
                            break
                    namaBaru = input('Masukkan Nama : ')
                    print()
                    print('Data Baru Mahasiswa')
                    print('Nama Mahasiswa\t\t:',namaBaru.title())
                    print('NIM Mahasiswa\t\t:',nimBaru)
                    print('Kode Wali Mahasiswa\t:',kd)
                    while True:
                        inputDataBaru = input('Data Mahasiswa Akan Ditambahkan (Ya/Tidak)? ')
                        if inputDataBaru.upper() == 'YA':
                            tambahDataSiswa(namaBaru,int(nimBaru),kd)
                            print('Data Mahasiswa Berhasil Ditambah')
                            print()
                            break
                        elif inputDataBaru.upper() == 'TIDAK':
                            print()
                            break
                        else :
                            print('Opsi yang dimasukkan salah')
                            print()

                elif int(inputTambahMenu) == 2:
                    while True :
                        nimBaru = input('Masukkan Kode Wali Baru: ')
                        if nimBaru.isdigit() == False :
                            print('Kode yang dimasukkan salah')
                            print()
                        elif cekKode(int(nimBaru)) == True:
                            print('Kode sudah terdaftar')
                            print()
                        else :
                            break
                    namaBaru = input('Masukkan Nama : ')
                    print()
                    print('Data Baru Wali')
                    print('Nama Wali\t:',namaBaru.title())
                    print('Kode Wali\t:',nimBaru)
                    while True:
                        inputDataBaru = input('Data Wali Akan Ditambahkan (Ya/Tidak)? ')
                        if inputDataBaru.upper() == 'YA':
                            listWaliBaru = [int(nimBaru),namaBaru.title()]
                            wali.append(listWaliBaru)
                            print('Data Wali Berhasil Ditambah')
                            print()
                            break
                        elif inputDataBaru.upper() == 'TIDAK':
                            print()
                            break
                        else :
                            print('Opsi yang dimasukkan salah')
                            print()
                
                elif int(inputTambahMenu) == 3:
                    while True :
                        mkBaru = input('Masukkan Matakuliah Baru: ')
                        if cekMK(mkBaru.title()) == True:
                            print('Matakuliah sudah terdaftar') 
                        else :
                            break
                    print()
                    print('Data Baru Matakuliah')
                    print('Matakuliah\t:',mkBaru.title())
                    while True:
                        inputDataBaru = input('Data Matakuliah Akan Ditambahkan (Ya/Tidak)? ')
                        if inputDataBaru.upper() == 'YA':
                            mataKuliah.append(mkBaru.title())
                            for i in range(len(siswa)):
                                siswa[i][2][mkBaru.title()] = 0
                            print('Data Matakuliah Berhasil Ditambah')
                            print()
                            break
                        elif inputDataBaru.upper() == 'TIDAK':
                            print()
                            break
                        else :
                            print('Opsi yang dimasukkan salah')
                            print()

                else :
                    continue

#--------------------------------------------- MENU EDIT ADMIN ---------------------------------------------------------------------------------------------------------
            elif int(inputAdminMenu) == 5:
                while True:
                    print()
                    print('1. Edit Data Mahasiswa')
                    print('2. Edit Data Wali')
                    print('3. Edit Data Matakuliah')
                    print('4. Kembali')
                    while True:
                        inputAdminEdit = input('Input opsi (1-4) : ')
                        if inputAdminEdit.isdigit() == False or (int(inputAdminEdit) < 1 or int(inputAdminEdit) > 4):
                            print('Opsi yang dimasukkan salah')
                            print()
                        else : 
                            break
                    if int(inputAdminEdit) == 1:
                        if siswa == [] :
                            print('Data mahasiswa masih kosng')
                            continue
                        tampilSemuaDaftarSiswa()
                        while True:
                            inputNIM = input('Masukkan NIM yang akan di edit : ')
                            if inputNIM.isdigit() == False or cekNIM(int(inputNIM)) == False:
                                print('NIM tidak ditemukan')
                                print()
                            else : 
                                break
                        print()
                        inputNIM = int(inputNIM)
                        indexSiswa = cekIndexSiswa(inputNIM)
                        tampilNamaNIM(indexSiswa)
                        tampilNilai(inputNIM)
                        print('Opsi :')
                        print('1. Edit Nama')
                        print('2. Edit NIM')
                        print('3. Edit Nilai Matakuliah')
                        print('4. Kembali')
                        while True:
                            inputAdminEdit = input('Input opsi (1-4) : ')
                            if inputAdminEdit.isdigit() == False or (int(inputAdminEdit) < 1 or int(inputAdminEdit) > 4):
                                print('Opsi yang dimasukkan salah')
                                print()
                            else : 
                                break
                        if int(inputAdminEdit) == 1 :
                            print()
                            tampilNamaNIM(indexSiswa)
                            while True :
                                editNama = input('Masukkan Nama Baru : ')
                                if editNama == '':
                                    print('Nama tidak boleh kosong')
                                    print()
                                else :
                                    break
                            while True :
                                inputEditData = input(f'Nama Mahasiswa {siswa[indexSiswa][1]} Akan Dirubah Menjadi {editNama} (Ya/Tidak)?')
                                if inputEditData.upper() == 'YA':
                                    siswa[indexSiswa][1] = editNama
                                    print('Nama Mahasiswa Berhasil Diubah')
                                    print()
                                    break
                                elif inputEditData.upper() == 'TIDAK':
                                    print()
                                    break
                                else :
                                    print('Opsi yang dimasukkan salah')
                                    print()
                                    break
                        
                        elif int(inputAdminEdit) == 2 :
                            print()
                            tampilNamaNIM(indexSiswa)
                            while True :
                                editNIM = input('Masukkan NIM Baru : ')
                                noAwal = editNIM[:1]
                                if editNIM.isdigit() == False :
                                    print('NIM yang dimasukkan salah')
                                    print()
                                elif int(str(inputNIM)[:1]) != int(noAwal):
                                    print('Nomor Awal Harus Serupa !')
                                    print()
                                elif cekNIM(int(editNIM)) == True:
                                    print('NIM yang dimasukkan sudah terdaftar')
                                    print()
                                elif len(editNIM) != 4:
                                    print('NIM yang dimasukkan harus 4 digit')
                                    print()
                                else :
                                    break
                            while True :
                                inputEditData = input(f'NIM {siswa[indexSiswa][1]} {siswa[indexSiswa][0]} Akan Dirubah Menjadi {editNIM} (Ya/Tidak)? ')
                                if inputEditData.upper() == 'YA':
                                    siswa[indexSiswa][0] = int(editNIM)
                                    print('NIM Mahasiswa Berhasil Diubah')
                                    print()
                                    break
                                elif inputEditData.upper() == 'TIDAK':
                                    print()
                                    break
                                else :
                                    print('Opsi yang dimasukkan salah')
                                    print()

                        elif int(inputAdminEdit) == 3 :
                            print()
                            tampilNamaNIM(indexSiswa)
                            print('Daftar Nilai')
                            tampilNilai(inputNIM)
                            print()
                            print('Nilai matakuliah yang akan dirubah')
                            while True :
                                for i in range(len(mataKuliah)):
                                    print(f'{i+1}. {mataKuliah[i]}')
                                print(f'{len(mataKuliah)+1}. Edit Semua Nilai')
                                print(f'{len(mataKuliah)+2}. Kembali')
                                print()    
                                break
                            while True :
                                editMatkul = input(f'Input opsi matakuliah yang ingin dirubah (1-{len(mataKuliah)+2}) : ')
                                if editMatkul.isdigit() == False or int(editMatkul) < 1 or int(editMatkul) > len(mataKuliah)+2:
                                    print('Opsi yang dimasukkan salah')
                                elif int(editMatkul) == len(mataKuliah)+1:
                                    editSemuaNilaiMatkul(indexSiswa)
                                    # for i in range(1,len(mataKuliah)+1):
                                    #     editNilaiMatkul(i-1,indexSiswa)
                                    break
                                elif int(editMatkul) == len(mataKuliah)+2:
                                    break
                                else :
                                    editNilaiMatkul(int(editMatkul),indexSiswa)
                                    break
                        else :
                                break
                    
                    elif int(inputAdminEdit) == 2:
                        tampilSemuaDaftarWali()
                        print()
                        print('1. Edit Nama')
                        print('2. Edit Kode Wali')
                        print('3. Kembali')
                        while True:
                            inputWaliEdit = input('Input opsi (1-3) : ')
                            if inputWaliEdit.isdigit() == False or (int(inputWaliEdit) < 1 or int(inputWaliEdit) > 3):
                                print('Opsi yang dimasukkan salah')
                                print()
                            else : 
                                break
                        if int(inputWaliEdit) == 1:
                            while True :
                                inputKodeWali = input('Input Kode Wali : ')
                                if inputKodeWali.isdigit() == False or cekKode(int(inputKodeWali)) == False:
                                    print('Kode yang dimasukkan salah')
                                    print()
                                else :
                                    break
                            inputNamaWali = input('Input Nama Baru Wali : ')
                            indexWali = cekIndexWali(int(inputKodeWali))
                            while True :
                                inputEditData = input(f'Nama Wali {wali[indexWali][1]} Akan Dirubah Menjadi {inputNamaWali} (Ya/Tidak)?')
                                if inputEditData.upper() == 'YA':
                                    wali[indexWali][1] = inputNamaWali
                                    print('Nama Wali Berhasil Diubah')
                                    print()
                                    break
                                elif inputEditData.upper() == 'TIDAK':
                                    print()
                                    break
                                else :
                                    print('Opsi yang dimasukkan salah')
                                    print()

                        elif int(inputWaliEdit) == 2:
                            while True :
                                inputKodeWali = input('Input Kode Wali : ')
                                if inputKodeWali.isdigit() == False or cekKode(int(inputKodeWali)) == False:
                                    print('Kode yang dimasukkan salah')
                                    print()
                                else :
                                    break
                            kd = int(inputKodeWali)
                            indexWali = cekIndexWali(kd)
                            while True :
                                inputKodeWali = input('Input Kode Baru Wali : ')
                                if inputKodeWali.isdigit() == False:
                                    print('Format kode yang dimasukkan salah')
                                    print()
                                elif int(inputKodeWali) < 1:
                                    print('Kode tidak boleh lebih kecil dari 1')
                                    print()
                                elif cekKode(int(inputKodeWali)) == True:
                                    print('Kode wali sudah terdaftar')
                                    print()
                                else :
                                    break
                            while True :
                                inputEditData = input(f'Kode Wali {wali[indexWali][1]} (Kode {wali[indexWali][0]}) Akan Dirubah Menjadi {inputKodeWali} (Ya/Tidak)?')
                                originalKode = wali[indexWali][0]
                                if inputEditData.upper() == 'YA':
                                    wali[indexWali][0] = inputKodeWali
                                    if cekBanyakSiswa(int(inputKodeWali)) != 0:
                                        for i in range(len(siswa)):
                                            if siswa[i][3] == originalKode:
                                                siswa[i][3] = int(inputKodeWali)
                                                temp = inputKodeWali+str(siswa[i][0])[:1]
                                                siswa[i][0] = int(temp)

                                    print('Kode Wali Berhasil Diubah')
                                    print()
                                    break
                                elif inputEditData.upper() == 'TIDAK':
                                    print()
                                    break
                                else :
                                    print('Opsi yang dimasukkan salah')
                                    print()
                    
                    elif int(inputAdminEdit) == 3:
                        print()
                        tampilSemuaDaftarMatakuliah()
                        print('Opsi :')
                        print('1. Edit Nama Matakuliah')
                        print('2. Kembali')
                        while True:
                            inputAdminEdit = input('Input opsi (1-2) : ')
                            if inputAdminEdit.isdigit() == False or (int(inputAdminEdit) < 1 or int(inputAdminEdit) > 2):
                                print('Opsi yang dimasukkan salah')
                                print()
                            else : 
                                break
                        if int(inputAdminEdit) == 1:
                            print()
                            print('Daftar Matakuliah')
                            for i in range(len(mataKuliah)):
                                print(f'{i+1}. {mataKuliah[i]}')
                            while True:
                                EditMatkul = input('Input index matakuliah yang akan di ubah : ')
                                if (int(EditMatkul) < 1 or int(EditMatkul) > len(mataKuliah)) or EditMatkul.isdigit() == False :
                                    print('Kode yang dimasukkan salah')
                                    print()
                                else :
                                    break
                            namaBaru = input('Masukkan nama baru matakuliah : ')
                            while True :
                                inputEditData = input(f'Nama Matakuliah {mataKuliah[int(EditMatkul)-1]} Akan Dirubah Menjadi {namaBaru} (Ya/Tidak)?')
                                if inputEditData.upper() == 'YA':
                                    for i in range(len(siswa)):
                                        siswa[i][2][namaBaru] = siswa[i][2].pop(mataKuliah[int(EditMatkul)-1])
                                    mataKuliah[int(EditMatkul)-1] = namaBaru
                                    print('Nama Matakuliah Berhasil Diubah')
                                    print()
                                    break
                                elif inputEditData.upper() == 'TIDAK':
                                    print()
                                    break
                                else :
                                    print('Opsi yang dimasukkan salah')
                                    print()
                    else :
                        break

#--------------------------------------------- MENU HAPUS HAPUS ---------------------------------------------------------------------------------------------------------
            elif int(inputAdminMenu) == 6:
                while True:
                    print()
                    print('1. Hapus Data Mahasiswa')
                    print('2. Hapus Data Dosen')
                    print('3. Hapus Data Matakuliah')
                    print('4. Kembali')
                    while True:
                        inputAdminHapus = input('Input opsi (1-4) : ')
                        if inputAdminHapus.isdigit() == False or (int(inputAdminHapus) < 1 or int(inputAdminHapus) > 4):
                            print('Opsi yang dimasukkan salah')
                            print()
                        else : 
                            break
                    if int(inputAdminHapus) == 1:
                        if siswa == [] :
                            print('Data mahasiswa masih kosng')
                            continue
                        print()
                        tampilSemuaDaftarSiswa()
                        print('1. Hapus Data Mahasiswa')
                        print('2. Hapus Semua Data Mahasiswa Berdasarkan Kode Wali')
                        print('3. Hapus Semua Data Mahasiswa ')
                        print('4. Kembali ')
                        while True:
                            inputAdminEdit1 = input('Input opsi (1-4) : ')
                            if inputAdminEdit1.isdigit() == False or (int(inputAdminEdit1) < 1 or int(inputAdminEdit1) > 4):
                                print('Opsi yang dimasukkan salah')
                                print()
                            else : 
                                break
                        if int(inputAdminEdit1) == 1:
                            while True:
                                HapusSiswa = input('Input NIM data mahasiswa : ')
                                if cekNIM(int(HapusSiswa)) == False or HapusSiswa.isdigit() == False :
                                    print('NIM yang dimasukkan salah')
                                    print()
                                else :
                                    break
                            HapusSiswa = int(HapusSiswa)
                            indexHapusSiswa = cekIndexSiswa(HapusSiswa)
                            print()
                            tampilNamaNIM(indexHapusSiswa)
                            print('Daftar Nilai')
                            tampilNilai(HapusSiswa)
                            verifikasiHapus(indexHapusSiswa)

                        elif int(inputAdminEdit1) == 2:
                            while True:
                                kd = input('Input kode wali : ')
                                if cekKode(int(kd)) == False or kd.isdigit() == False :
                                    print('Kode wali yang dimasukkan salah')
                                    print()
                                else :
                                    break
                            kd = int(kd)
                            print()
                            tampilDaftarSiswa(kd)
                            while True :
                                verification = input('Akan dihapus apakah anda yakin (ya/tidak) : ')
                                if verification.upper() == 'YA':
                                    siswa = hapusSiswaKode(kd)
                                    print('Data Berhasil Dihapus')
                                    print()
                                    break
                                elif verification.upper() == 'TIDAK':
                                    print()
                                    break
                                else :
                                    print('Opsi yang dimasukkan salah')
                                    print()
                        elif int(inputAdminEdit1) == 3:
                            tampilSemuaDaftarSiswa()
                            while True :
                                verification = input('Akan dihapus apakah anda yakin (ya/tidak) : ')
                                if verification.upper() == 'YA':
                                    siswa.clear()
                                    print('Data Berhasil Dihapus')
                                    print()
                                    break
                                elif verification.upper() == 'TIDAK':
                                    print()
                                    break
                                else :
                                    print('Opsi yang dimasukkan salah')
                                    print()
                        else :
                            break

                    if int(inputAdminHapus) == 2:
                        if wali == []  :
                                print('Data mahasiswa masih kosng')
                                break
                        print()
                        tampilSemuaDaftarWali()
                        print('1. Hapus Data Wali')
                        print('2. Hapus Semua Data Wali ')
                        print('3. Kembali ')
                        while True:
                            inputAdminHapus1 = input('Input opsi (1-3) : ')
                            if inputAdminHapus1.isdigit() == False or (int(inputAdminHapus1) < 1 or int(inputAdminHapus1) > 3):
                                print('Opsi yang dimasukkan salah')
                                print()
                            else : 
                                break
                        if int(inputAdminHapus1) == 1:
                            while True:
                                HapusWali = input('Input kode wali : ')
                                if cekKode(int(HapusWali)) == False or HapusWali.isdigit() == False :
                                    print('Kode yang dimasukkan salah')
                                    print()
                                else :
                                    break
                            HapusWali = int(HapusWali)
                            indexHapusWali = cekIndexWali(HapusWali)
                            print()
                            tampilWaliIndex(indexHapusWali)
                            verifikasiHapusWali(indexHapusWali)
                        
                        elif int(inputAdminHapus1) == 2:
                            tampilSemuaDaftarWali()
                            while True :
                                verification = input('Akan dihapus apakah anda yakin (ya/tidak) : ')
                                if verification.upper() == 'YA':
                                    wali.clear()
                                    for i in range(len(siswa)):
                                        siswa[i][3] = 0
                                    print('Data Berhasil Dihapus')
                                    print()
                                    break
                                elif verification.upper() == 'TIDAK':
                                    print()
                                    break
                                else :
                                    print('Opsi yang dimasukkan salah')
                                    print()
                        else :
                            print()
                            break

                    if int(inputAdminHapus) == 3:
                        if len(mataKuliah) == 1  :
                            print('Data Matakuliah Tidak Boleh Kosong!')
                            continue
                        print()
                        tampilSemuaDaftarMatakuliah()
                        print()
                        print('Opsi :')
                        print('1. Hapus Data Matakuliah')
                        print('2. Kembali ')
                        while True:
                            inputAdminHapus1 = input('Input opsi (1-2) : ')
                            if inputAdminHapus1.isdigit() == False or (int(inputAdminHapus1) < 1 or int(inputAdminHapus1) > 2):
                                print('Opsi yang dimasukkan salah')
                                print()
                            else : 
                                break
                        if int(inputAdminHapus1) == 1:
                            print()
                            print('Daftar Matakuliah')
                            for i in range(len(mataKuliah)):
                                print(f'{i+1}. {mataKuliah[i]}')
                            while True:
                                HapusMatkul = input('Input index matakuliah : ')
                                if (int(HapusMatkul) < 1 or int(HapusMatkul) > len(mataKuliah)) or HapusMatkul.isdigit() == False :
                                    print('Kode yang dimasukkan salah')
                                    print()
                                else :
                                    break
                            HapusMatkul = int(HapusMatkul)-1
                            print()
                            verifikasiHapusMatakuliah(HapusMatkul)
                        else :
                            print()
                            break
                    else:
                        print()
                        break 
                continue
            else:
                break
    else:
        break


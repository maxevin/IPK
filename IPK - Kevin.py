data_mahasiswa = []

def tampilkan_daftar(data_mahasiswa):
    print('Daftar Mahasiswa dari Universitas ABC')
    print('NIM     | Nama      | Alamat       | Asal Sekolah      | Kode Prodi    | Nilai IPK Awal  | Nilai UTS  | Nilai IPS | IPK Akhir | Beasiswa')
    for i in range(len(data_mahasiswa)):
        data = str(i) + (' ') * 10 + data_mahasiswa[i][0] + (' ') * 10 + data_mahasiswa[i][1] + (' ') * 10 + data_mahasiswa[i][2] + (' ') * 10 + data_mahasiswa[i][3] + (' ') * 15 + str(data_mahasiswa[i][4]) + (' ') * 10 + str(data_mahasiswa[i][5]) + (' ') * 10 + str(data_mahasiswa[i][6]) + (' ') * 10 + str(data_mahasiswa[i][7]) + (' ') * 10 + str(data_mahasiswa[i][8]) + (' ')
        print(data)

def beasiswa(kode_prodi,ipk_akhir):
    if kode_prodi == 'TI' or kode_prodi == 'SI':
        if 75<ipk_akhir<85:
            print('Beasiswa 20%')
        elif 85<ipk_akhir<100:
            print('Beasiswa 30%')
        else:
            print('tidak dapat beasiswa')
    elif kode_prodi == 'DKV' or kode_prodi == 'Teknik Industri':
        if 75<ipk_akhir<85:
            print('Beasiswa 25%')
        elif 85<ipk_akhir<100:
            print('Beasiswa 35%')
        else:
            print('tidak dapat beasiswa')
    



nama = input('Nama : ')
alamat = input('Alamat : ')
asal_sekolah = input('Asal Sekolah : ')
kode_prodi = input('Kode Prodi : ')
ipk_awal = int(input('Nilai IPK Awal : '))
nilai_uts = int(input('Nilai UTS : '))
nilai_uas = int(input('Nilai UAS : '))
nilai_tm = int(input('Nilai TM : '))
nilai_ips = (0.3 * nilai_uts) + (0.3 * nilai_tm) + (0.4 * nilai_uas)
ipk_akhir = (ipk_awal+nilai_ips)/2

data_mahasiswa.append([nama,alamat,asal_sekolah,kode_prodi,ipk_awal,nilai_uts,nilai_ips,ipk_akhir,beasiswa(kode_prodi,ipk_akhir)])

tampilkan_daftar(data_mahasiswa)
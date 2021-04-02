#Program untuk menyapa pengunjung
#input nama dan jenis kelamin
nama = input('Masukan nama anda: ')
jeniskelamin = str(input('Masukan jenis kelamin anda (l/p): '))
jeniskelamin = jeniskelamin.lower()
#memeriksa jenis kelamin
if jeniskelamin == 'l':
    print('Selamat datang, Tuan',nama,'!')
else:
    print('Selamat datang, Nyonya',nama,'!')

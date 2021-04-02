#Program Grading Nilai
#input nama dan nilai
nama = str(input('Siapa nama anda: '))
nilai = float(input('Masukan nilai anda: '))
#memproses nilai
if nilai > 100 :
    print('Nilai tidak valid')
elif nilai >= 85 :
    print('Hallo, ',nama,'! Nilai anda setelah dikonversi adalah A')
elif nilai >= 80 :
    print('Hallo, ', nama, '! Nilai anda setelah dikonversi adalah A-')
elif nilai >= 75:
    print('Hallo, ', nama, '! Nilai anda setelah dikonversi adalah B+')
elif nilai >= 70:
    print('Hallo, ', nama, '! Nilai anda setelah dikonversi adalah B')
elif nilai >= 65:
    print('Hallo, ', nama, '! Nilai anda setelah dikonversi adalah C+')
elif nilai >= 60:
    print('Hallo, ', nama, '! Nilai anda setelah dikonversi adalah C')
else:
    print('Hallo, ', nama, '! Nilai anda setelah dikonversi adalah E')
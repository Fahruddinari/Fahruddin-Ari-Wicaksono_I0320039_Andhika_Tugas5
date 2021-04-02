#penggunaan if untuk tiga kasus dan selebihnya
#input bilangan
print('Masukan koordinat!')
x = int(input('Masukan nilai x: '))
y = int(input('Masukan nilai y: '))
info = 'Koordinat (' + str(x) + ',' + str(y) + ') berada pada kaudran'
#memriksa nilai x dan y
if x > 0 and y > 0:
    print(info + 'I')
elif x < 0 and y > 0:
    print(info + 'II')
elif x < 0 and y < 0:
    print(info + 'III')
elif x > 0 and y < 0:
    print(info + 'IV')
else:
    pass
print()

# BIODATA

### Nama = Lola Seftyliani
### Kelas = TI.24.A.4
### NIM = 312410339

# Program Bilangan Terbesar

Program ini adalah sebuah aplikasi sederhana untuk menentukan bilangan terbesar dari sejumlah input yang diberikan oleh pengguna. Program akan terus meminta pengguna untuk memasukkan bilangan sampai pengguna memasukkan angka `0`. Ketika angka `0` dimasukkan, program akan berhenti dan menampilkan bilangan terbesar yang telah dimasukkan.

## Fitur

- Menentukan bilangan terbesar dari sejumlah input bilangan
- Menghentikan program ketika pengguna memasukkan angka `0`
- Memberikan notifikasi jika tidak ada bilangan yang dimasukkan (selain `0`)

## Cara Menggunakan

1. Jalankan program dengan interpreter Python.
2. Masukkan bilangan satu per satu ketika diminta.
3. Untuk menghentikan input, masukkan angka `0`.
4. Program akan menampilkan bilangan terbesar yang dimasukkan sebelum angka `0`.

## Contoh Penggunaan

```python
bilangan_terbesar = float('-inf')  

while True:
    bilangan = float(input("Masukkan bilangan (tekan 0 untuk berhenti): "))
    if bilangan == 0:
        break   
    if bilangan > bilangan_terbesar:
        bilangan_terbesar = bilangan

if bilangan_terbesar == float('-inf'):
    print("Tidak ada bilangan yang dimasukkan.")
else:
    print("Bilangan terbesar adalah:", bilangan_terbesar)
```



```
Masukkan bilangan (tekan 0 untuk berhenti): 90
Masukkan bilangan (tekan 0 untuk berhenti): 87
Masukkan bilangan (tekan 0 untuk berhenti): 23
Masukkan bilangan (tekan 0 untuk berhenti): 0
Bilangan terbesar adalah: 90.0

```
## BERIKUTADALAH HASIL SCREENSHOT NYA

![Screenshot 2024-10-20 162252](https://github.com/user-attachments/assets/f5b6797a-d2a6-4bac-a9e5-bf8c4455bfb5)

## BERIKU ADALAH FLOWCHARTNYA

![2 flowchart](https://github.com/user-attachments/assets/0d3b77d8-ba0b-4a8c-9332-4aac227404e7)


## Prasyarat

- Python 3.x harus sudah terinstal di sistem.

## Cara Menjalankan

1. Pastikan Python sudah terinstal di komputer Anda.
2. Simpan kode program dalam file bernama `pemrograman.py`.
3. Buka terminal atau command prompt.
4. Jalankan program dengan perintah berikut:

   ```bash
   python pemrograman.py
   ```

   # menetukan 3 bilangan terbesar

Program ini digunakan untuk menemukan bilangan terbesar dari tiga bilangan yang dimasukkan oleh pengguna. Program meminta tiga bilangan sebagai input, membandingkannya, dan kemudian mencetak bilangan terbesar di antara ketiga bilangan tersebut.

## Kode Program

```python
a = int(input('Masukkan bilangan pertama: '))
b = int(input('Masukkan bilangan kedua: '))
c = int(input('Masukkan bilangan ketiga: '))

if a > b and a > c:
    print(f'Bilangan terbesar adalah {a}')
elif b > a and b > c:
    print(f'Bilangan terbesar adalah {b}')
else:
    print(f'Bilangan terbesar adalah {c}')
```

# Hasil screenshot di visualstudiocode

![Screenshot 2024-10-20 174553](https://github.com/user-attachments/assets/63169e87-0b98-4131-9d33-a4444268665c)


# Berikut adalah flowchartnya

![Screenshot 2024-10-20 172359](https://github.com/user-attachments/assets/cfc0194a-265d-41ab-8fd8-d184f3056b9d)

## Penjelasan Kode

1. *Input Bilangan:*
   Program meminta pengguna memasukkan tiga bilangan menggunakan fungsi input() dan mengonversinya menjadi bilangan bulat (int), kemudian disimpan ke variabel a, b, dan c.

2. *Logika Penentuan Bilangan Terbesar:*
   - Program menggunakan struktur kondisi if-elif-else untuk membandingkan ketiga bilangan.
   - Jika a lebih besar dari b dan c, program akan mencetak bahwa a adalah bilangan terbesar.
   - Jika b lebih besar dari a dan c, program akan mencetak bahwa b adalah bilangan terbesar.
   - Jika tidak ada kondisi di atas yang terpenuhi, program akan menganggap bahwa c adalah bilangan terbesar dan mencetaknya.

3. *Output:*
   Program akan mencetak bilangan terbesar yang ditemukan di antara ketiga bilangan yang diinputkan oleh pengguna.

## Contoh Eksekusi Program

### Contoh 1:
Pengguna memasukkan tiga bilangan, yaitu 10, 20, dan 15.


Masukkan bilangan pertama: 10
Masukkan bilangan kedua: 20
Masukkan bilangan ketiga: 15
Bilangan terbesar adalah 20


### Contoh 2:
Pengguna memasukkan tiga bilangan, yaitu 45, 35, dan 50.


Masukkan bilangan pertama: 45
Masukkan bilangan kedua: 35
Masukkan bilangan ketiga: 50
Bilangan terbesar adalah 50

![Screenshot 2024-10-19 095852](https://github.com/user-attachments/assets/18c4eb26-8df1-45df-afb3-dee64f83a5f9)
## PRAKTIKUM 3

# LATIHAN 1

<img width="712" alt="image" src="https://github.com/user-attachments/assets/1447f1ff-cdc7-42cd-a86c-90956cac26f5">
<p># PEMBAHSAN MENGENAI:</p>
<p># PENGGUNAAN END</p>
<p># PENGGUNAAN SEREPATOR</p>
<p># STRING FORMAT</p>

## PENGGUNAAN END
<img width="286" alt="image" src="https://github.com/user-attachments/assets/6d7f5c02-fa7a-46bf-97b4-1bf8f3a45e90">

```python
print('A', end='')
print('b', end='')
print('c', end='')
print()
print('x')
print('y')
print('z')
````

Parameter end dalam fungsi `Print ()` di python di gunakan untuk menambahkan string(" ")apapun diakhir dan mengeluarkan pertanyaan print

```python
print()
````

Secara default,fungsi `print()` akan mengakhiri dengan baris baru,dan akan secara otomatis karakter baris baru di akhir outputnya

inilah hasil program tersebut:

![Screenshot 2024-10-19 105401](https://github.com/user-attachments/assets/e4be0ae6-0c1e-46ab-a947-1470668b5387)

dan ini hasil tanpa menggunakan fungsi `print()` di tengah pada kode program di atas:

![Screenshot 2024-10-19 105727](https://github.com/user-attachments/assets/ce8c4426-642e-4460-b59e-31b88d4bd59b)

## PENGGUNAAN SEREPATOR

![Screenshot 2024-10-19 105946](https://github.com/user-attachments/assets/f883e3f9-751b-4be6-973a-a1720cf8d062)

```python
w, x, y, z, =10, 15, 20, 25
print(w, x, y, z,)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='-----')
````
pada python penggunaan serepator dapat menggunakan fungsi `split()` atau `sep` yang seperti dalam kode program di atas

serepator ini menentukan pembatasan yang digunakan untuk memisahkan sting,serepator dapat berupa karakter tunggal atau beberapa karakter.jika tidak ditentukan,maka python akan menggunakan spasi sebagai pemisah.

Berikut Hasil Kode Program Diatas:

![Screenshot 2024-10-19 111502](https://github.com/user-attachments/assets/9afa0286-fcd8-437e-8319-0da6019ef34e)

```python
w, x, y, z, =10, 15, 20, 25
````
Variable yang seperti ini menentukan parameter,jadi variable ini tidak bisa memasukan variable angka yang sudah ditentukan w = 10,x=15,y=20,z=25

```python
print(w, x, y, z,)
````

Fungsi ini hanya mencetak saja yang menggunakan fungsi `print()`, tetapi di karenakan mencetak parameter,koma tersebut di hilangkan

```python
print(w, x, y, z, sep=',')
````
karena pemisahnya dihilangkan,kita menggunakan fungsi `sep`atau`split()`dan kita memasukkan pemisahnya didalam string akan memunculkan cetakan yang sesuai keinginan anda dalam memisahkan sesuatu parameter

## STRING FORMAT

![Screenshot 2024-10-19 112724](https://github.com/user-attachments/assets/d5f2d127-76c0-4653-996c-aa5e6d201274)

```python
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**6)
print(7, 10**7)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))
````
String Format adalah proses memasukan variable atau string kustom ke dalam teks yang sudah ditentukan,dan dapat digunakan untuk berbagai keperluan,seperti memasukan judul dalam grafik,menampilkan pesan atau kesalahan, atau meneruskan kesalahan ke suatu fungsi 

```python
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**5)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)
````

Nilai pertama dalam setiap pasangan adalah angka dari 0 hingga 10, kode program ini dihitung dengan menggunakan operasi pangkat atau fungsinya `(**)` untuk menaikkan 10 ke pangkat yang sesuai dengan angka pertama, yang bisa di bahasa manusiakan variable 0 = 10 pangkat 0, variable 1 10 pangkat 1 dan seterusnya hingga variable 10 yaitu 10 pangkat 10, dan di cetak dengan fungsi `print()`

```python
print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))
````

Kode ini mencetak 11 baris dengan format `{0:3}` `{1:16}` yang di gunakan untuk mengatur format string

Pada string pertama, angka `0` di format untuk memeliki lebar 3 karakter atau yang bisa disebut 3 kali spasi dengan perataan kanan.

angka 1 diformat untuk memiliki lebar 16 Karakter atau 16 kali spasi dengan perataan kanan, dan masing-masing mencetak nilai seperti format di atas dengan fungsi `print()`

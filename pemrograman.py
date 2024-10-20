# Inisialisasi variabel untuk menyimpan bilangan terbesar
bilangan_terbesar = float('-inf')  # Inisialisasi dengan nilai terkecil

while True:
    bilangan = float(input("Masukkan bilangan (tekan 0 untuk berhenti): "))
    if bilangan == 0:
        break  # Keluar dari loop jika input 0
    if bilangan > bilangan_terbesar:
        bilangan_terbesar = bilangan

# Memeriksa apakah ada bilangan yang dimasukkan
if bilangan_terbesar == float('-inf'):
    print("Tidak ada bilangan yang dimasukkan.")
else:
    print("Bilangan terbesar adalah:", bilangan_terbesar)


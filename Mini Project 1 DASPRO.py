nama =  input("Masukkan Nama: ")
nim =   input("Masukkan NIM: ")
kelas = input("Masukkan Kelas: ")

print("\nSelamat anda telah berhasil login,", nama)
print("NIM: ", nim)
print("Kelas: ",kelas) 

def hitung_total_harga():
    while True:
        # Input harga barang dan jumlah pembelian
        harga_barang = float(input("Masukkan harga barang: Rp"))
        jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))

        # Menghitung total harga
        total_harga = harga_barang * jumlah_pembelian
        print(f"Total harga sebelum diskon: Rp{total_harga}")

        # Cek apakah total harga lebih dari Rp250.000
        if total_harga > 250000:
            diskon = total_harga * 0.25
            total_harga -= diskon
            print(f"Diskon 25%: Rp{diskon}")
        else:
            print("Tidak ada diskon.")

        # Menampilkan total harga setelah diskon
        print(f"Total harga setelah diskon: Rp{total_harga:.2f}")

        # Menanyakan apakah pengguna ingin menghitung lagi
        pilihan = input("Apakah Anda ingin menghitung total harga lagi? (ya/tidak): ").strip().lower()
        if pilihan != 'ya':
            print("Terima kasih! Program selesai.")
            break

# Memanggil fungsi
hitung_total_harga()
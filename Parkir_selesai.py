import datetime
import math

waktu = []
kendaraan_masuk = {}
tarif_per_detik = 10000  # Tarif parkir per 60 detik
denda_4_menit = 0.1
denda_6_menit = 0.25
pin_admin_parkir = "1234"

def input_pin():
    pin_input = input("Masukkan PIN Admin Parkir: ")
    if pin_input == pin_admin_parkir:
        print("Menu Admin Parkir:")
        print("1. Riwayat Transaksi Parkir")
        print("2. Kembali ke Menu Utama")
        print("3. Exit")
        # Tambahkan menu admin lainnya di sini
        pilihan_admin = input("Pilih menu admin (1/2/3): ")
        if pilihan_admin == "1":
            tampilkan_kendaraan_masuk()
        elif pilihan_admin == "2":
             menu_utama()
        elif pilihan_admin == "3":
            print("\nSEE YOU!!")
            exit()
    else:
        print("PIN Admin Parkir salah.")

def kendaraan_masuk_area_parkir():
    nomor_kendaraan = input("Masukkan nomor/plat kendaraan: ")
    waktu_masuk = datetime.datetime.now()
    kendaraan_masuk[nomor_kendaraan] = {'waktu_masuk': waktu_masuk}
    print("Waktu masuk :", waktu_masuk)
    print("Gerbang masuk terbuka. Silahkan masuk.")

def kendaraan_keluar_area_parkir():
    nomor_kendaraan = input("Masukkan nomor/plat kendaraan: ")

    if nomor_kendaraan not in kendaraan_masuk:
        print("Error: Kendaraan tidak terdaftar dalam area parkir.")
        return

    waktu_keluar = datetime.datetime.now()
    waktu_masuk = kendaraan_masuk[nomor_kendaraan]['waktu_masuk']
    durasi_parkir = (waktu_keluar - waktu_masuk).total_seconds()

    if(durasi_parkir<60):
        durasi_parkir = 60
    else:
    # Pembulatan waktu parkir ke kelipatan 60 detik
        durasi_parkir = math.ceil(durasi_parkir / 60) * 60
    biaya_parkir = (durasi_parkir / 60) * tarif_per_detik

    if durasi_parkir >= 240:
        denda = biaya_parkir * denda_4_menit
        if durasi_parkir >= 360:
            denda = biaya_parkir * denda_6_menit
        biaya_parkir += denda

    print(f"Biaya parkir untuk kendaraan dengan nomor {nomor_kendaraan}: Rp {int(biaya_parkir)}")

    nominal_pembayaran = int(input("Masukkan nominal pembayaran: "))

    if nominal_pembayaran >= biaya_parkir:
        print("Terima Kasih. Gerbang keluar terbuka.")
        if nominal_pembayaran > biaya_parkir:
            kembalian = nominal_pembayaran - biaya_parkir
            print (f"Kembalian RP {kembalian}")
        else:
            pass
        del kendaraan_masuk[nomor_kendaraan]

        # Menambahkan informasi transaksi ke riwayat
        waktu.append({
            'nomor_kendaraan': nomor_kendaraan,
            'waktu_masuk': waktu_masuk,
            'waktu_keluar': waktu_keluar,
            'durasi_parkir': durasi_parkir,
            'biaya_parkir': biaya_parkir,
            'nominal_pembayaran': nominal_pembayaran,
            'kembalian': kembalian
        })

    else:
        print("Pembayaran kurang. Silahkan melakukan pembayaran yang cukup.")


def tampilkan_kendaraan_masuk():
    print("\n===== Riwayat Transaksi Parkir =====")
    for transaksi in waktu:
        print(f"Nomor Kendaraan: {transaksi['nomor_kendaraan']}")
        print(f"Waktu Masuk: {transaksi['waktu_masuk']}")
        print(f"Waktu Keluar: {transaksi['waktu_keluar']}")
        print(f"Durasi Parkir: {transaksi['durasi_parkir']} detik")
        print(f"Biaya Parkir: Rp {int(transaksi['biaya_parkir'])}")
        print(f"Nominal Pembayaran: Rp {transaksi['nominal_pembayaran']}")
        print(f"Kembalian: Rp {transaksi['kembalian']}")
        print("=" * 30)


def menu_utama():
    while True:
        print("\n=== MENU PARKIR ===")
        print("1. Masuk area parkir")
        print("2. Keluar area parkir")
        print("3. Admin parkir")
        pilih_menu = int(input("Pilih menu parkir (1/2/3): "))

        if pilih_menu == 1:
            kendaraan_masuk_area_parkir()

        elif pilih_menu == 2:
            kendaraan_keluar_area_parkir()

        elif pilih_menu == 3:
             input_pin()

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

while True:
    Pilih = int(input("\nApakah Anda Ingin Memulai Program Parkir? \n\n1.Ya\n2.Tidak\n\npilih Dulu ya!: "))
    if (Pilih == 1):
        menu_utama()
    elif (Pilih == 2):
        print ("\nSEE YOU!!")
        break
    else:
        print ("\nPilihan Tidak Ada Ya Silahkan Cek Lagi")

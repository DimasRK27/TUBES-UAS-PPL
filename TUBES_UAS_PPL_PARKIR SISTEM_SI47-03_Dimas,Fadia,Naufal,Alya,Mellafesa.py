import datetime
import math

waktu = []
kendaraan_masuk = {}
tarif_per_detik = 10000  #Tarif parkir per 60 detik
denda_4_menit = 0.1 #Inisialisasi Denda 4 Menit
denda_6_menit = 0.25 #Inisialisasi Denda 6 Menit
pin_admin_parkir = 1234 #PIN Admin
kembalian = 0  #Inisialisasi kembalian 

#Fungsi Untuk Menu Admin
def input_pin():
    while True:
        try:
            #Tampilan Utama Menu Admin
            pin_input = int(input("Masukkan PIN Admin Parkir: "))
            if pin_input != pin_admin_parkir:
                raise ValueError("PIN Admin Parkir salah.",)
            
            else:
                print("Menu Admin Parkir:")
                print("1. List Data Kendaraan")
                print("2. Riwayat Transaksi Parkir")
                print("3. Kembali ke Menu Utama")
                print("4. Exit")

                #Percabangan Pemilihan Pada Menu Admin
                pilihan_admin = int(input("Pilih menu admin (1/2/3/4): "))
                if pilihan_admin == 1:
                    list_kendaraan()
                elif pilihan_admin == 2:
                    tampilkan_kendaraan_masuk()
                elif pilihan_admin == 3:
                    menu_utama()
                elif pilihan_admin == 4:
                    print("\nSEE YOU!!")
                    exit()
                else:
                    print("Pilih menu yang ada!")
                break  
        except ValueError as e:
            print(f"Error: {e}")

#Fungsi Untuk List Kendaraan Di Menu Admin
def list_kendaraan():
     for i, (nomor_kendaraan, data_kendaraan) in enumerate(kendaraan_masuk.items(), start=1):
        waktu_masuk = data_kendaraan['waktu_masuk']
        print(f"{i}. Nomor Plat: {nomor_kendaraan} | Waktu Masuk: {waktu_masuk}")

#Fungsi Untuk Kendaraan Masuk
def kendaraan_masuk_area_parkir():
    while True:
        nomor_kendaraan = input("Masukkan nomor/plat kendaraan: ")

        #Pengecekan Nomer Plat Apakah Sesuai
        if len(nomor_kendaraan) > 8:
            print("Error: Nomor plat kendaraan tidak boleh lebih dari 8 karakter. Silahkan coba lagi.")
        else:
            waktu_masuk = datetime.datetime.now()
            kendaraan_masuk[nomor_kendaraan] = {'waktu_masuk': waktu_masuk}
            print("Waktu masuk:", waktu_masuk)
            print("Gerbang masuk terbuka. Silahkan masuk.")
            break

#Fungsi Untuk Kendaraan Keluar
def kendaraan_keluar_area_parkir():
    nomor_kendaraan = input("Masukkan nomor/plat kendaraan: ")

    if nomor_kendaraan not in kendaraan_masuk:
        print("Error: Kendaraan tidak terdaftar dalam area parkir.")
        return
    else:
        waktu_keluar = datetime.datetime.now()
        waktu_masuk = kendaraan_masuk[nomor_kendaraan]['waktu_masuk']
        durasi_parkir = (waktu_keluar - waktu_masuk).total_seconds()

        if durasi_parkir < 60:
            durasi_parkir = 60
        else:
            #Pembulatan waktu parkir ke kelipatan 60 detik
            durasi_parkir = math.ceil(durasi_parkir / 60) * 60

        biaya_parkir = (durasi_parkir / 60) * tarif_per_detik

        #Pengecekan Denda
        denda = 0
        if durasi_parkir >= 240:
            denda = biaya_parkir * denda_4_menit
            if durasi_parkir >= 360:
                denda = biaya_parkir * denda_6_menit

        total_biaya = biaya_parkir + denda

        while True:
            print(f"Biaya parkir untuk kendaraan dengan nomor {nomor_kendaraan}: Rp {int(total_biaya)}")

            if denda > 0:
                print(f"NOTIFIKASI: Anda terkena denda sebesar Rp {int(denda)} karena melebihi waktu parkir.")

            nominal_pembayaran = int(input("Masukkan nominal pembayaran: "))
            if nominal_pembayaran >= total_biaya:
                print("Terima Kasih. Gerbang keluar terbuka.")
                if nominal_pembayaran > total_biaya:
                    kembalian = nominal_pembayaran - total_biaya
                    print(f"Kembalian RP {kembalian}")
                else:
                    kembalian = 0
                del kendaraan_masuk[nomor_kendaraan]

                #Menambahkan informasi transaksi ke riwayat
                waktu.append({
                    'nomor_kendaraan': nomor_kendaraan,
                    'waktu_masuk': waktu_masuk,
                    'waktu_keluar': waktu_keluar,
                    'durasi_parkir': durasi_parkir,
                    'biaya_parkir': total_biaya,
                    'nominal_pembayaran': nominal_pembayaran,
                    'kembalian': kembalian,
                    'denda': denda
                })
                break
            else:
                print("Pembayaran kurang. Silahkan masukkan pembayaran yang cukup.")

#Fungsi Untuk Riwayat Transaksi Di Menu Admin
def tampilkan_kendaraan_masuk():
    print("\n===== Riwayat Transaksi Parkir =====")
    for transaksi in waktu:
        print(f"Nomor Kendaraan: {transaksi['nomor_kendaraan']}")
        print(f"Waktu Masuk: {transaksi['waktu_masuk']}")
        print(f"Waktu Keluar: {transaksi['waktu_keluar']}")
        print(f"Durasi Parkir: {transaksi['durasi_parkir']} detik")
        print(f"Biaya Parkir: Rp {int(transaksi['biaya_parkir'])}")
        print(f"Denda: Rp {int(transaksi['denda'])}")
        print(f"Nominal Pembayaran: Rp {transaksi['nominal_pembayaran']}")
        print(f"Kembalian: Rp {transaksi['kembalian']}")
        print("=" * 30)

#Fungsi Untuk Tampilan Menu Utama
def menu_utama():
    while True:
        print("\n=== MENU PARKIR ===")
        print("1. Masuk area parkir")
        print("2. Keluar area parkir")
        print("3. Admin parkir")
        pilih_menu = (input("Pilih menu parkir (1/2/3): "))

        #Percabangan Pemilihan Di Menu Utama
        if pilih_menu == "1":
            kendaraan_masuk_area_parkir()
        elif pilih_menu == "2":
            kendaraan_keluar_area_parkir()
        elif pilih_menu == "3":
             input_pin()
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

#Perulangan Untuk Memulai Program Parkir
while True:
    Pilih = int(input("\nApakah Anda Ingin Memulai Program Parkir? \n\n1.Ya\n2.Tidak\n\npilih Dulu ya!: "))
    if (Pilih == 1):
        menu_utama()
    elif (Pilih == 2):
        print ("\nSEE YOU!!")
        break
    else:
        print ("\nPilihan Tidak Ada Ya Silahkan Cek Lagi")

import time

waktu = []
kendaraan_masuk = {}

pin_admin_parkir = "1234"

def input_pin():
    pin_input = input("\nMasukkan PIN Admin Parkir: ")
    if pin_input == pin_admin_parkir:
        return True
    else:
        print("PIN Salah")
        return False

def kendaraan_masuk_area_parkir():
    nomor_plat = input("\nMasukkan nomor/plat kendaraan (contoh: D1234AF): ")
    waktu_masuk = time.time()
    kendaraan_masuk[nomor_plat] = {'waktu_masuk': waktu_masuk}
    print("Gerbang masuk terbuka. Silahkan masuk.")

def kendaraan_keluar_area_parkir():
    nomor_plat = input("\nMasukkan nomor/plat kendaraan (contoh: D1234AF): ")
    if nomor_plat in kendaraan_masuk:
        waktu_masuk = kendaraan_masuk[nomor_plat]['waktu_masuk']
        waktu_keluar = time.time()
        durasi_parkir_detik = int(waktu_keluar - waktu_masuk)
        durasidetik = durasi_parkir_detik + (60 - durasi_parkir_detik % 60)
        if durasidetik <= 60:
            print(f"Durasi parkir: {durasidetik} detik")
            biaya_parkir = 10000
            print(f"Biaya parkir anda adalah: {biaya_parkir} rupiah")
        elif 60 < durasidetik >= 120:
            biaya_parkir = 2 * 10000
            print(f"Durasi parkir asli : {durasi_parkir_detik} detik")
            print(f"Durasi parkir: {durasidetik} detik")
            print(f"Biaya parkir anda adalah: {biaya_parkir} rupiah")

        del kendaraan_masuk[nomor_plat]
    else:
        print("Nomor plat tidak ditemukan.")

# def hitung_biaya_parkir(durasi_detik):
#     if durasi_detik > 60:
#         durasi_parkir = round(durasi_detik / 60) * 60
#         biaya_parkir = durasi_parkir / 60 * 10000
#         print (biaya_parkir)


    
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
        if input_pin():
            print("\n=== MENU ADMIN ===")
            print("1. Lihat List kendaraan")
            print("2. Kembali ke Menu Utama")
            pilih_menu_admin = int(input("Pilih menu admin: "))
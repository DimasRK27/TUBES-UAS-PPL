import time
import math

plat = []
waktu = []
kendaraan_masuk = []

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
    kendaraan_masuk[nomor_plat] = waktu_masuk
    print("Gerbang masuk terbuka. Silahkan masuk.")
            
while True:
    print("\n=== MENU PARKIR ===")
    print("1. Masuk area parkir")
    print("2. Keluar area parkir")
    print("3. Admin parkir")
    pilih_menu = int(input("Pilih menu parkir (1/2/3): "))


    if pilih_menu == 1:
        nomor_plat = input("\nMasukkan nomor/plat kendaraan (contoh: D1234AF): ")
        current_time = time.strftime("%H:%M:%S")
        inputwaktu = input(f"{current_time}")

        waktu.append({
        'platnomor' : nomor_plat,
        'inputwaktu' : current_time
        })

        
    elif pilih_menu == 2 :
        print("")

    elif pilih_menu == 3:
        input_pin()
        print("\n=== MENU ADMIN ===")
        print("1. Lihat List kendaraan")
        print("2. Kembali ke Menu Utama")
        pilih_menu_admin = int(input("Pilih menu admin: "))
        if pilih_menu_admin == 1:
            print("\n=== LIST nomor plat ===")
            for i, parkir in enumerate(waktu, start=1):
                print(f"{i}. Nomor Plat : {parkir['platnomor']} | Waktu Input : {parkir['inputwaktu']}")
        elif pilih_menu_admin == 2:
            pass
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.") 


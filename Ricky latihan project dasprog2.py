"""menu={
    "aqua"      : 3000,
    "pepsi"     : 2000,
    "cola-cola" : 4000,
    "teh pucuk" : 3000,
}

print("==========daftar menu==========")
for i in menu:
    print("----------",i, " = ",menu[i],"----------")
print("===========================")
beli=input("pilih menu: ")
jumlah=int(input("jumlah pesanan: "))
bayar=jumlah* menu[beli]
print("==========detail pembayaran==========")
print("menu yang di pesan:",beli)
print("jumlah di beli    :",jumlah)
print("total pembayaran  :",bayar)"""


"""menu = {
    "aqua": 3000,
    "pepsi": 2000,
    "cola-cola": 4000,
    "teh pucuk": 3000,
}

while True:
    print("\n========== Daftar Menu ==========")
    for item, harga in menu.items():
        print(f"{item:15} : Rp {harga}")
    print("=================================\n")

    beli = input("Pilih menu (atau ketik 'exit' untuk keluar): ").lower()
    if beli == "exit":
        print("Terima kasih telah menggunakan mesin kasir ini!")
        break
    elif beli not in menu:
        print("Menu tidak ditemukan. Silakan pilih kembali.")
        continue

    try:
        jumlah = int(input("Jumlah pesanan: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0.")
            continue
    except ValueError:
        print("Masukkan angka yang valid untuk jumlah pesanan.")
        continue

    bayar = jumlah * menu[beli]
    print("\n========== Detail Pembayaran ==========")
    print(f"Menu yang dipesan : {beli}")
    print(f"Jumlah dibeli     : {jumlah}")
    print(f"Total pembayaran  : Rp {bayar}")
    print("=======================================\n")

    lagi = input("Apakah ingin memesan lagi? (y/n): ").lower()
    if lagi != 'y':
        print("Terima kasih telah menggunakan mesin kasir ini!")
        break"""


"""menu = {
    "aqua": 3000,
    "pepsi": 2000,
    "cola-cola": 4000,
    "teh pucuk": 3000,
}

total_harga = 0  

print("\n========== Mesin Kasir ==========")
print("\n")
print("\n========== Daftar Menu ==========")
for item, harga in menu.items():
    print(f"{item:15} : Rp {harga}")
print("=================================\n")
while True:
        beli = input("Pilih menu (atau ketik 'exit' untuk selesai): ").lower()
        if beli == "exit":
            break
        elif beli not in menu:
            print("Menu tidak ditemukan. Silakan pilih kembali.")
            continue

        try:
            jumlah = int(input("Jumlah pesanan: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
        except ValueError:
            print("Masukkan angka yang valid untuk jumlah pesanan.")
            continue
member=input("Gunakan keuntungan member?: ([Y/T])").upper()
if member=="Y":
    akun=input("sudah punya akun?:([Y/T]) ").upper()
    if akun=="T":
        import getpass
        print("=================================\n")
        print("\n REGISTRASI")
        menu[beli]=+10000
    
        print("biaya pendaftaran Rp.10.000")
        username1=input("buat username anda: ")
        password1=input("buat password anda: ")
        print("\n")
        print("-----DATA DI KONFIRMASI-----")
        print("\n")
        username2=input("masukan username anda: ")
        password2=getpass.getpass("masukan password anda: ")
        if username2==username1 and password2==password1:
            print("=================================")
            print(f"login di terima,selamat datang {username1}")
            print("=================================\n")
            print("\tpromo spesial!")
            print("paket hemat1 : 3 minumam Rp5000")
            while True:
                print("=================================\n")
                beli2=input("ingin membeli paket? masukan nama paket.ketik(exit)jika tidak..")
                print("=================================\n")
                if beli2=="paket hemat1":
                    menu[beli]+=5000
                
                elif beli2=="exit":
                    break
                    
                
        else:
            print("=================================\n")
            print(f"login di tolak,username tidak terdaftar")
            print("=================================\n")
print("=================================\n")
harga_item = jumlah * menu[beli]
total_harga += harga_item  # Menambahkan ke total harga
print(f"Pesanan {beli} sebanyak {jumlah} berhasil ditambahkan. Subtotal: Rp {harga_item}")
        
print("\n========== Total Belanja ==========")
print(f"Total yang harus dibayar: Rp {total_harga}")
print("Terima kasih telah berbelanja!")"""




menu = {
    "aqua": 3000,
    "pepsi": 2000,
    "coca-cola": 4000,
    "teh pucuk": 3000,
}

total_harga = 0
member = False
biaya_registrasi = 0
paket_terbeli = {"paket1": False, "paket2": False, "paket3": False, "paket4": False}  # Untuk melacak pembelian paket

print("\n========== Mesin Kasir ==========")
print("\n========== Daftar Menu ==========")
for item, harga in menu.items():
    print(f"{item:15} : Rp {harga}")
print("=================================\n")

while True:
    beli = input("Pilih menu (atau ketik 'exit' untuk selesai): ").lower()
    if beli == "exit":
        break
    elif beli not in menu:
        print("Menu tidak ditemukan. Silakan pilih kembali.")
        continue

    try:
        jumlah = int(input("Jumlah pesanan: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0.")
            continue
    except ValueError:
        print("Masukkan angka yang valid untuk jumlah pesanan.")
        continue

    harga_item = jumlah * menu[beli]
    total_harga += harga_item
    print(f"Pesanan {beli} sebanyak {jumlah} berhasil ditambahkan. Subtotal: Rp {harga_item}")

# Penawaran Member
gunakan_member = input("\nApakah Anda ingin menggunakan keuntungan member? ([Y/T]) ").upper()
if gunakan_member == "Y":
    sudah_akun = input("Apakah Anda sudah memiliki akun member? ([Y/T]) ").upper()
    if sudah_akun == "T":
        print("\n")
        print("========================================")
        print("Registrasi Member (Biaya Rp 10.000)")
        username = input("Buat username Anda: ")
        password = input("Buat password Anda: ")
        print("--Registrasi berhasil!--")
        print("========================================")
        print("\n")
        # Login setelah registrasi
        while True:
            print("===============================================")
            print("                  -Login-")
            login_username = input("Masukkan username Anda: ")
            login_password = input("Masukkan password Anda: ")

            if login_username == username and login_password == password:
                print("\nLogin berhasil! Anda mendapatkan diskon 10% sebagai member.")
                print("============================================")
                member = True
                biaya_registrasi = 10000  # Tambahkan biaya registrasi
                break
                
            else:
                print("\nLogin gagal! Username atau password salah. Coba lagi.")
    elif sudah_akun == "Y":
        while True:
            print("\n")
            print("========================================")
            print("                  -Login-")
            username = input("Masukkan username Anda: ")
            password = input("Masukkan password Anda: ")
            print("========================================")
            print("\n")
            if username == "k" and password == "k":
                print("\n       Login berhasil! Anda mendapatkan diskon 10% sebagai member.")
                member = True
                break
            else:
                print("\nLogin gagal! Username atau password salah. Coba lagi.")

    # Menawarkan Paket Promo
    while True:
        print("""
        =============================================================
                                PROMO SPESIAL!!!
        
        PAKET1            PAKET2          PAKET3          PAKET4
        Aqua              indomilk        sariwangi       molto
        chitato           mie sedaap(2)   sunco           sunlight
        silverqueen       teh pucuk       bango           giv
                          jet zet                         pepsodent
        -----------       -----------     -----------     -----------
        Rp17.000          Rp21.000        Rp50.000        Rp22.000
        =============================================================
        """)
        beli2 = input("Ketik nama paket untuk membeli atau ketik 'exit' untuk selesai: ").lower()

        if beli2 == "exit":
            break
        elif beli2 == "paket1":
            if not paket_terbeli["paket1"]:
                total_harga += 17000
                paket_terbeli["paket1"] = True
                print("Paket1 berhasil ditambahkan. Subtotal: Rp 17.000")
            else:
                print("Paket1 sudah dibeli. Anda tidak bisa membeli lagi.")
        elif beli2 == "paket2":
            if not paket_terbeli["paket2"]:
                total_harga += 21000
                paket_terbeli["paket2"] = True
                print("Paket2 berhasil ditambahkan. Subtotal: Rp 21.000")
            else:
                print("Paket2 sudah dibeli. Anda tidak bisa membeli lagi.")
        elif beli2 == "paket3":
            if not paket_terbeli["paket3"]:
                total_harga += 50000
                paket_terbeli["paket3"] = True
                print("Paket3 berhasil ditambahkan. Subtotal: Rp 50.000")
            else:
                print("Paket3 sudah dibeli. Anda tidak bisa membeli lagi.")
        elif beli2 == "paket4":
            if not paket_terbeli["paket4"]:
                total_harga += 22000
                paket_terbeli["paket4"] = True
                print("Paket4 berhasil ditambahkan. Subtotal: Rp 22.000")
            else:
                print("Paket4 sudah dibeli. Anda tidak bisa membeli lagi.")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if member:
    diskon = total_harga * 0.1  # Diskon 10% untuk member
    total_harga -= diskon
    print(f"\nDiskon member 10% diterapkan. Anda hemat Rp {int(diskon)}.")

total_akhir = total_harga + biaya_registrasi

print("\n========== Total Belanja ==========")
print(f"Biaya registrasi member: Rp {biaya_registrasi}")
print(f"Total belanja setelah diskon: Rp {total_harga}")
print(f"Total yang harus dibayar: Rp {total_akhir}")
print("Terima kasih telah berbelanja!")





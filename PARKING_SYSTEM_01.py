import time
from time import sleep
import winsound

#FUNGSI PEMBATAS
def space():
    print()
    print("==========================================================") ; sleep(1)
    print()

#FUNGSI LOADING
def wait():
    print("[MOHON TUNGGU SEBENTAR]") ; sleep(0.5)
    print(".", end=" ") ; sleep(0.5)
    print(".", end=" ") ; sleep(0.5)
    print(".") ; sleep(0.5)
    print()
    
#PENGATURAN AWAL PARKING SYSTEM
print("[PENGATURAN AWAL PARKING SYSTEM]")
a = int(input("Jumlah slot parkir motor : "))
b = int(input("Jumlah slot parkir mobil : "))
c1 = int(input("Waktu pertama untuk biaya khusus motor (detik) : "))
d1 = int(input("Biaya khusus motor (Rupiah) : "))
e1 = int(input("Perhitungan biaya motor untuk setiap waktu (detik) : "))
f1 = int(input("Biaya motor (Rupiah) : "))
c2 = int(input("Waktu pertama untuk biaya khusus mobil (detik) : "))
d2 = int(input("Biaya khusus mobil (Rupiah) : "))
e2 = int(input("Perhitungan biaya mobil untuk setiap waktu (detik) : "))
f2 = int(input("Biaya mobil (Rupiah) : "))
space()

#MENUNJUKKAN KETERSEDIAAN SLOT PARKIR
def slot_parkir(motor_count, mobil_count):
    print("[SLOT PARKIR TERSEDIA]")
    print("Mobil =", mobil_count)
    print("Motor =", motor_count)

#MENGHITUNG JUMLAH SLOT PARKIR YANG KOSONG
def count_motor(x):
    motor_count = 0
    for i in range(a):
        motor_count = motor_count + x[i]
    return motor_count
def count_mobil(y):
    mobil_count = 0
    for i in range(b):
        mobil_count = mobil_count + y[i]
    return (mobil_count)

#KALKULASI HARGA
def perhitungan_motor(durasi):
    harga = 0
    harga1 = 0
    if durasi >= c1:
        harga1 = harga + d1
        durasi = durasi - c1
        if durasi < 0:
            durasi = 0
        elif durasi%e1 > 0:
            durasi = durasi + e1
        harga = (durasi // e1)*f1
        total = harga1 + harga
    return total
def perhitungan_mobil(durasi):
    harga = 0
    harga1 = 0
    if durasi >= c2:
        harga1 = harga + d2
        durasi = durasi - c2
        if durasi < 0:
            durasi = 0
        elif durasi%e2 > 0:
            durasi = durasi + e2
        harga = (durasi // e2)*f2
        total = harga1 + harga
    return total

#DEKLARASI VARIABEL
motor = [1 for i in range(a)]
mobil = [1 for j in range(b)]
start_motor = [0 for i in range(a)]
start_mobil = [0 for i in range(b)]

#PROGRAM UTAMA
looping = 0
while (looping<1):
    sistem = int(input("Tekan 1 untuk masuk atau 2 untuk keluar. \n"))
    space()

    if sistem == 1:
        motor_count = count_motor(motor)
        mobil_count = count_mobil(mobil)
        slot_parkir(motor_count, mobil_count)
        winsound.PlaySound("SELAMAT_DATANG.wav", winsound.SND_ASYNC)
        print()
        print("[SELAMAT DATANG]")
        jenis = int(input("Tekan 1 untuk motor atau 2 untuk mobil. \n"))
        space()

        if jenis == 1 and motor_count != 0:
            print("Silahkan tempelkan kartu")
            bantuan = int(input("Silahkan tekan 1 untuk tempelkan kartu atau 2 untuk bantuan. \n"))
            space()
            wait()
            
            if bantuan == 1:
                check = 0
                while check<a:
                    if motor[check] == 1:
                        slot = check
                        check = 999
                    check = check + 1
                motor[slot] = motor[slot] - 1
                winsound.PlaySound("SILAHKAN_MASUK.wav", winsound.SND_ASYNC)
                print("[TERIMAKASIH]\nAnda parkir pada slot", str(slot+1))
                space()
                start_motor[slot] = time.time()
                
            else:
                print("Mohon tunggu sebentar petugas kami akan segera datang.")
                space()
                
        elif jenis == 2 and mobil_count != 0:
            print("Silahkan tempelkan kartu")
            bantuan = int(input("Silahkan tekan 1 untuk tempelkan kartu atau 2 untuk bantuan. \n"))
            space()
            wait()
            
            if bantuan == 1:
                check = 0
                while check<b:
                    if mobil[check] == 1:
                        slot = check
                        check = 999
                    check = check + 1
                mobil[slot] = mobil[slot] - 1
                winsound.PlaySound("SILAHKAN_MASUK.wav", winsound.SND_ASYNC)
                print("[TERIMAKASIH]\nAnda parkir pada slot", str(slot+1))
                space()
                start_mobil[slot] = time.time()
                
            else:
                print("Mohon tunggu sebentar petugas kami akan segera datang.")
                space()
                
        elif mobil_count == 0 or motor_count == 0:
            print("Mohon maaf parkiran telah penuh.")
            space()
        else:
            print("[MOHON MAAF SILAHKAN COBA LAGI {ERROR CODE 1}]")
            space()

    elif sistem == 2:
        motor_count = count_motor(motor)
        mobil_count = count_mobil(mobil)
        jenis = int(input("Tekan 1 untuk motor atau 2 untuk mobil. \n"))
        space()
        if jenis == 1 and motor_count < a:
            slot = int(input("Silahkan masukkan slot parkir Anda: \n")) - 1
            if motor[slot] == 0:
                motor[slot] = motor[slot] + 1
                end_motor = time.time()
                durasi = end_motor - start_motor[slot]
                print("Anda telah parkir selama", durasi, "detik")
                total = perhitungan_motor(durasi)
                print("Biaya parkir sebesar Rp." + str(total))
                space()
                input("Tekan enter untuk pembayaran dengan tempelkan kartu.")
                print()
                print("[TERIMAKASIH]") ; sleep(1)
                space()
            else:
                print()
                print("[MOHON MAAF SILAHKAN COBA LAGI {ERROR CODE 2}]")
                space()
            
        elif jenis == 2 and mobil_count < b:
            slot = int(input("Silahkan masukkan slot parkir Anda: \n")) - 1
            if mobil[slot] == 0:
                mobil[slot] = mobil[slot] + 1
                end_mobil = time.time()
                durasi = end_mobil - start_mobil[slot]
                print("Anda telah parkir selama", durasi, "detik")
                total = perhitungan_mobil(durasi)
                print("Biaya parkir sebesar Rp." + str(total))
                space()
                input("Tekan enter untuk pembayaran dengan tempelkan kartu.")
                print()
                print("[TERIMAKASIH]") ; sleep(1)
                space()
            else:
                print()
                print("[MOHON MAAF SILAHKAN COBA LAGI {ERROR CODE 2}]")
                space()
        elif jenis != 1 and jenis != 2:
            print("[MOHON MAAF SILAHKAN COBA LAGI {ERROR CODE 1}]")
            space()
        else:
            print("[MOHON MAAF SILAHKAN COBA LAGI {ERROR CODE 2}]")
            space()
    else:
        print("[MOHON MAAF SILAHKAN COBA LAGI {ERROR CODE 1}]")
        space()

input("EXIT {ERROR CODE 3}")

#LIST ERROR
#CODE 1: PILIHAN TIDAK ADA
#CODE 2: SLOT TIDAK ADA
#CODE 3: PERULANGAN SELESAI

#REVISI 01
# =SUDAH PAKAI SUARA
# ="TAP KARTU" DIGANTI JADI "TEMPELKAN KARTU
# =KODE ERROR UDAH BENER


"**PROPERTY OF HAYU**"

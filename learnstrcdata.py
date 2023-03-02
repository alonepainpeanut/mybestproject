# Dibuat oleh Ridwanul Bakhri
# hasil jujur, karya sendiri

def tiketDewasa():
    while True:
        a = True
        while a:
            jumlahOrang = int(input("Masukkan jumlah orang \t\t\t\t\t: "))
            if jumlahOrang < 0:
                print("Maaf, Input Anda salah, jumlah tidak boleh negatif!")
                break
            elif 4 < jumlahOrang <= 6:
                hargaAwal = jumlahOrang * 255000
                hargaDiskon = int(hargaAwal - ((20 / 100) * hargaAwal))
                print(f"Harga setelah diskon \t\t\t\t\t: Rp{hargaDiskon:,}")
                nominalPembayaran = int(input("Masukkan nominal pembayaran Anda \t\t\t: "))
                if nominalPembayaran > hargaDiskon:
                    print(f"Uang Anda \t\t\t\t\t\t: Rp{nominalPembayaran:,}")
                    print("-"*105)
                    print(f"Uang kembalian Anda \t\t\t\t\t: Rp{(nominalPembayaran - hargaDiskon):,}")
                    print(f"""
                                        Terima kasih telah membeli karcis kami :)\n{"-"*105}""")
                    a = False
                elif nominalPembayaran < hargaDiskon:
                    import os
                    os.system("cls")
                    print()
                    print(f"""{("Maaf, proses tidak dapat dilakukan karena uang Anda tidak cukup!".center(105)).upper()}
{"-"*105}\nsisa tagihan Anda \t\t\t\t\t\t: Rp{abs(nominalPembayaran - hargaDiskon):,}""")
                    a = False
                else:
                    print(f"Uang Anda pas!")
                    print(f"""
                                        Terima kasih telah membeli karcis kami :)\n{"-"*105}""")
                    a = False
            elif 1 <= jumlahOrang or jumlahOrang >= 7:
                hargaAwal = jumlahOrang * 255000
                print(f"Harga karcis \t\t\t\t\t\t: Rp{hargaAwal:,}")
                nominalPembayaran = int(input("Masukkan nominal pembayaran Anda \t\t\t: "))
                if nominalPembayaran > hargaAwal:
                    print(f"Uang Anda \t\t\t\t\t\t: Rp{nominalPembayaran:,}")
                    print("-"*105)
                    print(f"Uang kembalian Anda \t\t\t\t\t: Rp{(nominalPembayaran - hargaAwal):,}")
                    print(f"""
                                        Terima kasih telah membeli karcis kami :)\n{"-"*105}""")
                    a = False

                elif nominalPembayaran < hargaAwal:
                    import os
                    os.system("cls")
                    print()
                    print(f"""{("Maaf, proses tidak dapat dilakukan karena uang Anda tidak cukup!".center(105)).upper()}
{"-"*105}\nsisa tagihan Anda \t\t\t\t\t\t: Rp{abs(nominalPembayaran - hargaAwal):,}""")
                    a = False       
                else:
                    print(f"Uang Anda pas!")
                    print(f"""
                                        Terima kasih telah membeli karcis kami :)\n{"-"*105}""")
                    a = False
        if a == False:
            break
                    

def tiketAnakAnak():
    while True:
        a = True
        while a:
            jumlahOrang = int(input("Masukkan jumlah orang \t\t\t\t\t: "))
            if jumlahOrang < 0:
                print("Maaf, Input Anda salah, jumlah tidak boleh negatif!")
                break
            hargaAwal = jumlahOrang * 150000
            print(f"Harga tiket \t\t\t\t\t\t: Rp{hargaAwal:,}")
            nominalPembayaran = int(input("Masukkan nominal pembayaran Anda \t\t\t: "))
            if nominalPembayaran > hargaAwal:
                print(f"Uang Anda \t\t\t\t\t\t: Rp{nominalPembayaran:,}")
                print("-"*105)
                print(f"Uang kembalian Anda \t\t\t\t\t: Rp{(nominalPembayaran - hargaAwal):,}")
                print(f"""
                                    Terima kasih telah membeli karcis kami :)\n{"-"*105}""")
                a = False
            elif nominalPembayaran < hargaAwal:
                import os
                os.system("cls")
                print()
                print(f"""{("Maaf, proses tidak dapat dilakukan karena uang Anda tidak cukup!".center(105)).upper()}
{"-"*105}\nsisa tagihan Anda \t\t\t\t\t\t: Rp{abs(nominalPembayaran - hargaAwal):,}""")
                a = False
            else:
                print(f"Uang Anda pas!")
                print(f"""
                                    Terima kasih telah membeli karcis kami :)\n{"-"*105}""")
                a = False
        if a == False:
            break

def tiketInfant():
    while True:
        a = True
        while a:
            jumlahOrang = int(input("Masukkan jumlah orang \t\t\t\t\t: "))
            if jumlahOrang < 0:
                print("Maaf, Input Anda salah, jumlah tidak boleh negatif!")
                break
            hargaAwal = jumlahOrang * 25000
            print(f"Harga tiket \t\t\t\t\t\t: Rp{hargaAwal:,}")
            nominalPembayaran = int(input("Masukkan nominal pembayaran Anda \t\t\t: "))
            if nominalPembayaran > hargaAwal:
                print(f"Uang Anda \t\t\t\t\t\t: Rp{nominalPembayaran:,}")
                print("-"*105)
                print(f"Uang kembalian Anda \t\t\t\t\t: Rp{(nominalPembayaran - hargaAwal):,}")
                print(f"""
                                    Terima kasih telah membeli karcis kami :)\n{"-"*105}""")
                a = False
            elif nominalPembayaran < hargaAwal:
                import os
                os.system("cls")
                print()
                print(f"""{("Maaf, proses tidak dapat dilakukan karena uang Anda tidak cukup!".center(105)).upper()}
{"-"*105}\nsisa tagihan Anda \t\t\t\t\t\t: Rp{abs(nominalPembayaran - hargaAwal):,}""")
                a = False
            else:
                print(f"Uang Anda pas!")
                print(f"""
                                    Terima kasih telah membeli karcis kami :)\n{"-"*105}""")
                a = False
        if a == False:
            break

print(f"""
 {" AGEN PENJUALAN KARCIS KERETA API 'ARGO RITMA' ".center(105, "-")}

1. Tiket Dewasa      = Rp255,000
2. Tiket Anak-Anak   = Rp150,000
3. Tiket Infant      = Rp25,000

Diskon 20% untuk pembelian tiket dewasa lebih dari 4 orang dan maksimal 6 orang :)

{"-"*105}
""")

while True:
    pilihanTiket = int(input("Masukkan opsi pembelian tiket \t\t\t\t: "))
    if pilihanTiket not in range(1, 4):
        print("Maaf, input Anda salah! Mohon memilih di antara opsi 1,2, dan 3!")
    elif pilihanTiket == 1:
        tiketDewasa()
        break
    elif pilihanTiket == 2:
        tiketAnakAnak()
        break
    elif pilihanTiket == 3:
        tiketInfant()
        break
import Carrefour
import Hypermart
import Superindo

print("Indeks Harga Makanan Carrefour, Hypermart, dan Superindo\n")

j = ''
a = Carrefour.buah("Jeruk = Rp. 2,490/100gr", "Apel = Rp. 4,690/100gr", "Melon = Rp. 2,590/100gr", "Semangka Merah = Rp. 1,350/100gr")
b = Carrefour.sayur("Buncis = Rp. 4,780/100gr", "Cabai = Rp. 12,590/100gr", "Kembang Kol = Rp. 3,990/100gr", "Jagung = Rp. 1,170/100gr")
c = Carrefour.hewani("Susu = Rp. 17,170/liter", "Telur = Rp. 22,900/kg", "Fillet Ayam = Rp. 4,250/100gr", "Cumi = Rp. 9,800/100gr")
d = Carrefour.mie("Indomie Goreng = Rp. 2,500/pcs", "Indomie Rebus = Rp. 2,500/pcs", "Mie Sedaap Goreng = Rp. 2,800/pcs", "Mie Sedaap Rebus = Rp. 2,190/pcs")

e = Hypermart.buah("Jeruk = Rp. 2,890/100gr", "Apel = Rp. 4,990/100gr", "Melon = Rp. 1,850/100gr", "Semangka Merah = Rp. 750/100gr")
f = Hypermart.sayur("Buncis = Rp. 1,990/100gr", "Cabai = Rp. 3,890/100gr", "Kembang Kol = Rp. 3,590/100gr", "Jagung = Rp. 1,190/100gr")
g = Hypermart.hewani("Susu = Rp. 26,950/liter", "Telur = Rp. 15,000/10pcs", "Fillet Ayam = Rp. 6,290/100gr", "Cumi = Rp. 7,890/100gr")
h = Hypermart.mie("Indomie Goreng = Rp. 2,100/pcs", "Indomie Rebus = Rp. 2,167/pcs", "Mie Sedaap Goreng = Rp. 2,180/pcs", "Mie Sedaap Rebus = Rp. 2,200/pcs")

i = Superindo.buah("Jeruk = Rp. 4,290/100gr", "Apel = Rp. 4,990/100gr", "Melon = Rp. 2,295/100gr", "Semangka Merah = Rp. 1,195/100gr")
j = Superindo.sayur("Buncis = Rp. 2,695/100gr", "Cabai = Rp. 9,993/100gr", "Kembang Kol = Rp. 3,895/100gr", "Jagung = Rp. 4,833/pcs")
k = Superindo.hewani("Susu = Rp. 16,322/liter", "Telur = Rp. 40,450/10pcs", "Fillet Ayam = Rp. 6,995/100gr", "Cumi = Rp. 9,495/100gr")
l = Superindo.mie("Indomie Goreng = Rp. 2,190/pcs", "Indomie Rebus = Rp. 2,390/pcs", "Mie Sedaap Goreng = Rp. 2,500/pcs", "Mie Sedaap Rebus = Rp. 2,200/pcs")

while j != "tidak" or j != "Tidak":
    print("Jenis Makanan Apa yang Ingin Anda Beli?")
    print("a. Buah-buahan\nb. Sayur-sayuran\nc. Produk Hewani\nd. Mie Instan")
    j = input("Masukkan pilihan anda: ")

    #harga buah
    if j == "a" or j == "A":
        print("\nHarga buah-buahan pada toko swalayan:\n")
        #harga di Carrefour
        a.hargabuah()
        #harga di Hypermart
        e.hargabuah()
        #harga di Superindo
        i.hargabuah()
        print("Apakah anda masih ingin berbelanja?")
        print("Ya.\nTidak.")
        j = input("Masukkan pilihan anda: ")
        if j == "ya" or j == "Ya":
            print("Selamat Berbelanja.\n")
        elif j == "tidak" or j == "Tidak":
            print("Terimakasih sudah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak tersedia.")
    
    #harga sayur
    elif j == "b" or j == "B":
        print("\nHarga sayur-sayuran pada toko swalayan:\n")
        #harga di Carrefour
        b.hargasayur()
        #harga di Hypermart

        #harga di Superindo

        print("Apakah anda masih ingin berbelanja?")
        print("Ya.\nTidak.")
        j = input("Masukkan pilihan anda: ")
        if j == "ya" or j == "Ya":
            print("Selamat Berbelanja.\n")
        elif j == "tidak" or j == "Tidak":
            print("Terimakasih sudah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak tersedia.")

    #harga produk hewani
    elif j == "c" or j == "C":
        print("\nHarga produk hewani pada toko swalayan:\n")
        #harga di Carrefour
        c.hargahewani()
        #harga di Hypermart

        #harga di Superindo

        print("Apakah anda masih ingin berbelanja?")
        print("Ya.\nTidak.")
        j = input("Masukkan pilihan anda: ")
        if j == "ya" or j == "Ya":
            print("Selamat Berbelanja.\n")
        elif j == "tidak" or j == "Tidak":
            print("Terimakasih sudah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak tersedia.")

    #harga mie instan
    elif j == "d" or j == "D":
        print("\nHarga mie instan pada toko swalayan:\n")
        #harga di Carrefour
        d.hargamie()
        #harga di Hypermart

        #harga di Superindo

        print("Apakah anda masih ingin berbelanja?")
        print("Ya.\nTidak.")
        j = input("Masukkan pilihan anda: ")
        if j == "ya" or j == "Ya":
            print("Selamat Berbelanja.\n")
        elif j == "tidak" or j == "Tidak":
            print("Terimakasih sudah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak tersedia.")
 
    else:
        print("Pilihan tidak tersedia.")


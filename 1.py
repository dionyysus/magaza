import sqlite3

secim = int(input("""
Lütfen girişinizi belirleyiniz:
    1- Personel girişi
    2- Müşteri girişi
"""))


if secim == 1:
    personel = []
    db = sqlite3.connect("Urun.yonetimi")
    urun = db.cursor()

    urun.execute("Create Table if not exists personel_giris (users, password)")
    while True:
        giris = int(input("Giriş yapmak için: 1, Kayıt olmak için: 2"))
        if giris == 1:
            while True:
                kullanici = input("Kullanıcı adınızı giriniz: ")
                sifre = input("Şifre giriniz:")
                urun.execute("SELECT * FROM personel_giris WHERE users = ? and password = ? ", (kullanici, sifre))
                data = urun.fetchone()
                if data:
                    print("\nGiriş yapıldı.\n")
                    break
                else:
                    print("\n Girdiğiniz bilgilere uygun bir kayıt yok. Lütfen kayıt olunuz!")
            break
        elif giris == 2:
            while True:
                kullanici_ad = input("Kullanıcı adınızı belirleyiniz: ")
                pswrd = input("Şifre belirleyin: ")
                if len(pswrd) <= 5:
                    print("\nLütfen 5 kelimeden büyük şifre belirleyiniz:\n")
                    continue
                else:
                    personel += [kullanici_ad, pswrd]
                    urun.execute("insert into personel_giris values (?, ?)", personel)
                    print("Tebrikler kayıt oluşturuldu..")
                    break
        else:
            print("Geçersiz giriş..")
            continue
        print("Giriş yapılabilir.:)")
    isim.commit()
    isim.close()

    print("""        
    # # # # # # # # # # # # # # # # # # # # # # #
    #            Ü R Ü N  M E N Ü S Ü           #
    # # # # # # # # # # # # # # # # # # # # # # #
    #                                           #
    #                                           #
    #         [1]... Ürün  Ekle                 #
    #         [2]... Ürün Sil                   #
    #                                           #
    #                                           #
    #                                           #
    #         [ ].. Seçimi Giriniz :            #
    #                                           #
    # # # # # # # # # # # # # # # # # # # # # # #
    """)

    urunler = []
    # ad = sqlite3.connect("Urun.gizem")
    # a = ad.cursor()

    a.execute("Create Table if not exists urunler_tablosu (urun_ad, miktar)")
    while True:
        secim = int(input("Yapmak istediğiniz işlemi seçiniz: "))
        if secim == 1:
            i = 0
            urun_sayi = int(input("Kaç ürün ekleyeceğinizi giriniz: "))
            while urun_sayi != i:
                urun_isim = input("Ürün adını giriniz:\n")
                urun_miktar = int(input("Ürün miktarını giriniz:\n "))
                i += 1
                a.execute("SELECT * FROM urunler_tablosu WHERE urun_ad = ? and miktar = ? ", (urun_isim, urun_miktar))
                data = a.fetchone()

                if data:
                    print("Ürünler kaydedildi.")
                    urunler += [urun_isim, urun_miktar]
                    a.execute("insert into urunler_tablosu values ( ?, ?)", urunler)
                    break
        elif secim == 2:
            while True:
                urun_sil = input("Silmek istediğiniz ürünün adını giriniz: \n")
                sil_miktar = int(input("Üründen kaç adet sileceğinizi giriniz:\n "))
                a.execute("SELECT * FROM urunler_tablosu WHERE urunSil = ? and silMiktar = ?", (urun_sil, sil_miktar))
                data = a.fetchone()
                if data:
                    urunler.remove(urun_sil, sil_miktar)
                    a.execute("insert into urunler_tablosu values (?, ?)", urunler)
                    break
        else:
            print("Hatalı şeçim yaptınız.")
            continue
    ad.commit()
    ad.close()
if secim == 2:
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#            S A T I Ş  M E N Ü S Ü         #")
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#                                           #")
    print("#                                           #")
    print("#    Müşteri Adı"
          "     Miktar"
          "     Tutar")
    print("# # # # # # # # # # # # # # # # # # # # # # #")
    print("#               #")
    print("#                                           #")
    print("# # # # # # # # # # # # # # # # # # # # # # #")

    islem = int(input("Almak istediğiniz ürünü giriniz: "))

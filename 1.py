import sqlite3


db = sqlite3.connect("veritabani.db")
dbcursor = db.cursor()

GIRIS_GEREKLI = False


#dbcursor.execute("CREATE TABLE IF NOT EXISTS personel_giris (users, password)")
#dbcursor.execute("insert into personel_giris ('gizem','coskun')")
#db.commit()
#dbcursor.execute("CREATE TABLE IF NOT EXISTS urunler (urun_ID INTEGER PRIMARY KEY AUTOINCREMENT, urun_ad STRING (50), urun_fiyat DECIMAL, urun_mevcut INTEGER");


def KullaniciGirisi():

    kullanici = input("Kullanıcı adınızı giriniz: ")
    sifre = input("Şifre giriniz:")
    dbcursor.execute("SELECT * FROM personel_giris WHERE users = ? and password = ? ", (kullanici, sifre))
    data = dbcursor.fetchone()
    if data:
        print("\nGiriş yapıldı.\n")
        return True
    else:
        print("\n Girdiğiniz bilgilere uygun bir kayıt yok. Lütfen kayıt olunuz!")
        return False




def KullaniciKayit(kullanici_turu=1):
    while True:
        kullanici_ad = input("Kullanıcı adınızı belirleyiniz: ")
        pswrd = input("Şifre belirleyin: ")

        if len(pswrd) <= 5:
            print("\nLütfen 5 karakterden büyük şifre belirleyiniz:\n")
            continue
        else:
            dbcursor.execute("insert into personel_giris values ('%s', '%s')" % (kullanici_ad,pswrd))
            db.commit()
            print("Tebrikler kayıt oluşturuldu..")
            return True

    return False



def AnaGiris():
    secim = int(input("""
    Lütfen girişinizi belirleyiniz:
        1- Personel girişi
        2- Müşteri girişi
        3- Yeni Kayit

    """))
    if secim == 1:
        KullaniciGirisi()
    elif secim == 2:
        KullaniciGirisi()
    elif secim == 3:
        KullaniciKayit()




if __name__ == "__main__":
    if GIRIS_GEREKLI:
        while True:
            if AnaGiris():
                break

    print("""        
    # # # # # # # # # # # # # # # # # # # # # # #
    #            Ü R Ü N  M E N Ü S Ü           #
    # # # # # # # # # # # # # # # # # # # # # # #
    #                                           #
    #                                           #ksiyon
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

    while True:
        secim = int(input("Yapmak istediğiniz işlemi seçiniz: "))
        if secim == 1:
            i = 0
            urun_sayi = int(input("Kaç ürün ekleyeceğinizi giriniz: "))
            while urun_sayi != i:
                urun_isim = input("Ürün adını giriniz:\n")
                urun_miktar = int(input("Ürün miktarını giriniz:\n "))
                i += 1

                ## HATALI KOD. OLMAYAN URUN ICIN SORGULAMA YAPILIYOR
                dbcursor.execute("SELECT * FROM urunler WHERE urun_ad = '%s' " % (urun_isim))
                data = dbcursor.fetchone()

                #urun adi varsa miktar guncellenir
                if data:
                    dbcursor.execute("update urunler set urun_mevcut = %s WHERE urun_adi='%s' values ('%s','%s')"  % ((data[1]+int(urun_miktar)), urun_isim) )
                    db.commit()
                # urun yoksa eklenir
                else:
                    dbcursor.execute(
                        "insert into urunler (urun_ad, urun_mevcut) values ('%s','%s')" % (urun_isim, urun_miktar))
                    db.commit()
                    # islem bitmeden kullaniciya geri bildirim yapilmaz
                    print("Ürünler kaydedildi.")

                    break

        elif secim == 2:
            while True:
                urun_adi = input("Silmek istediğiniz ürünün adını giriniz: \n")
                sil_miktar = int(input("Üründen kaç adet sileceğinizi giriniz:\n "))

                dbcursor.execute("SELECT * FROM urunler WHERE urun_ad = '%s' " % (urun_adi))
                data = dbcursor.fetchone()
                if data:
                    try:
                        dbcursor.execute("DELETE FROM urunler WHERE urun_ad='%s' " % urun_adi)
                        db.commit()
                        print('Urun silindi')
                    except:
                        print('Hata: Urun silinemedi')


                # @TODO - urun adina gore urunu bul sonra DELETE komutu ile sil
                """
                dbcursor.execute("SELECT * FROM urunler_tablosu WHERE urunSil = ? and silMiktar = ?", (urun_sil, sil_miktar))
                data = dbcursor.fetchone()
                if data:
                    urunler.remove(urun_sil, sil_miktar)
                    dbcursor.execute("insert into urunler_tablosu values (?, ?)", urunler)
                    break
                """
        else:
            print("Hatalı şeçim yaptınız.")
            continue



def Satis():
    if secim == 2:
        print("""
        # # # # # # # # # # # # # # # # # # # # # # #
        #            S A T I Ş  M E N Ü S Ü         #
        # # # # # # # # # # # # # # # # # # # # # # #
        #                                           #
        #                                           #
        #    Müşteri Adı
                   Miktar
                   Tutar
        # # # # # # # # # # # # # # # # # # # # # # #
        #                                           #
        #                                           #
        # # # # # # # # # # # # # # # # # # # # # # #
        """)

        islem = int(input("Almak istediğiniz ürünü giriniz: "))


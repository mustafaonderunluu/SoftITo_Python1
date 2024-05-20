class Insan:
    adi="ibrahim123"
    soyadi="gokyar"
    yas=0
    maas= 0.0
    cinsiyet = False
    def __init__(self,adi=None,soyadi=None,yas=None,maas=None,cinsiyet=None):
       self.adi= adi
       self.soyadi= soyadi
       self.cinsiyet=cinsiyet
       self.yas=yas
       self.maas=maas


    #Uyu adında ve parametre almayan ve geriye değer döndürmeyen fonksiyon tanımlandı.
    def uyu(self):
        print("uyuyor")
    def ekranayaz(self,isim,soyisim):
       
       print("Kişinin adı : " + isim + "Kişinin Soyadı :"+soyisim )
    def mesajGoster(self,age):
       mesaj=" "
       if (age > 0 and age <= 18):
         print("Küçüksünüz")
 

       
#bir classdan nesne olusturmak icin
#nesneadi = classadi()



#constructor
i2=Insan("Onder","Ünlü",22,38000,True)






i = Insan()
i.adi="İbrahim"
i.soyadi="gökyar"
i.yas=45
i.maas= 85205
i.cinsiyet=True
print("Kişinin Adı = "+  i.adi   +   "  soyadi = "+i.soyadi)


    



#kalitim


class Anne(Insan):
  pass

a=Anne()
a.ekranayaz("Fahriye","Gökyar")

class Baba(Insan):
   pass

b=Baba()
b.ekranayaz("Kasım","Gökyar")


class Cocuk(Insan):
  sifat=" "
  def adSoyadSifatYaz(self,ad,soyad,sifat):
     print(ad+" "+soyad+"  "+sifat )
  

class Cocuk:
    def adSoyadSifatYaz(self, adi, soyadi, sifat):
        print(f"{adi} {soyadi} {sifat}")

class AkilliCocuk(Cocuk):
    pass

ak = AkilliCocuk()
ak.adi = "Hakan"
ak.soyadi = "Yilmaz"
ak.sifat = "Akıllıdır"
ak.adSoyadSifatYaz(ak.adi, ak.soyadi, ak.sifat)

class UsluCocuk(Cocuk):
    pass

uc = UsluCocuk()
uc.adi = "Mehmet"
uc.soyadi = "Yildiz"
uc.sifat = "Usludur"
uc.adSoyadSifatYaz(uc.adi, uc.soyadi, uc.sifat)




   



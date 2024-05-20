class Araba:
    Marka = ""
    Model = ""
    Renk = ""
    yil = 0
    KapiSayisi = 0

    def Sınıf(self, marka, model):
        print(marka + " " + model + " sınıfından bir araba")

    def durum(self, yas):
        if yas > 0 and yas <= 10:
            mesaj = "iyi"
        elif yas > 10 and yas <= 20:
            mesaj = "Servis Gerekebilir"
        elif yas > 20 and yas <= 30:
            mesaj = "Hurdaya Çıkabilir"
        elif yas > 30 and yas <= 40:
            mesaj = "Hurda"
        else:
            mesaj = "Bilinmeyen durum"
        return mesaj

# Ana sınıf örneği
araba = Araba()
araba.Marka = "Ford"
araba.Model = "Ranger"
araba.Renk = "Siyah"
araba.yil = 2023
araba.KapiSayisi = 4

# Yaşı kullanıcıdan al
yas = int(input("Lütfen sayı giriniz: "))
print(araba.durum(yas))

# Kalıtım
class Bmw(Araba):
    pass

a = Bmw()
a.Sınıf("Bmw", "X5")

class Mercedes(Araba):
    pass

b = Mercedes()
b.Sınıf("Mercedes", "XL")

class Porsche(Araba):
    pass

c = Porsche()
c.Sınıf("Porsche", "Carrera")

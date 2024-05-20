class Uygulama:
    age=int(input("Lütfen Yaşınızı Giriniz :"))
    
    def DurumHesaplama(self,age):
        if(age>0 and age<=18):
            print("Küçüksünüz")
        elif(age>18 and age <35):
            print("Gençsiniz")
        elif(age>35 and age<55 ):
            print("Yetişkinsiniz")
        elif(age>55 and age<75):
            print("Yaşlısınız")
        elif(age>75 and age <99):
            print("Çok Yaşlısınız")
        else:
            print("Geçersiz bir sayı girdiniz.")
       

           

    def dogum(self,a,b):
        return a - b
        
zaman=Uygulama()


tarih =int(input("doğum yılı: "))
yil=int(input("şimdiki yıl: "))

sonuc= zaman.dogum(yil,tarih)
print("yaşınız: " +str(sonuc))















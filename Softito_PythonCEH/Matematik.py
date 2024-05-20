class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1+sayi2
    
    def Cikar(self,sayi1,sayi2):
        return sayi1-sayi2
    
    
    def Carp(self,sayi1,sayi2):
        return sayi1*sayi2
    
    def Bol(self,sayi1,sayi2):
        return sayi1/sayi2
    
m=Matematik()
sonuc = m.topla(8,7)
print("Toplam  : " +str(sonuc))

#Kullanicidan veri alma.
number1= int(input("birinci sayiyi giriniz : "))
number2= int(input("ikinci sayiyi giriniz  : "))

toplam =m.topla(number1,number2)
print("Toplam : " +str(toplam)  )


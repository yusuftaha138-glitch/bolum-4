musteriAdi = "Sadik"
musteriSoyad = "Turan"
musteriTelefon = "05321234567"
musteriEmail = "info@sadikturan.com" 
musteriAdres = "Kocaeli"


urun1Ad = "Kablosuz Mouse"
urun1Fiyat = 550

urun2Ad = "Kablosuz Klavye"
urun2Fiyat = 650

urun3Ad = "Dizüstü Bilgisayar"
urun3Fiyat = 55000

toplamOdenenUcret = urun1Fiyat + urun2Fiyat + urun3Fiyat
print ("Toplam ödenen miktar: " + str(toplamOdenenUcret))

print("Toplam kdv oranı:" + str(toplamOdenenUcret * 0.18))
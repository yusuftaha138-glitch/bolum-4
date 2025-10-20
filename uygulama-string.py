title = "Python ile Programlama Dersi"
# title değişkeni içerisindeki karakter sayısı nedir ?

print(len(title))

print (title[0:6])  # Python

print (title[0:6] + " " + title[-5:])

print (title[::-1]) 

ad = input('ad: ')
soyad = input('soyad: ')
not1 = input('1.not: ')
not2 = input('2.not: ')
ortalama = (float(not1) + float(not2)) / 2

sonuc = f"{ad} {soyad} isimli öğrencinin 1. notu {not1} 2. notu {not2} ortalaması {ortalama} olarak hesaplanmıştır."
print(sonuc)
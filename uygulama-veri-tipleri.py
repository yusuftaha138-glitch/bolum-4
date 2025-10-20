# r = float( input("yarıçap:") )
# daireAlani = r * r * 3.14

# daireCevresi = 2 * 3.14 * r 

# print("Dairenin alanı: " + str(daireAlani))
# print("Dairenin çevresi: " + str(daireCevresi))

mesafeKM = input("km giriniz:") 
mesafeMil = float(mesafeKM) / 1.60934
mesafeMil = round(mesafeMil, 2)

print(mesafeKM + " km = " + str(mesafeMil) + " mil eder") 
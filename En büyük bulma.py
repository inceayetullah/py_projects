sayilar = []

while True :
    sayi = float(input("Sayı girin : "))

    sayilar.append(sayi)
    
    if len(sayilar) < 6:

      continue

    else :
       
       break
    
    
print(sayilar)

en_buyuk = sayilar[0]

for i in sayilar :
   
   if i > en_buyuk:
      
     en_buyuk = i

   elif en_buyuk == i :
      
     en_buyuk = i
      


print(en_buyuk)



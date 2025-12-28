print("Vücut Kitle Endeksi Hesaplama (VKI)".center(30 , " "))
kilo = float(input("kilonuzu giriniz: "))
boy = float(input("Boyunuzu giriniz: "))

VKI = (kilo/(boy/100)**2) #VKI hesaplama


print(f"{VKI:.1f}")

if VKI < 18.5 :

    print("Zayıf")

elif VKI >= 18.5 and VKI <25 :
    
    print ("Normal")

elif VKI >=25 and VKI <30 :

    print("Fazla Kilolu")

elif VKI > 30:
    
    print( "Obezite")

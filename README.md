a = 5
b = 10

#Toplama 
toplam = a + b
print("Toplam :" , toplam)
 
#Çıkarma 
cikarma = a - b 
print("Çıkarma :", cikarma)
 
#Çarpma 
carpma = a * b
print("Çarpma :" , carpma)

#Bölme 
bolme = a / b
print("bölme : " , bolme)
 
#Tam Bölme
tamBolme = a // b
print("tamBolme :" , tamBolme)

#Üst Alma
ustAlma = a ** b
print("ustAlma :" , ustAlma)

sayi1 = input("Deger Giriniz : ")

print(type(sayi1))

print(type(int(sayi1)))

print(sayi1 * 5)

print(int(sayi1) * 5)

sayi1 = int(input("Deger Giriniz : "))
sayi2 = int(input("Deger Giriniz : "))
islem = input("İslemi Giriniz : (+, -, *, / , //):")


if sayi1 > sayi2:
    print("sayi1 büyükmüs ")

if sayi2 > sayi1:
    print("sayi2 büyükmüş")
    
if sayi1 == sayi2:
    print("sayılar eşitmiş")

deger = input("Devam etmek için ('e') : ")

if deger.lower() == "e":
    print("girilen deger e imiş")

if islem == "+":
    print("Toplama İsleminin Sonucu : ", (sayi1 + sayi2))

elif islem == "-" :
    print("Çıkarma işleminin sonucu :" , (sayi1 - sayi2))
    
elif islem == "*" :
    print("Çarpma işleminin sonucu :" , (sayi1 * sayi2))
    
elif islem == "/" :
    if sayi2 == 0:
        print("0'a bölünme hatası")
    else:
        print("Bölme işleminin sonucu :" , (sayi1 / sayi2))
            
elif islem == "//" :
    print("Tam bölme işleminin sonucu :" , (sayi1 // sayi2))

elif islem == "**" :
    print("Üs alma işleminin sonucu : " , (sayi1 ** sayi2))
else:
    print("Geçersiz işlem girdiniz")
elif islem == "**" :
    print("Üs alma işleminin sonucu : " , (sayi1 ** sayi2))
else:
    print("Geçersiz işlem girdiniz")
    
    

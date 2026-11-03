# Programlama 1 - ASCII Tablosu Ödevi

# Başlıkları ve çizgiyi hizalı olacak şekilde ayarladık
print(f"{'ASCII Kodu':^10} | {'Karakter'}")
print("-" * 11 + "+" + "-" * 20)

for kod in range(128):  # 0-127 arasındaki kodlar (sayılar) için

    if (0 <= kod <= 31) or (kod == 127):
        karakter = "Kontrol karakteri"  # 0-31 arası ve 127 kontrol karakteri
        
    elif kod == 32:
        karakter = "[boşluk]"  # 32 boşluk karakteri
        
    else:  # Diğer karakterler
        karakter = chr(kod)
        
    # {:^10} ifadesi sayı kaç basamaklı olursa olsun onu 10 karakterlik alanda ortalar
    print(f"{kod:^10} | {karakter}")

    
    

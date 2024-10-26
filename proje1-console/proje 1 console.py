import  modüller.urunler
def urunmenu():

    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║    ÜRÜN LİSTESİ     ║")  
    print("║  1-İçecekler        ║")                                                 
    print("║  2-Meyve            ║")    
    print("║  3-Sebze            ║")
    print("║  4-Bakliyat         ║")
    print("║  5-Süt Ürünleri     ║")              
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    #en az 5 seçim olsun
    # ana menüde en az 5 seçenek olsun

    seçim=input() #input ile string veri alır.
    print("secim,seçtiniz.")

    if seçim=="1":
        print("İçecekler kategorisini seçtiniz.")
        modüller.içecekler.içeceklermenu()
        urunmenu()
    if seçim =="2":    
        print("Meyve kategorisini seçtiniz.")
    if seçim =="3":
        print("Sebze kategorisini seçtiniz.")
    if seçim =="4":
        print("Bakliyat kategorisini seçtiniz.")
    if seçim =="5":
        print("Süt Ürünleri kategorisini seçtiniz.")
urunmenu()
    
# import moduller.içecekler
def urunmenu():

  print("\033[1;32;40m")
  #print("╔"+"═"*20+"╗")
  print("╔═════════════════════╗")
  print("║    ÜRÜN LİSTESİ     ║")  
  print("║  1-kola             ║")                                                  
  print("║  2-soda             ║")    
  print("║  3-şalgam           ║")                                                                                    
  print("║  4-ayran            ║")
  print("║  5-boza             ║")              
  print("║    Seçimiz nedir?   ║")
  print("╚═════════════════════╝")

  #en az 5 seçim olsun
  # ana menüde en az 5 seçenek olsun

  seçim=input() #input ile string veri alır.
  print("seçim,seçtiniz.")

  if seçim=="1":
      print("İçecekler kategorisini seçtiniz.")
      urunler.içecekler.içecekmenu
      urunmenu()
  elif seçim =="2":    
    print("Meyve kategorisini seçtiniz.")
  elif seçim =="3":
    print("Sebze kategorisini seçtiniz.")
  elif seçim =="4":
    print("Bakliyat kategorisini seçtiniz.")
  elif seçim =="5":
    print("Süt Ürünleri kategorisini seçtiniz.")

    
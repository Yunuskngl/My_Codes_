print("******************\n HOŞGELDİNİZ \n******************\n")
print("""
      
işlemler : 
1. bakiye sorgulama
2. para yatırma
3. para çekme

ÇIKIŞ İÇİN q tuşuna basın.      
      
      
""")

bakiye = 10000

while True:
    islem  = input("islemi giriniz: ")
    
    if(islem == "q"):
        print("görüşmek üzere......")
        break
    elif(islem == "1"):
        print("bakiyeniz {} tl'dir".format(bakiye))
    elif(islem == "2"):
        miktar = int(input("yatırmak istediğiniz tutarı giriniz: "))
        bakiye += miktar
    elif(islem == "3"):
        miktar = int(input("çekmek istediğiniz tutarı giriniz: "))
        if(bakiye - miktar < 0):
            print("bu kadar para çekemezsiniz...")
            print("bakiyeniz {} tl'dir".format(bakiye))
            continue
        bakiye -= miktar
    else:
        print("lütfen geçerli bir işlem giriniz: ")

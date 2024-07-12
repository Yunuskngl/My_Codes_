print("******************\n Kullanıcı Girişi \n******************\n")

sys_adı= "yunus"
sys_parola = "12345"

giris_hakkı = 3

while True:
    kullanıcı_adı = input("kullanıcı adı:")
    parola = input("parola:")
    
    if(kullanıcı_adı != sys_adı and parola == sys_parola):
        print("kullanıcı adı hatalı....")
        giris_hakkı-=1
    elif(kullanıcı_adı == sys_adı and parola != sys_parola):
        print("parola yanlışş!!")
        giris_hakkı-=1
    elif(kullanıcı_adı != sys_adı and parola != sys_parola):
        print("lütfen kullancı adını veya parolayı kontrol edin!")
        giris_hakkı-=1
    else:
        print("başarıyla girdiniz...")
        break
    
    if(giris_hakkı == 0) : 
        print("giriiş hakkı doldu... ")
        break
    
    
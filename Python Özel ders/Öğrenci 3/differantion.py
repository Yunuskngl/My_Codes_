def f(x):
    return x ** 2

h = 1e-10

for x in range(100):
    # 1) Türevin limit tanımını hesapla ve değişkene ata
    a = (f(x + h) - f(x)) / h
    # 2) Sonucu iki ondalık basamağa yuvarlayarak yazdır
    print("f'({}) = {} {}".format(x, round(a, 2),1))
    
    #print("f'("+str(x)") = " + str(round(a,2)))




print(type(9))print(type(9.2))print(type("asdadasdas"))print(type('c'))   #type fonksiyonu girilen değişkenin tipini verir.print("hello world")#-------------------------------------------------------------------a = "*selamlar efendim*      "len(a)    #uzunluğu verir.a.upper()   #tüm harfleri büyük harf yapar.a.lower()   #tüm harfleri küçük harf yapar.a.islower()   #tüm harfler küçük mü diye kontrol eder.a.isupper()   #tüm harfler büyük mü diye kontrol eder.a.strip()     #baştaki ve sondaki spaceleri kaldırıyor.a.strip("* ") #baştaki ve sondaki yıldız işaretini kaldırır.a.replace("e","i")   #e harfleri yerine i harflerini getirir.dir(a)   #dir() fonksiyonu ile metodların ne olduğuna bakarız.#-------------------------------------------------------------------t = ("ali","veli",1,2,33,[1,2,3,4])  #tupple yapısı değiştirilemez.t[2:]  #ikinci indexten sonuna kadar yazdırma işlemi#-------------------------------------------------------------------#DICTIONARY dictionary = {"REG" : "REGRESYON",              "LOJ" : "LOJISTIK REGRESYON",              "CART": "CLASSIFICATION AND REG"}len(dictionary)   #6 değildir . 3 tür.dictionary1 = {"word" : {"rge" : 10,                         "sse" : 15,                         "mse" : 17},               "word2": ["gre",20],               "word3": ["erg",30]}   #bu şekilde sözlük oluşturabiliriz.#sözlüklerde index mantığı yoktur. print(dictionary1["word"])print(dictionary["REG"])print(dictionary["LOJ"])print(dictionary["CART"])print(dictionary1["word2"])print(dictionary1["word"]["sse"])dictionary["lbm"] = "bilmiyom anlamini"  #bu şekilde sona eklenir.#!!!!!1 dictionary yapısına list yapısı eklenmez çünkü değiştirilebilir yapıdır.#ancak tuple yapısı eklenebilir.t = ("tuple",)dictionary1[t] = "tuple yapısı ekledik"dictionary1#-------------------------------------------------------------------#SETLER#Değerleri farklı , değiştirilebilir , birden fazla tür içeren ,sırasızlar.#hızlı işlemlerde kullanılır.l = ["ali" , "ata" , "bak" , "ali", "bak"]set1 = set(l)set1  #farkettiysek elemanlar tekrarlamaz.set1.add("ile")      #eleman ekleme görevi yapar.set1.remove("ali")set1.discard("ata")  #ikisi de eleman çıkarma görevi yapar#****************************setnum1 = set([1,4,5])setnum2 = set([2,3,4])setnum1.difference(setnum2)  #set1 de olup set2 de olmayanlar.setnum1 - setnum2           #bu şekilde de yapabiliriz.setnum2.difference(setnum1)  #set2 de olup set1 de olmayan.setnum2 - setnum1           #bu şekilde de yapabiliriz.setnum1.symmetric_difference(setnum2)   #ortak olmayan elemanlar gösterilir.setnum1.intersection(setnum2)  #ortak eleman yani kesişim gösterilir.setnum1.union(setnum2)   #Birleşim kümesini gösterir. setnum1.intersection_update(setnum2)  #kesişim elemanları setnum1 elemanları olur.#sorgu işlemlerisetnum3 = set([7,8,9])setnum4 = set([5,6,7,8,9,10])setnum3.isdisjoint(setnum4)  #iki küme kesişimi boş mu ?setnum3.issubset(setnum4)  #setnum3 setnum4'ün alt kümesi mi?setnum4.issuperset(setnum3)  #set4 set3'ü kapsıyor mu?
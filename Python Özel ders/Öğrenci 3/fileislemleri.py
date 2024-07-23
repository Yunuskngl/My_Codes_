with open("bilgiler.txt","r+") as file :
    file.seek(5)
    file.seek(6)
    icerik = file.read(10)
    print(icerik)
    print(file.tell())



#class 


""""

#bu şekilde tanımlarız ve sadece bu özellikler olur .

class Araba():
    model = "BMW"
    colour = "Gümüş"
    horsePower = 240
    silindir = 8
    

araba1 = Araba()

print(araba1.model)
print(araba1.colour)
print(araba1.horsePower)
print(araba1.silindir)
"""


"""
#bu şekilde fonksiyonlu yaparız.
class Araba():
    def __init__(self,model = "Bilgi yok", colour = "Bilgi yok" ,horsePower = 70 , silindir = 4):
        self.model = model
        self.colour = colour
        self.horsePower = horsePower
        self.silindir = silindir
        
    
araba1 = Araba("MERCEDES-BENZ","Mavi",900,8)

print(araba1.model)
print(araba1.horsePower)
print(araba1.colour)
print(araba1.silindir)
        
        
        
"""
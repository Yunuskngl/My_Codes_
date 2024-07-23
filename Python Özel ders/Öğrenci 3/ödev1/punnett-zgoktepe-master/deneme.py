import random
import matplotlib.pyplot as plt
from collections import namedtuple

Creature = namedtuple("Creature", ["shape", "color"])

def choose_feature(pheno1, pheno2):
    """
    İki fenotipten birer gen seçerek yeni bir fenotip oluşturur.
    """
    return "".join(random.choice(pair) for pair in zip(pheno1, pheno2))

def cross(c1, c2):
    """
    İki yaratığın genetik özelliklerini birleştirir ve yeni bir yaratık oluşturur.
    """
    return Creature(
        shape=choose_feature(c1.shape, c2.shape),
        color=choose_feature(c1.color, c2.color)
    )

def is_green(creature):
    """
    Yaratığın renk fenotipi çekinik (aa) ise True döner.
    """
    return creature.color == "aa"

def is_wrinkled(creature):
    """
    Yaratığın şekil fenotipi çekinik (rr) ise True döner.
    """
    return creature.shape == "rr"

def percentage_green(population):
    """
    Popülasyondaki yeşil yaratıkların yüzdesini hesaplar.
    """
    return sum(is_green(creature) for creature in population) / len(population)

def percentage_wrinkled(population):
    """
    Popülasyondaki buruşuk yaratıkların yüzdesini hesaplar.
    """
    return sum(is_wrinkled(creature) for creature in population) / len(population)

def percentage_green_and_wrinkled(population):
    """
    Popülasyondaki hem yeşil hem de buruşuk yaratıkların yüzdesini hesaplar.
    """
    return sum(is_green(creature) and is_wrinkled(creature) for creature in population) / len(population)

def generation(population):
    """
    Yeni bir nesil yaratıkları üretir.
    """
    new_population = []
    for _ in range(50000):
        parents = random.sample(population, 2)  # Rastgele iki ebeveyn seçilir
        new_population.append(cross(parents[0], parents[1]))  # Ebeveynlerden yeni yaratık oluşturulur
    return new_population

# Başlangıç popülasyonu oluşturuluyor
# Hiçbir bireyin çekinik gen taşımadığı bir popülasyon oluşturulur
population = []
for shape in ["Rr", "RR", "rR"]:
    for color in ["Aa", "AA", "aA"]:
        population.append(Creature(shape=shape, color=color))

# Simülasyon gerçekleştiriliyor
xs = []
green = []
wrinkled = []
both = []
for i in range(10):
    xs.append(i)  # Nesil sayısı
    green.append(percentage_green(population))  # Yeşil yaratık yüzdesi
    wrinkled.append(percentage_wrinkled(population))  # Buruşuk yaratık yüzdesi
    both.append(percentage_green_and_wrinkled(population))  # Hem yeşil hem buruşuk yaratık yüzdesi
    population = generation(population)  # Yeni nesil oluşturuluyor

# Grafikler çiziliyor ve kaydediliyor
plt.plot(xs, green, 'g-')
plt.plot(xs, wrinkled, 'b--')
plt.plot(xs, both, "r--")
plt.savefig('out.png')

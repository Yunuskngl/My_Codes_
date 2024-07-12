def f(x):
    return x ** 2

a = 0
b = 2
DELTA = 1e-5

result = 0
curr = a

while curr < b:
    # 1) Dikdörtgenin genişliği DELTA ve yüksekliği f(curr) olan alanı ekle
    result += f(curr) * DELTA
    # 2) Bir sonraki noktaya geçmek için curr'u güncelle
    curr += DELTA
    

# 3) Sonucu iki ondalık basamağa yuvarlayarak yazdır
print("integral({}, {}) = {}".format(a, b, round(result, 6)))

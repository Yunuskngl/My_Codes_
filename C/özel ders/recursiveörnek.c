/*

1. Faktöriyel Hesaplama
Faktöriyel hesaplama, verilen bir sayının 1'den bu sayıya kadar olan tüm pozitif tam sayıların çarpımını bulur.

#include <stdio.h>

// Faktöriyel fonksiyonu
int faktoriyel(int n) {
    if (n == 0) // Temel durum
        return 1;
    else
        return n * faktoriyel(n - 1); // Rekürsif durum
}

int main() {
    int sayi;
    printf("Bir sayı giriniz: ");
    scanf("%d", &sayi);
    printf("%d! = %d\n", sayi, faktoriyel(sayi));
    return 0;
}

Açıklama:
faktoriyel fonksiyonu, temel durumda n sıfıra eşit olduğunda 1 döndürür.
Temel durum sağlanmazsa, n değerini bir azaltarak fonksiyonu yeniden çağırır ve n ile çarpar.
Bu süreç, n sıfıra ulaşana kadar devam eder.

*/



//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




/*
2. Dizideki En Büyük Elemanı Bulma
Bu fonksiyon, verilen bir dizideki en büyük elemanı bulur.

#include <stdio.h>

// Rekürsif fonksiyon
int enBuyuk(int dizi[], int n) {
    if (n == 1) // Temel durum
        return dizi[0];
    else {
        int max = enBuyuk(dizi, n - 1); // Rekürsif durum
        return (dizi[n - 1] > max) ? dizi[n - 1] : max;
    }
}

int main() {
    int dizi[] = {2, 8, 5, 1, 9, 3};
    int n = sizeof(dizi) / sizeof(dizi[0]);
    printf("Dizideki en büyük eleman: %d\n", enBuyuk(dizi, n));
    return 0;
}


Açıklama:
enBuyuk fonksiyonu, temel durumda dizinin tek elemanı olduğunda bu elemanı döndürür.
Temel durum sağlanmazsa, dizinin bir eksik elemanını içeren alt dizi üzerinde fonksiyonu yeniden çağırır.
Fonksiyon, en son elemanı önceki maksimum değer ile karşılaştırır ve büyük olanı döndürür.




*/


//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



/*3. Diziyi Ters Çevirme
Bu fonksiyon, verilen bir diziyi ters çevirir.

kod : 
#include <stdio.h>

// Rekürsif fonksiyon
void tersCevir(int dizi[], int baslangic, int bitis) {
    if (baslangic >= bitis) // Temel durum
        return;
    
    // Elemanları değiştir
    int temp = dizi[baslangic];
    dizi[baslangic] = dizi[bitis];
    dizi[bitis] = temp;
    
    // Rekürsif çağrı
    tersCevir(dizi, baslangic + 1, bitis - 1);
}

int main() {
    int dizi[] = {1, 2, 3, 4, 5, 6};
    int n = sizeof(dizi) / sizeof(dizi[0]);
    
    printf("Orijinal dizi: ");
    for (int i = 0; i < n; i++)
        printf("%d ", dizi[i]);
    printf("\n");
    
    tersCevir(dizi, 0, n - 1);
    
    printf("Ters çevrilmiş dizi: ");
    for (int i = 0; i < n; i++)
        printf("%d ", dizi[i]);
    printf("\n");
    
    return 0;
}


Açıklama:
tersCevir fonksiyonu, temel durumda başlangıç indeksi bitiş indeksini geçtiğinde durur.
Temel durum sağlanmazsa, başlangıç ve bitiş indekslerindeki elemanları değiştirir.
Sonrasında, başlangıç indeksini bir artırır ve bitiş indeksini bir azaltarak fonksiyonu yeniden çağırır.
Bu süreç, dizinin ortasına kadar devam eder ve dizi ters çevrilmiş olur.
Bu üç örnek, rekürsif fonksiyonların nasıl çalıştığını ve farklı problemlerde nasıl kullanılabileceğini gösterir. Temel durum ve rekürsif çağrı mantığı her bir örnekte farklı şekillerde uygulanmıştır.




*/
#include <iostream>
using namespace std;

/**/
//Bir çiftlikte tavşanların sayısı 1042 iken,kuşların sayısı 2272’dir.Bir yılda tavşanlar %3.8 oranında çoğalırken,kuşlar %1.2 oranında çoğalmaktadır. Tavşanların kuşların sayısını kaç yıl sonra geçeceğini bulan bir C++ programı yazınız.

int main()
{
    int tavsan = 1042;
    int kus = 2272;
    int yil = 0;
    while (kus > tavsan)
    {
        tavsan = tavsan + tavsan * 0.038;
        kus = kus + kus * 0.012;
        yil++;
    }
    cout << yil << endl;
    return 0;
}


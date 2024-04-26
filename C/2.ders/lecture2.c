
#include <stdio.h>
#include <stdlib.h>


int main() {
    int num1 = 5;
    float num2 = 3.5; 
    double num3 = 7.3;  
    char ch = 'B';

/*
    if(ch == 'A'){
        printf("A harfi girildi.\n");
    }
    else if(ch == 'B'){
         printf("B harfi girildi.\n");
    }
    else{
        printf("A, B ve C harflerinden farklı bir harf girildi.\n");
    }


    //switch case yapısı 
    switch (ch) {
        case 'A':
            printf("A harfi girildi.\n");
            break;
        case 'B':
            printf("B harfi girildi.\n");
            break;
        case 'C':
            printf("C harfi girildi.\n");
            break;
        default:
            printf("A, B ve C harflerinden farklı bir harf girildi.\n");
    }*/

    //break yapısı 
/*
    for (int i = 1; i <= 10; i++) {
        if (i ==4) {
            break;
        }
        printf("%d\n", i);
        
    }
*/
    //continue yapısı
    for(int i = 1; i <= 10; i++) {
        if (i == 5) {
            continue;
        }
        printf("%d\n", i);
    }


    return 0;
   
}
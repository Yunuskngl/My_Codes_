#include <stdio.h>
#include <stdlib.h>

int main(){
    int *ad1, *ad2 , *ad;
    int n= 10, p = 20;

    ad1 = &n;
    ad2 = &p;

    printf("atamadan önce ad1 degeri %d \n", *ad1);
    printf("%d\n",ad1);
    *ad1 = *ad2+2;

    printf("atama yaptıktan sonra ad1 degeri %d\n",*ad1);
    printf("%d\n",ad1);

    
}
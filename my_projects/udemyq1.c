#include <stdio.h>
#include <stdlib.h>

//print n times entered sentences in txt file.

int main(){
    FILE *file;
    char sentences[50][50] = {"yunus kodlama calisiyor. ve size selam soyluyor."};
    int hm;
    printf("how many times want write your entered sentence in text:\n");
    scanf("%d",&hm);
    file = fopen("udemyquestion1.txt","w");
    for(int i=0 ; i< hm ; i++){
        for(int j=0; j<50 ; j++){
            fprintf(file,"%s",sentences[j]);
        }
        fprintf(file,"\n");
    }
    fclose(file);
return 0;}
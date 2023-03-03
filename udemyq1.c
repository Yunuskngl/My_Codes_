#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//create information struct of competitor in compatition.

typedef struct{
    char Name[20];
    char Surname[20];
    float scores[10];
    float result;
}competitor_info;
float performance_Score(competitor_info comp){
    int i ;float max , min ; float sum = 0.0 ; 
    max = comp.scores[0];
    min = comp.scores[1];
    for(i=0 ; i<10; i++){
        if(max < comp.scores[i]) max = comp.scores[i];
        if(min > comp.scores[i]) min = comp.scores[i];
        sum = sum + comp.scores[i]; 
    }
    float result =(sum - max - min) / 8 ;
    return result ; 
    

}
int main(){
   /**/ competitor_info competitor1;
    printf("please enter competitor name:\n");
    scanf("%s",&competitor1.Name);
    printf("please enter competitor name:\n");
    scanf("%s",&competitor1.Surname);
    printf("please enter competitor scores:\n");
    for(int i=0 ; i<10 ;i++){
        scanf("%f",&competitor1.scores[i]);
    }
    printf("\n\n\n\n\n");
    competitor1.result = performance_Score(competitor1);
    printf("Name : %s\nSurname : %s\nResult : %.2f",competitor1.Name,competitor1.Surname,competitor1.result);


}
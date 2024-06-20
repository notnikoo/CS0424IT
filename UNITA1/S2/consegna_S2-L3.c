#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){

    int a,b;
    float media;

    printf("Inserire due numeri per farne la media: \n");
    scanf("%d%d", &a, &b);

    media= (float) (a+b)/2;

    printf("La media tra %d e %d è: %.1f", a, b, media);

    return 0;
    

}
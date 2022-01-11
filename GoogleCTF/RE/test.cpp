#include<stdio.h>
#include"include0.h"
#define ROM_3_2 6
#define _LD(x, y) ROM_ ## x ## _ ## y
#define __INCLUDE_LEVEL__ 5
#define LD(x, y) _LD(x, y)
#define Q
int main()
{
    printf("hello\n");
    printf("%d\n",LD(3, 2));
    printf("%d\n", Q);
    return 0;
}
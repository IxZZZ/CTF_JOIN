#include <stdio.h>
#include <stdlib.h>

int main()
{

    for (int i = 0; i < 20000000; i++)
    {
        printf("%d,", rand() % 33);
    }
    return 0;
}

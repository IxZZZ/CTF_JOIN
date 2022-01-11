#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("PATH : %s\n", getenv("PATH"));
    printf("joezidsecret : %s\n", getenv("joezidsecret"));
    printf("ROOT : %s\n", getenv("TEMP"));

    return (0);
}
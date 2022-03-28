/* Infinite loop bug involving the while loop */

#include <stdio.h>      /* printf */

int main(void)
{
    int i = 0;

    while (i <= 10) {
        printf("%d \n", i);
    }

    return 0;
}

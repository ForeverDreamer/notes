/* Infinite loop bug involving the while loop */

#include <stdio.h>      /* Console I/O */

int main(void)
{
    int i = 64;

    while (i = 64) {
        printf("Please enter a number (enter a value different than 64 to quit): ");
        scanf("%d", &i);

        printf("You entered: %d \n\n", i);
    }

    printf("** Loop terminated **");

    return 0;
}

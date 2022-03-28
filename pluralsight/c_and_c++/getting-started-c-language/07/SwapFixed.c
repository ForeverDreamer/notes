/* 
 * Swap function - correct implementation 
 * 
 * by Giovanni Dicanio
 */

#include <stdio.h>

/*
 * Swap the content of the variables pointed by a and b
 */
void Swap(int *a, int *b) 
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int main(void) 
{
    int x = 10;
    int y = 20;

    printf("Initial values: \n x = %d; y = %d \n\n", x, y);

    /* Invoke Swap passing *pointers* to x and y */
    Swap(&x, &y);

    printf("Values after calling Swap: \n x = %d; y = %d \n", x, y);

    return 0;
}

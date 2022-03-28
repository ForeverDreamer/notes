/* 
 * String Length vs. Size
 *  
 * by Giovanni Dicanio
 */

#include <stdio.h>
#include <string.h>

int main(void) {
    printf("Please enter a string: ");

    char str[40];
    scanf("%39s", str);

    int len  = strlen(str);
    int size = sizeof(str);

    printf("\nLength = %d; Size = %d \n", len, size);

    return 0;
}

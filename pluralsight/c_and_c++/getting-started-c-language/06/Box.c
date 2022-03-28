/* Demo: Drawing a box around a string using the for loop */
/* by Giovanni Dicanio                                    */

#include <stdio.h>      /* for printf, putchar */
#include <string.h>     /* for strlen */

int main(void)
{
    char str[] = "Connie is learning C";

    
    /* 
     * Print the string in a box 
     * 
     *           +------- boxWidth
     *           |
     *      <----+--->
     *      |        |
     *      **********    <--- top
     *      * String *    <--- center
     *      **********    <--- bottom
     */
    int boxWidth = strlen(str) + 4; /* 1 asterisk and 1 space for both sides -> 2 + 2 = 4 */

    /* Top */
    for (int i = 0; i < boxWidth; i++) {
        putchar('*');
    }
    putchar('\n');

    /* Center */
    printf("* %s * \n", str);

    /* Bottom */
    for (int i = 0; i < boxWidth; i++) {
        putchar('*');
    }
    putchar('\n');

    return 0;
}

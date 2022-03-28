/* Demo: Underlining a string using the for loop */

#include <stdio.h>      /* for printf, putchar */
#include <string.h>     /* for strlen */

int main(void)
{
    /* String to underline */
    char str[] = "Connie is learning C.";

    /* Print the string */
    printf("%s \n", str);

    /* Print the underline */
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        putchar('-');
    }
    putchar('\n');

    return 0;
}

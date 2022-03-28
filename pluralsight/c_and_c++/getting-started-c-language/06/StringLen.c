/* Demo: while loop in action */

#include <stdio.h>      /* printf */

int main(void)
{
    char str[] = "Connie";
    
    int len = 0;                 /* Current char index               */
    while (str[len] != '\0') {   /* While current char is _not_ null */
        len++;                   /* Update length counter            */
    }

    printf(" String: \"%s\" \n", str);
    printf(" Length: %d chars \n", len);

    return 0;
}

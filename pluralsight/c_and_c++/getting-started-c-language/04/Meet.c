/* 
 * Meet the User - C String I/O Demo
 *  
 * by Giovanni Dicanio
 */

#include <stdio.h>

int main(void) {
    printf("What's your name? ");

    char name[40];
    scanf("%39s", name);

    printf("\n");
    printf("Nice to meet you, %s!\n", name);

    return 0;
}

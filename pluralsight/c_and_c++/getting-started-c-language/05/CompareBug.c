/* Demo: Subtle beginner bug involving if */

#include <stdio.h>      /* For console I/O */

int main(void)
{
    printf(" Please enter an integer number: ");
    int n;
    scanf("%d", &n);

    if (n = 64) {
        printf(" You entered 64. \n");
    } 
    
    return 0;
}

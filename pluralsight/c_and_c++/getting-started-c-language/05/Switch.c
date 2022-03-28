/* Demo: switch */

#include <stdio.h>  /* For console I/O */

int main(void) 
{
    int number;
    printf(" Please enter an integer number: ");
    scanf("%d", &number);

    switch (number) {
    case 1:
        printf(" You entered one. \n");
        break;

    case 10:
        printf(" You entered ten. \n");
        break;

    case 64:
        printf(" You entered sixty-four. \n");
        break;

    default:
        printf(" You entered a number different than 1, 10, 64. \n");
        break;
    }

    return 0;
}

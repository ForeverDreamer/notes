/* Demo: if...else if */

#include <stdio.h>      /* For console I/O */

int main(void)
{
    printf(" Please enter an integer number: ");
    int number1;
    scanf("%d", &number1);

    printf(" Please enter another integer number: ");
    int number2;
    scanf("%d", &number2);

    if (number1 > number2) {
        printf(" number1 > number2 \n");
    } else if (number1 < number2) {
        printf(" number1 < number2 \n");
    } else {
        printf(" number1 == number2 \n");
    }

    return 0;
}

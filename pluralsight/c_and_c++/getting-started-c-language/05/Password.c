/* Demo: if...else */

#include <stdio.h>      /* For console I/O */
#include <string.h>     /* For strcmp */

int main(void)
{
    char password[20];
    printf(" Please enter the password: ");
    scanf("%19s", password);

    if (strcmp(password, "Pluralsight") == 0) {
        printf(" Correct password! \n");
    } else {
        printf(" Wrong password :-( \n");
    }    

    return 0;
}

#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

/*
 IMPORTANT MACROS:
  Each one of these macros determines the different functions/fields which are set on 
  standard library functions and the returned lconv type when calling lcoaleconv().

  LC_ALL      - All functions/fields
  LC_COLLATE  - strcoll and strxfrm STL functions
  LC_CTYPE    - Character functions in STL
  LC_MONETARY - Monetary fields on the lconv type
  LC_NUMERIC  - lconv type fields and decimal-point formatting
  LC_TIME     - strftime STL function

*/


int main(void) {
    struct lconv* my_locale;

    setlocale(LC_MONETARY, "ja_JP");

    my_locale = localeconv();

    printf("Japanese currency symbol: %s\n", my_locale->currency_symbol);

    setlocale(LC_ALL, "");

    my_locale = localeconv();

    printf("Currency symbol from the environment: %s\n", my_locale->currency_symbol);

    return 0;
}


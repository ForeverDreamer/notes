#include <ctype.h>
#include <stdio.h>
#include <string.h>

int to_upper_str(char* str, size_t len);

int main(void) {
    char alphnum_1 = 'a';
    char alphnum_2 = '1';
    printf("Is 'a' alphanumeric: %d\n", isalnum(alphnum_1));
    printf("Is '1' alphanumeric: %d\n", isalnum(alphnum_2));

    printf("Is 'a' alphabetic: %d\n", isalpha(alphnum_1));
    printf("Is '1' alphabetic: %d\n", isalpha(alphnum_2));
    
    printf("Is '1' a decimal digit: %d\n", isdigit(alphnum_2));

    char hex_digit_1 = 'a';
    char hex_digit_2 = 'g';

    printf("Is 'a' a hexadecimal digit: %d\n", isxdigit(hex_digit_1));
    printf("Is 'g' a hexadecimal digit: %d\n", isxdigit(hex_digit_2));

    char lowercase = 'a';
    printf("%d\n", islower(lowercase));

    char uppercase = 'A';
    printf("%d\n", isupper(uppercase));

    char punctuation = ',';
    printf("%d\n", ispunct(punctuation));

    char space = ' ';
    printf("%d\n", isspace(space));

    // backspace, escape, newline.. etc.
    printf("Is a newline character a control character: %d\n", iscntrl('\n'));

    printf("%d\n", isprint(space));

    printf("%d\n", isgraph(space));

    printf("Converted lowercase to uppercase: %c\n", toupper(lowercase));
    printf("Converted uppercase to lowercase: %c\n", tolower(uppercase));

    char uppercase_str_test[] = "Zachary Bennett";
    int converted_chars = to_upper_str(uppercase_str_test, strlen(uppercase_str_test));
    printf("to_upper_str test: %s\n", uppercase_str_test);
    printf("converted chars: %d\n", converted_chars);

    return 0;
}

/**
* Wired Brain Coffee "toupper" extension that will uppercase an entire C string
*/
int to_upper_str(char* str, size_t len) {
    int converted = 0;
    if (len > 0) {
        for (int i = 0; i < len; i++) {
            str[i] = toupper(str[i]);
            converted++;
        }
    }

    return converted;
}

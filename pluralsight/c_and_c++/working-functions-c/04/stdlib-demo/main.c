#include <stdlib.h>
#include <stdio.h>

void my_print_function(void) {
    printf("Exiting!\n");
}

int compare_int(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}


int main(void) {

    /**
     * MEMORY
     **/
    char** dynamic_str_1 = (char**)malloc(sizeof(char) * 8);
    if (dynamic_str_1 != NULL) {
        *dynamic_str_1 = "1234567";
        printf("dynamic_str_1: %s\n", *dynamic_str_1);
    }

    char** dynamic_str_2 = (char**)calloc(8, sizeof(char));
    *dynamic_str_2 = "12";

    dynamic_str_2 = (char**)realloc(dynamic_str_2, sizeof(char) * 3);

    printf("dynamic_str_1: %s\n", *dynamic_str_2);


    free(dynamic_str_1);
    free(dynamic_str_2);


    /**
     * CONVERSION
     **/
    const char* my_int = "457";
    const char* my_long = "234234234";
    const char* my_double = "38.545";
    char* my_str  = "39.5478 is the amount.";
    char** str_out = (char**)malloc(sizeof(my_str));

    int    my_char_conv_1      = atoi(my_int);
    printf("conv: %d \n", my_char_conv_1);
    long   my_char_conv_2      = atol(my_long);
    printf("conv: %li \n", my_char_conv_2);
    double my_char_conv_3      = atof(my_double);
    printf("conv: %f \n\n", my_char_conv_3);

    double   conv_amount_1 = strtod(my_str, str_out);
    printf("conv: %f \n", conv_amount_1);
    printf("conv: %s \n\n", *str_out);

    long conv_amount_2 = strtol(my_str, str_out, 10);
    printf("conv: %li \n", conv_amount_2);
    printf("conv: %s \n\n", *str_out);

    unsigned long conv_amount_3 = strtoul(my_str, str_out, 16);
    printf("conv: %lu \n", conv_amount_3);
    printf("conv: %s \n\n", *str_out);


    /**
     * PROCESS/PROGRAM
     */
    // abort();

    // exit(1);

    atexit(&my_print_function);


    char* my_var = getenv("PATH");
    printf("PATH: %s\n\n", my_var);

    int result = system("echo $PATH");
    printf("\nCall went: %s\n", result == 0 ? "good" : "bad");

    /**
     * ALGORITHM
     **/
    int* matching_item = NULL;
    int item_to_find = 2;
    int items[] = { 1, 2, 3, 4, 5, 6};
    int item_count = 6;

    matching_item = (int*)bsearch(&item_to_find, items, item_count, sizeof(int), &compare_int);

    if (matching_item) {
        printf("Found it: %d\n", *matching_item);
    }

    /**
     * MATH
     **/

    int abs_neg_four = abs(-4);
    printf("\nAbsolute value of negative four: %d\n", abs_neg_four);

    div_t fraction = div(7, 3);
    printf("\nRemainder: %d\n", fraction.rem);

    srand(20);
    int my_random_number = rand();
    printf("\nRandom number: %d\n", my_random_number);

    /**
     * MULTI-BYTE CHARACTER
     *
     * One example is given here as these functions are rarely used.
     **/

    wchar_t my_wide_char_str[] = L"WIDE";
    // This is like writing { L'W', L'I', L'D', L'E' }

    int size = 45;
    char my_multibyte_str[size];
    int count_of_converted_characters = 0;

    count_of_converted_characters = wcstombs(my_multibyte_str, my_wide_char_str, size);

    printf("Converted character count: %d\n\n", count_of_converted_characters);
    printf("Multi-byte string: %s\n\n", my_multibyte_str);
    printf("Multi-byte string length: %d\n\n", mblen(my_multibyte_str, size));



    return 0;
}



#include <errno.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void) {
    printf("Current value of errno: %d\n", errno);

    // Demonstrate using errno with EDOM and ERANGE - create a wired brain coffee wrapper function for these
    double sqrt_of_neg_number = sqrt(-100);

    // Note: This actually doesn't get set! The C standard does not require EDOM be set by math functions
    if (errno == EDOM) {
        printf("%s\n", strerror(errno));
    }

    printf("\nSquare root of -100: %f\n", sqrt_of_neg_number);

    // Instead we can check using the "isnan" macro located in the "math.h" header file
    if (isnan(sqrt_of_neg_number)) {
        printf("%s\n", strerror(errno));
    }

    double log_of_0 = log(0);

    // This doesn't get set on my machine! Does it work on yours?
    if (errno == ERANGE) {
        printf("%s\n", strerror(errno));
    }

    printf("\nLogarithm of 0: %f\n", log_of_0);

    if (!isfinite(log_of_0)) {
        printf("%s\n\n", strerror(errno));
    }

    // EDOM and ERANGE are just two fo the required macros for errno.h to implement on a given platform.
    // For a more complete list of error codes you can check out:
    // https://www.gnu.org/software/libc/manual/html_node/Error-Codes.html

    FILE* nonexistent_file = fopen("not_a_file.txt", "r");
    if (nonexistent_file) {
        printf("The 'not_a_file.txt' file actually does exist...\n");
    }

    if (errno == ENOENT) {
        printf("File not found!\n");
        printf("%s\n", strerror(errno));
    }

    return 0;
}


#include <stdio.h>
#include <math.h>

int main(void) {
    double my_double = 4.5;

    double higher = ceil(my_double);  // 5.0
    double lower  = floor(my_double); // 4.0
    double my_double_positive = fabs(-1 * my_double);  //  4.5

    printf("Ceiling: %f\n", higher);
    printf("Floor: %f\n", lower);
    printf("Absolute value: %f\n", my_double_positive);


    printf("2 to the power of 3: %f\n", pow(2, 3));
    printf("Square root of 9: %f\n", sqrt(9));

    printf("Base-e logarithm of %f: %f\n", my_double, log(my_double));
    printf("e to the power of 5: %f\n", exp(5));

    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SECONDS_ELAPSED(start, end) ((double)(end - start) / CLOCKS_PER_SEC)

typedef struct MyHugeStructure {
    long values_1[65536];
    long values_2[65536];
    long values_3[65536];
    long values_4[65536];
    long values_5[65536];
} MyHugeStructure;

void simulate_pass_by_value(MyHugeStructure test) {

}

void simulate_pass_by_ref(MyHugeStructure* test) {

}

int main(void) {
    MyHugeStructure *my_structure = malloc(sizeof(MyHugeStructure));


    clock_t start_val = clock();
    simulate_pass_by_value(*my_structure);
    clock_t end_val = clock();

    clock_t start_ref = clock();
    simulate_pass_by_ref(my_structure);
    clock_t end_ref = clock();


    double time_spent_by_val = SECONDS_ELAPSED(start_val, end_val);
    double time_spent_by_ref = SECONDS_ELAPSED(start_ref, end_ref);

    printf("Spent %f seconds passing by value\n", time_spent_by_val);
    printf("Spent %f seconds passing by reference\n", time_spent_by_ref);

    return 0;
}

// Credit for grabbing the execution time:
// https://stackoverflow.com/questions/5248915/execution-time-of-c-program

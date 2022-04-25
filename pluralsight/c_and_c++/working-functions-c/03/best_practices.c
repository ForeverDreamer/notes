#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "wbc_lib.h"


extern bool is_cleaning_machine;

void cleanup(CoffeeMachine* a) {

    is_cleaning_machine = true;

    a->status = CLEANING_STATE;

    for (int i = 0; i < a->duration; i++) {
        COLLECT_METRICS_API_CALL();
    }

    free(a);

    is_cleaning_machine = false;
}


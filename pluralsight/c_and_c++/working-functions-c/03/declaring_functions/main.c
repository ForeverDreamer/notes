#include <stdio.h>
#include <stdlib.h>

#include "wbc_lib.h"

// Type Definitions

typedef struct CoffeeMetric {
    int tick;
    int duration;
    double value;
    char* coffee_machine_id;
} CoffeeMetric;

// Function prototypes
static CoffeeMetric*  make_metric(int duration, char* coffee_machine_id);
static void collect_metrics(int duration, CoffeeMetric *metric_collection[duration]);

// This is a public API function
CoffeeMachine* make_coffee_machine(int status, char* serial_number, int duration) {
    CoffeeMachine* machine = (CoffeeMachine*)malloc(sizeof(CoffeeMachine));

    if (machine != NULL) {
        machine->status = status;
        machine->serial_number = serial_number;
        machine->duration = duration;
    }

    return machine;
}

// This should be marked as static - it is an internal API function that is only relevant to this file.
static CoffeeMetric* make_metric(int duration, char* coffee_machine_id) {
    CoffeeMetric* metric = (CoffeeMetric*)malloc(sizeof(CoffeeMetric));

    if (metric != NULL) {
        metric->duration = duration;
        metric->coffee_machine_id = coffee_machine_id;
    }

    return metric;
}

// This should be marked as static - it is an internal API function that is only relevant to this file.
static void collect_metrics(int duration, CoffeeMetric *metric_collection[duration]) {
    for(int i = 0; i < duration; i++) {
        CoffeeMetric *current_metric = metric_collection[i];

        if (current_metric != NULL) {
            current_metric->tick = i;
            current_metric->value = 2.5; // This would call out to another API function to get an actual metric
        }
    }
}

int main(void) {
    int pour_duration = 10;

    CoffeeMachine* machine = make_coffee_machine(1, "ABC123", pour_duration);
    if (!machine) {
        printf("Unable to instantiate coffee machine.\n");
        return 1;
    }

    CoffeeMetric* metrics[pour_duration];
    for (int i = 0; i < pour_duration; i++) {
        metrics[i] = make_metric(machine->duration, machine->serial_number);
    }

    collect_metrics(pour_duration, metrics);

    for (int i = 0; i < pour_duration; i++) {
        printf("Metric: %f\n", metrics[i]->value);
    }

    return 0;
}

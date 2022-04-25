//
// Created by micro on 2022/4/7.
//

#ifndef DECLARING_FUNCTIONS_WBC_LIB_H
#define DECLARING_FUNCTIONS_WBC_LIB_H

typedef struct CoffeeMachine {
    int status;
    char* serial_number;
    int duration;
} CoffeeMachine;

CoffeeMachine* make_coffee_machine(int status, char* serial_number, int duration);

#endif //DECLARING_FUNCTIONS_WBC_LIB_H

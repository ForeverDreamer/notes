/* 
 * Simple Function Example: Convert Temperatures from Fahrenheit to Celsius 
 * 
 * by Giovanni Dicanio
 */

#include <stdio.h>

/*
 * Convert the input temperature from Fahrenheit degrees to Celsius degrees.
 */
float CelsiusFromFahrenheit(float temperatureF) 
{
    /* Convert the temperature value from F to C */
    float temperatureC = (temperatureF - 32.0) * 5.0 / 9.0;

    /* Return the converted value */
    return temperatureC;
}


/*
 * Print a temperature conversion table
 */
int main(void) 
{
    /* Print table header */
    puts("Temperature Conversion Table");
    puts("============================");

    /* Print table values, one row at a time */
    for (float tempF = 10.0; tempF < 100.0; tempF += 5.0) {
        
        /* Convert current temperature value from F to C */
        float tempC = CelsiusFromFahrenheit(tempF);

        /* Print a single row with temperatures values aligned */
        printf(" %.1f F      |      %5.1f C \n", tempF, tempC);
    }
          
    /* Print table footer */
    puts("----------------------------");

    return 0;
}

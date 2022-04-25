#include <stdio.h>
#include <time.h>

/*
    struct tm {
    int tm_sec;         seconds          
    int tm_min;         minutes           
    int tm_hour;        hours (from 0 to 23)
    int tm_mday;        day of the month 
    int tm_mon;         month (from 0 to 11)
    int tm_year;        Number of years since 1900   
    int tm_wday;        day of the week, (from 0 to 6)
    int tm_yday;        day in the year, (from 0 to 365)
    int tm_isdst;       daylight saving time boolean flag
    };
*/

/*
 IMPORTANT MACROS:

    CLOCKS_PER_SEC - This macro expands to the speed of your processor which is measured in clocks per second.

*/

int main(void) {

    // You can optionally pass a valid time_t* to cause the "time()" function to set the argument passed in.
    const time_t my_time = time(NULL); 

    // Local time
    struct tm* local_time = localtime(&my_time);
    printf("Local time day of the month: %d\n\n", local_time->tm_mday);

    // UTC/GMT Time
    struct tm* utc_time = gmtime(&my_time);
    printf("UTC day of the year: %d\n\n", utc_time->tm_yday);

    // Local time as a C string
    char* str_time = ctime(&my_time);
    printf("C string time: %s\n\n", str_time);

    // Day and time string
    char* day_and_time = asctime(local_time);
    printf("Day/Time: %s\n\n", day_and_time);

    // Convert a "tm" struct back to a time_t
    time_t my_next_time = mktime(utc_time);

    // Calculate the difference between two variables of type time_t
    double time_diff_in_sec = difftime(my_time, my_next_time);
    printf("Local time difference from UTC (hours): %f\n\n", time_diff_in_sec / 3600);

    // Create a formatted time string from a "tm" structure
    char my_formatted_time[50];

    /**
      * For a full listing of available formats, please check out this helpful website.
      * https://devhints.io/strftime
     **/
    strftime(my_formatted_time, 50, "%b, %d", local_time);
    printf("Mmm, dd: %s\n", my_formatted_time);

    // clock() returns the number of clock ticks that have happened since the beginning of the program.
    // This is useful for measuring performance of your code!

    clock_t start, end;
    start = clock();

    for(int i = 0; i < 77777777; i++){}

    end = clock();

    printf("Total time taken for loop to run: %f\n", (double)(end - start) / CLOCKS_PER_SEC);


    return 0;
}

/*
    Function Challenge
    void print_month_and_day() {

    }
*/

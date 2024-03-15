#include <stdio.h>                //  printf, gets, scanf
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define STRLEN 200



void lesFraFil(FILE* inn, char* linje);
void delay(int number_of_seconds);

/**
 * Hovedprogrammet:
 * 
 */
int main ()  {
    char linje[STRLEN];

    FILE* innfil;

    innfil = fopen("song.txt", "r");

    if (innfil) {
        
        lesFraFil(innfil, linje);
        while (!feof(innfil)) {
            printf("%s", linje);
            delay(2);
            lesFraFil(innfil, linje);
        }
    } else
        printf("Fant ikke filen 'song.txt'!");


    return 0;
}

void lesFraFil(FILE* inn, char* linje) {
    fgets(linje, STRLEN, inn);    
}

void delay(int number_of_seconds){
    // Converting time into milli_seconds
    int milli_seconds = 1000 * number_of_seconds;
 
    // Storing start time
    clock_t start_time = clock();
 
    // looping till required time is not achieved
    while (clock() < start_time + milli_seconds)
        ;
}
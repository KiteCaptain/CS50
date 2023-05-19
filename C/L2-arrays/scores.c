#include <stdio.h>

// int main(void)
// {
//     int score1 = 72;
//     int score2 = 45;
//     int score3 = 65;

//     printf("Average: %f \n", (score1 + score2 + score3) / (float) 3);

// }
#include <cs50.h>
#include <stdio.h>

// Prototype
float average(int length, int array[]);

const int TOTAL = 3;

int main(void)
{
    int scores[TOTAL];
    // int total = get_int("Total number of scores: ");
    for (int i = 0; i < TOTAL; i++)
    {
        scores[i] = get_int("Score: ");
    }
    printf("Average: %f \n",  average(TOTAL, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum = sum + array[i];
    }
    return (float) sum / (float) length;
}
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string names[] = {"Bill", "Charlie", "Chesner", "Fred",  "George", "Ginny", "Percy", "Ron", "Zack" };
    for (int i = 0 ; i < 9; i++)
    {
       if (strcmp(names[i], "Ron") == 0)
       { 
        printf("Found!\n");
        return 0;
       }
    }
    printf("Not found\n");
    return 1;
}
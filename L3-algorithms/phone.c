#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct 
    {
        string name;
        string number;    
    } 
    person;

const int NUMBER = 2;

int main(void)
{
    // string names[] = {"Bill", "Charlie"};
    // string numbers[] = {"+254714778374", "+24574839485"};
    person people[NUMBER];

    people[0].name = "Kite";
    people[0].number = "+25487326743";

    people[1].name = "Eugine";
    people[1].number = "+25487325343";

    for (int i = 0 ; i < 2; i++)
    {
       if (strcmp(people[i].name, "Eugine") == 0)
       { 
        printf("Found %s\n", people[i].number);
        return 0;
       }
    }
    printf("Not found\n");
    return 1;
}
#include <stdio.h>

// Implementing Linear search
int main(void)
{
    int myarr[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

    for (int i = 0; i < 10; i++)
    {
        if (myarr[i] == 21)
        {
            printf("Found!\n");
            return 0;
        }
        else 
        {
            printf("Not Found!\n");
        }
    }
    printf("Not found In the whole list!\n");
    return 1;
}
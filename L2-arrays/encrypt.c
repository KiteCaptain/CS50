#include <cs50.h>
#include <string.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc < 10)
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            // printf("%s", argv[1]);
            printf("%c", argv[1][i] + 7);
        }
    printf("\n");
    }
    else
    {
        printf("Missing arguments!!\n");
    }
}
// Detects if a file is a jpeg
#include <stdint.h>
#include <stdio.h>

typedef  uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check usage
    if (argc != 2)
    {
        return 1;
    }

    // Open file
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        return 1;
    }
    // return first 3 bytes
    BYTE bytes[3];
    fread(bytes,sizeof(BYTE), 3, file);
    // check first three bytes
    if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff)
    {
        printf("Maybe\n");
    }
    else
    {
        printf("No\n");
    }
}
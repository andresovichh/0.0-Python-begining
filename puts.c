#include <stdio.h>
#include <stdlib.h>

void _puts(char *str)
{
    int i = 0;

    while (str[i] != 0)
    {
        putchar(str[i]);
        i++;
    }
}

int main(void)
{
    _puts("\n");
    _puts("\n hola");
}
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
};

void print_square(int size)
{
    int i = 0;

    while (str[i] != 0)
    {
        putchar("#");
        i++;
    }
    

}


/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    print_square(2);
    print_square(10);
    print_square(0);
    return (0);
}
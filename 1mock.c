#include <stdio.h>
#include <stdlib.h>

void stetstringtoh(char *s, unsigned int size)
{
    int i, j = 0;
   



    if (!s)
    {
        printf("empty string");
    }

    for(i = 0; s[i] != 0; i++)
    {
        if (s[i] == 72)
        {
            while (j <= size)
            {
                printf("%c", 72);

                j++;
                
            }

        }
        
    }
}

int main(void)
{
    

    stetstringtoh("cacaH", 9);

}

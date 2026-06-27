#include<stdio.h>
int main()
{
    int num;

    printf("enter a number to print its table :");
    scanf("%d", &num);

    printf("--- table of %d---\n", num);

    for(int i = 1; i <= 10; i++)
{
    printf("\n%d x %d = %d",num ,i ,num * i);
}

return 0;

}
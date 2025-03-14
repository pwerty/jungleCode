#include <stdio.h>

int main()
{
    int inputA, inputB;

    scanf("%d %d", &inputA, &inputB);

    printf("%d\n", inputA + inputB);
    printf("%d\n", inputA - inputB);
    printf("%d\n", inputA * inputB);
    printf("%d\n", inputA / inputB);
    printf("%d\n", inputA % inputB);

    return 0;
}
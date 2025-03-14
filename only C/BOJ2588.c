#include <stdio.h>

int main()
{
    int inputA, inputB;

    scanf("%d", &inputA);
    scanf("%d", &inputB);

    int _t100, _t10, _t1;
    _t100 = inputB / 100;
    _t10 = inputB / 10 % 10;
    _t1 = inputB % 10;
    // 일부는 구구절절

    printf("%d\n", inputA * _t1);
    printf("%d\n", inputA * _t10);
    printf("%d\n", inputA * _t100);

    printf("%d\n", inputA * inputB);

    return 0;
}
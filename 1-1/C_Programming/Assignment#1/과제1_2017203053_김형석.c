/* ��¥: 2018.03.21
�й�: 2017203053
�̸�: ������
������Ʈ: �ܵ� ��� ���α׷�
*/
#include <stdio.h>

int main(void)
{
	int rest,numA, numB, num5000, num1000, num500, num100, num50, num10, num5, num1;

	printf("��ǰ ���� �Է�(1~10000): ");
	scanf("%d", &numA);

	printf("���ұݾ� �Է�(1~10000): ");
	scanf("%d", &numB);

	/* num5000 = (numB - numA) / 5000;
	num1000 = (numB - numA) % 5000 / 1000;
	num500 = (numB - numA) % 5000 % 1000 / 500;
	num100 = (numB - numA) % 5000 % 1000 % 500 / 100;
	num50 = (numB - numA) % 5000 % 1000 % 500 % 100 / 50;
	num10 = (numB - numA) % 5000 % 1000 % 500 % 100 % 50 / 10;
	num5 = (numB - numA) % 5000 % 1000 % 500 % 100 % 50 % 10 / 5;
	num1 = (numB - numA) % 5000 % 1000 % 500 % 100 % 50 % 10 % 5 / 1; */

	rest = numB - numA;
	num5000 = rest / 5000;
	rest %= 5000;
	num1000 = rest / 1000;
	rest %= 1000;
	num500 = rest / 500;
	rest %= 500;
	num100 = rest / 100;
	rest %= 100;
	num50 = rest / 50;
	rest %= 50;
	num10 = rest / 10;
	rest %= 10;
	num5 = rest / 5;
	rest %= 5;
	num1 = rest / 1;

	printf("-5000��: %d�� \n", num5000);
	printf("-1000��: %d�� \n", num1000);
	printf("-500��: %d�� \n", num500);
	printf("-100��: %d�� \n", num100);
	printf("-50��: %d��, ", num50);
	printf("10��: %d��, ", num10);
	printf("5��: %d��, ", num5);
	printf("1��: %d�� \n", num1);

	return 0;
}
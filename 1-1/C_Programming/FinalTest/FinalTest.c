/* C���α׷��� 2018-1 �⸻��� ���� ����
* main �Լ� �� �Լ������� ���� �������� ����, main �Լ� �ϴ��� �� �Լ����� �ϼ��� ��!
* �� �Լ����� ��������� �ݵ�� �ؼ��� ��!
* ���� ���� ���õ� �Լ��� �׿�  �°� ������ �Լ� �ϼ��� ��.
* ���� ���� ��, 0���̸� �κ� ���� ����.
* ��� �ۼ� ��, "�й�-�̸�.c" ������ U-ķ�� �����ϰ� ������ Ȯ�� �� ���.
*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void printSum1To1000(void);
int Factorial(int);
void covert2Low(char*);
void AvgOfArray(double*);
void my_strcpy(char *, char *);
void printGugudan2_5_8();

int main(void)
{
	int num;
	double arr[] = { 1.2, 3.5, 7.4, 0.5, 10.0 };
	char str[16];
	char des[60] = { '\0' };

	printf("����1 �Լ� ȣ�� ����\n");
	//1����: �ݺ����� �̿��ؼ� 1���� 1000������ ������ ����ؼ� ����ϴ� �Ʒ��� �Լ� �ϼ� 
	printSum1To1000();//5��

	printf("����2 �Լ� ȣ�� ����\n");
	//2 ����: ������ ���� ������ �Է� �� ���ڷ� ���޹޾Ƽ� �Ʒ��� ���� ���丮���� ����ϵ��� 
	//����Լ��� ������ Factorial �Լ��ϼ�.
	scanf("%d", &num);
	printf("%d! = %d \n", num, Factorial(num)); //6��

	printf("����3 �Լ� ȣ�� ����\n");
	//3 ����: ���� ���ڿ��� �Է� �޾Ƽ�, ���� �迭 str�� �����ϰ�, �빮�ڸ� ã�� �ҹ��ڷ� �ٲٴ� �Ʒ��� �Լ� �ϼ�.
	covert2Low(str);//6��
	printf("%s\n\n\n", str);

	printf("����4 �Լ� ȣ�� ����\n");
	//4 ����: ���� �ʱ�ȭ�� �迭 ������ ����� ���ؼ� �Ҽ� ��°�ڸ� ����ϴ� �Ʒ��� �Լ� �ϼ�.
	AvgOfArray(arr);//6��

	printf("����5 �Լ� ȣ�� ����\n");
	//5 ����: ���� ����� �迭 des�� "Hello World"�� �����ϴ� �Ʒ��� �Լ� �ϼ�
	my_strcpy(des, "Hello World");//6��
	printf("%s \n", des);

	printf("����6 �Լ� ȣ�� ����\n");
	//6 ����: ������ �߿��� 2��, 5��, 8���� ��ø �ݺ����� ����Ͽ� ���� ���� ���� ����ϴ� 
	//printGugudan2_5_8 �Լ� �ϼ�
	printGugudan2_5_8();//6��

	printf("\n Acknowledgement\n");
	printf("��� ���б� ���� ���� ������...\n");

	return 0;
}

//���� 1
void printSum1To1000(void)
{
	int i;
	int sum = 0;
	for (i = 1; i <= 1000; i++)
		sum += i;
	printf("%d\n", sum);
	
}

//����2
int Factorial(int n)
{//�ݵ�� ���ȣ��� �ۼ�
	if (n == 0)
		return 1;
	else
		return n*Factorial(n - 1);
}

//����3: Hint-> A~Z�� �ƽ�Ű�ڵ尪�� 65~90, a~z�� �ƽ�Ű�ڵ尪�� 97~122
void covert2Low(char *pStr)
{
	int i;
	int len = 0;

	scanf("%s", pStr);
	
	while (pStr[len] != '\0')
		len++;
	for (i = 0; i < len; i++)
	{
		if (pStr[i] >= 65 && pStr[i] <= 90)
			pStr[i] += 32;
		else if (pStr[i] >= 97 && pStr[i] <= 122)
			pStr[i] -= 32;
	}
}

//����4
void AvgOfArray(double *ptr)
{
	int i;
	double mean = 0;
	double sum = 0;
	
	for (i = 0; i < 5; i++)
		sum += ptr[i];
	mean = sum / i;
	printf("%.2lf\n", mean);
}

void my_strcpy(char *p1, char *p2)
{//���̺귯�� �Լ� ������� �� ��!!!
	int i;
	int len=0;

	while (p2[len] != '\0')
		len++;

	for (i = 0; i < len; i++)
		p1[i] = p2[i];


}
// ����6
void printGugudan2_5_8()
{/*���� ��)
 2x1= 2 5x1= 5 8x1= 8
 ...
 2x8=16 5x8=40 8x8=64
 2x9=18 5x9=45 8x9=72
 */
	int i;
	int j;
	int a=0;
	for (i = 1; i < 10; i++)
	{
		for (j = 2; j < 10; j = j + 3)
		{
			printf("%dx%d= %2d ", j, i, j*i);
			a++;
			if (a % 3 == 0)
				printf("\n");
		}
	}

}
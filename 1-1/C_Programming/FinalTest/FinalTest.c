/* C프로그래밍 2018-1 기말고사 문제 파일
* main 함수 및 함수원형은 절대 수정하지 말고, main 함수 하단의 각 함수들을 완성할 것!
* 각 함수별로 제약사항을 반드시 준수할 것!
* 실행 예가 제시된 함수는 그에  맞게 각각의 함수 완성할 것.
* 빌드 에러 시, 0점이며 부분 점수 없음.
* 답안 작성 후, "학번-이름.c" 파일을 U-캠에 제출하고 감독자 확인 후 퇴실.
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

	printf("문제1 함수 호출 시작\n");
	//1문제: 반복문을 이용해서 1부터 1000까지의 총합을 계산해서 출력하는 아래의 함수 완성 
	printSum1To1000();//5점

	printf("문제2 함수 호출 시작\n");
	//2 문제: 임의의 양의 정수를 입력 및 인자로 전달받아서 아래와 같이 팩토리얼을 출력하도록 
	//재귀함수로 구현된 Factorial 함수완성.
	scanf("%d", &num);
	printf("%d! = %d \n", num, Factorial(num)); //6점

	printf("문제3 함수 호출 시작\n");
	//3 문제: 영문 문자열을 입력 받아서, 위의 배열 str에 저장하고, 대문자를 찾아 소문자로 바꾸는 아래의 함수 완성.
	covert2Low(str);//6점
	printf("%s\n\n\n", str);

	printf("문제4 함수 호출 시작\n");
	//4 문제: 위에 초기화한 배열 원소의 평균을 구해서 소수 둘째자리 출력하는 아래의 함수 완성.
	AvgOfArray(arr);//6점

	printf("문제5 함수 호출 시작\n");
	//5 문제: 위에 선언된 배열 des에 "Hello World"를 복사하는 아래의 함수 완성
	my_strcpy(des, "Hello World");//6점
	printf("%s \n", des);

	printf("문제6 함수 호출 시작\n");
	//6 문제: 구구단 중에서 2단, 5단, 8단을 중첩 반복문을 사용하여 실행 예와 같이 출력하는 
	//printGugudan2_5_8 함수 완성
	printGugudan2_5_8();//6점

	printf("\n Acknowledgement\n");
	printf("모두 한학기 동안 수고 많았음...\n");

	return 0;
}

//문제 1
void printSum1To1000(void)
{
	int i;
	int sum = 0;
	for (i = 1; i <= 1000; i++)
		sum += i;
	printf("%d\n", sum);
	
}

//문제2
int Factorial(int n)
{//반드시 재귀호출로 작성
	if (n == 0)
		return 1;
	else
		return n*Factorial(n - 1);
}

//문제3: Hint-> A~Z의 아스키코드값은 65~90, a~z의 아스키코드값은 97~122
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

//문제4
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
{//라이브러리 함수 사용하지 말 것!!!
	int i;
	int len=0;

	while (p2[len] != '\0')
		len++;

	for (i = 0; i < len; i++)
		p1[i] = p2[i];


}
// 문제6
void printGugudan2_5_8()
{/*실행 예)
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
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h> // 루트계산을 위한 헤더파일 선언

int main()
{
	int seat[10] = { 0 }, i, k; // 7장 7번 변수 seat[10] = 좌석상태를 저장할 배열, i = 반복을 위한 변수, k = 좌석 번호
	int a = 0; // 채워진 좌석 수를 나타내는 변수
	char ans; // 7장 7번 변수 ans = 좌석 예약 y or n

	double mean, s, num[5], mean2, mean3, sum, sum2; // 7장 8번 변수 mean = 평균 , s = 표준편차, num[5] = 실수를 저장할 배열, mean2 = 제곱의 평균, mean3 = 평균의 제곱
	int j = 0; // 7장 8번 변수 j = 반복을 위한 변수
	int check; // 입력한 값의 형식을 체크하기 위한 변수

	mean = 0;
	s = 0; // 표준 편차 = 분산의 제곱근 = (제곱의 평균 - 평균의 제곱)의 제곱근
	sum = 0; // 7장 8번 입력값들의 합
	sum2 = 0; // 7장 8번 입력값들의 제곱의 합 

	printf("7장 7번 문제 시작......\n");

	for (;;)
	{
		printf("좌석을 예약하시겠습니까?(y 또는 n) ");
		scanf(" %c", &ans);
		if (a == 10) // y 입력 후 빈 자리가 없을 때 출력
		{
			printf("만석입니다.\n");
			break;
		}

		printf("------------------------------\n");

		if (ans == 'n') // 좌석 예약 입력에 n 입력 시 프로그램 종료
			break;

		for (i = 1; i < 11; i++) // 좌석 번호 1~10번 출력
			printf("%3d", i);
		printf("\n");
		printf("------------------------------\n");

		for (i = 0; i < 10; i++) // 좌석 예약 현황 출력
			printf("%3d", seat[i]);
		printf("\n");


		if (ans == 'y') // 좌석 예약 입력에 y 입력 시 예약 진행
		{
			printf("몇번째 좌석을 예약하시겠습니까? ");
			scanf("%d", &k);



			if (seat[k - 1] == 0) // 입력한 좌석 번호가 빈 자리 일때
			{
				seat[k - 1] = 1;
				a++;
				printf("예약되었습니다.\n");
			}
			else if (seat[k - 1] == 1) // 입력한 좌석 번호가 빈 자리가 아닐 때
				printf("입력하신 좌석은 이미 예약된 좌석입니다.\n");
			else if (k < 0 && k>11) // 입력한 좌석 번호가 현재 준비된 좌석의 번호에 포함이 안될 때
				printf("입력하신 좌석 번호가 없습니다. 다시 입력해주세요.\n");
		}
		else // 좌석 예약 입력 시 y 또는 n 이외의 값을 입력했을 때
			printf("잘못 입력하셨습니다. y 또는 n 을 입력해주세요.\n");

	}
	printf("\n\n");

	printf("7장 8번 문제 시작......\n");

	for (j = 0; j < 5; j++) // 5번 입력을 위한 반복문
	{
		printf("실수를 입력하시오: ");
		check = scanf("%lf", &num[j]);

		if (check == 1) // 입력한 값이 형식과 일치하는 갯수 -> 입력한 값이 실수일 때 scanf함수에서 1 반환
		{

			sum += num[j]; // 평균을 구하기 위한 입력된 실수들의 합
			sum2 += num[j] * num[j]; // 제곱의 평균을 구하기 위한 입력된 실수들의 제곱의 합
		}
		else // 입력한 값이 실수가 아닐 때
		{
			printf("실수를 다시 입력하세요.\n");
			j = j - 1;
			getchar(); // scanf 함수의 저장장소 buffer 속에 있는 \n을 지워주는 역할
		}						
	}

	mean = sum / 5; // 평균
	mean2 = sum2 / 5; // 제곱의 평균
	mean3 = mean * mean; // 평균의 제곱
	s = sqrt(mean2 - mean3); // 분산 = 제곱의 평균 - 평균의 제곱 , 표준편차 = 분산의 제곱근
	printf("평균 : %lf\n", mean);
	printf("표준편차 : %lf\n", s);

	return 0;
}
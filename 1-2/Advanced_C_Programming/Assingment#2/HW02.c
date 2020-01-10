/*
  File Name : C Programming Assignment #2
  Name : Hyoung Seok Kim
  Student Number : 2017203053
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>



void swap(int* a, int* b);
void QuickSort(int *arr, int start, int end);
int main() {
	int class[50][3];
	int i, j;
	int sum[50] = { 0 };
	int arr[3];
	int pivot;


	srand((unsigned)time(NULL)); // Step 1

	for (i = 0; i < 50; i++) {
		for (j = 0; j < 3; j++) {
			class[i][j] = rand() % 101; // 0~100 ������ ������ �� ����
			sum[i] += class[i][j];
		}
	}
	for (i = 0; i < 50; i++) { // Step 2
		printf("�й� : %2d, ", i + 1);
		for (j = 0; j < 3; j++)
			printf("���� %2d ���� = %3d, ", j, class[i][j]);
		printf("��� ���� = %lf\n", (double)sum[i] / 3);
	}
	printf("\n");
	printf("���������� ����� ���� ��ȣ �Է� : "); // Step 3

	scanf("%d", &pivot);
	printf("\n");
	for (i = 0; i < 50; i++) {
		for (j = 0; j < 3; j++)
			arr[j] = class[i][j];
		swap(&arr[pivot], &arr[0]);

		QuickSort(arr, 0, 2); // ������ �̿�

		for (j = 0; j < 3; j++)
			class[i][j] = arr[j];
	}
	for (i = 0; i < 50; i++) {
		printf("�й� : %2d, ", i + 1);
		for (j = 0; j < 3; j++)
			printf("���� %2d ���� = %3d, ", j, class[i][j]);
		printf("��� ���� = %lf\n", (double)sum[i] / 3);
	}
	return 0;
}

void swap(int *a, int *b) {
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

void QuickSort(int *arr, int start, int end) {
	int pivo = arr[start];
	int left = start + 1;
	int right = end;

	while (left <= right) {
		while (arr[left] < pivo)
			left++;
		while (arr[right] > pivo)
			right--;
		if (left <= right) {
			swap(&arr[left], &arr[right]);
		}
	}
	if (start < end) {
		swap(&arr[start], &arr[right]);

		QuickSort(arr, start, right - 1);
		QuickSort(arr, right + 1, end);
	}
}

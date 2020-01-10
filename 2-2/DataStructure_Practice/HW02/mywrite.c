/*
 * Student ID: 2017203053
 * Name: 김형석
 */
#include "MyStudent.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>

#define PERMS 0644

int main(int argc, char const *argv[]) {
    /* 아래에 코드를 작성하세요. */
	int fd=0; // file descriptor 초기 0
	char * pathName="./student.dat";
	
	ssize_t wSize = 0;

	char studentID[MAX_ID_SIZE + 1] = {'\0',};
	char studentName[MAX_NAME_SIZE + 1] = {'\0',};
	int studentScore=0;

	// 정보 담기 위한 구조체 생성 및 초기화
	Student * student=(Student *)malloc(sizeof(Student));
	memset(student->id,'\0',MAX_ID_SIZE + 1);
	memset(student->name,'\0',MAX_NAME_SIZE + 1);
	student->score=0;

	printf("ID: ");
	scanf("%[^\n]",studentID); // \n 제외한 모든 문자열 입력받음
	strcpy(student->id,studentID); // 구조체에 복사
	
	getchar();

	printf("Name: ");
	scanf("%[^\n]",studentName);
	strcpy(student->name,studentName);

	

	printf("Score: ");
	scanf("%d",&studentScore);
	student->score=studentScore;

	// 사용자 정보를 담기 위한 파일 생성
	fd=open(pathName,O_CREAT|O_APPEND|O_WRONLY,PERMS);
	if(fd == -1){
		perror("open() error!");
		exit(-1);
	}

	// 사용자 정보를 파일에 쓰기
	wSize = write(fd,(Student *)student, sizeof(Student));

	if(wSize == -1){
		perror("write() error!");
		exit(-2);
	}

	close(fd);
	free(student);


		
    return 0;
}

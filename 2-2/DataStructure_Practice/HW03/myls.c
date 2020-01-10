/*
 * Student ID: 2017203053
 * Name: 김 형 석
 */
#include <fcntl.h>
#include <pwd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <dirent.h>

#define MAX_PATH_LEN 1024

void myError(const char * msg);
void fileType(const struct stat * fileInfo);
void fileMode(const struct stat * fileInfo);

int main(int argc, char *argv[]) {
    /* 아래에 코드를 작성하세요. */
    struct stat fileInfo;
	struct passwd * userInfo;
	DIR * dirp;
	struct dirent * dirInfo;
	char cwd[MAX_PATH_LEN+1]={'\0',};
	
	if(argc != 2){
		printf("Usage: %s [pathname]\n",argv[0]);
		exit(-1);
	}
	
	if(chdir(argv[1])==-1){
			myError("chdir() error!");
			exit(-1);
			}
	if(getcwd(cwd,MAX_PATH_LEN)==NULL){
		myError("getcwd() error!");
		exit(-1);
	}
	printf("Directory to serarch: %s\n",argv[1]);

	dirp=opendir(cwd);
	while((dirInfo=readdir(dirp))!=NULL){
		
	    stat(dirInfo->d_name,&fileInfo);
	    userInfo=getpwuid(fileInfo.st_uid);
	    fileType(&fileInfo);
	    fileMode(&fileInfo);
    	    printf("%15s%15ld%15ld  %-20s\n",userInfo->pw_name,fileInfo.st_size,fileInfo.st_mtime,dirInfo->d_name);
	    
	    
		
	}

	closedir(dirp);


    return 0;
}

void myError(const char * msg){
    perror(msg);
    exit(-1);
}
void fileType(const struct stat * fileInfo){
    if(S_ISREG(fileInfo->st_mode))
		printf("-");
    else if(S_ISDIR(fileInfo->st_mode))
		printf("d");
    else if(S_ISCHR(fileInfo->st_mode))
		printf("c");
    else if(S_ISBLK(fileInfo->st_mode))
		printf("b");
    else if(S_ISLNK(fileInfo->st_mode))
		printf("l");
    else if(S_ISSOCK(fileInfo->st_mode))
		printf("s");
    else
		printf("?");
	
}
void fileMode(const struct stat * fileInfo){
	// User
	if(S_IRUSR & fileInfo->st_mode)
		printf("r");
	else
		printf("-");

	if(S_IWUSR & fileInfo->st_mode)
		printf("w");
	else
		printf("-");

	if(S_IXUSR & fileInfo->st_mode)
		printf("x");
	else
		printf("-");

	// Group
	if(S_IRGRP & fileInfo->st_mode)
		printf("r");
	else
		printf("-");

	if(S_IWGRP & fileInfo->st_mode)
		printf("w");
	else
		printf("-");

	if(S_IXUSR & fileInfo->st_mode)
		printf("x");
	else
		printf("-");

	// Others
	if(S_IROTH & fileInfo->st_mode)
		printf("r");
	else
		printf("-");
	
	if(S_IWOTH & fileInfo->st_mode)
		printf("w");
	else
		printf("-");

	if(S_IXOTH & fileInfo->st_mode)
		printf("x");
	else
		printf("-");

}

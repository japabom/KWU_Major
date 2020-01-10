/*
 * Student ID: 2017203053
 * Name: 김형석
 */
#include "MyStudent.hpp"
#include <fcntl.h>
#include <iostream>
#include <list>
#include <string>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

using namespace std;

int main(void) {
    /* 아래에 코드를 작성하세요. */
    list<Student> stuList;
    list<Student>::iterator iter;
    int i=1;
    int fd=0;
    string filepath="./StudentList.dat";
    Student* inputArr=new Student;

    fd=open(filepath.c_str(),O_RDONLY,0644);
    if(fd==-1){
        perror("open() error!");
        return 1;
    }

    int rsize;

    do{
        rsize=read(fd, inputArr, sizeof(Student));
        if(rsize==-1){
            perror("write() error");
            return 2;
        }
        if(rsize==0)
            break;
        stuList.push_back(*inputArr);

    }while(rsize>0);
    for(iter=stuList.begin();iter!=stuList.end();++iter) {
        cout << i << "번째 학생 정보" << endl;
        cout << "ID: " << iter->getId() << ", Name: " << iter->getName() << ", Score: " << iter->getScore()<<endl;

        i++;
    }
    delete[] inputArr;

    close(fd);
    return 0;
}

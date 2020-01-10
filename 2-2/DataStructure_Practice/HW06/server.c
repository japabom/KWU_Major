/*
 * Student ID : 2017203053
 * Name : hyung seok Kim
 */
#include "MyShm.h"
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <unistd.h>

#define MAX_SHM_SIZE 512

void signalHandler(int signum);
int calculate(Calc calc);
void myfunc(void);

key_t mykey = 0;
int shmid = 0;
int *shmaddr = NULL;

int main(int argc, char const *argv[]) {
    mykey = ftok("mykey", 2);
    shmid = shmget(mykey, MAX_SHM_SIZE, IPC_CREAT | 0644);
    shmaddr = shmat(shmid, NULL, 0);
    signal(SIGINT, signalHandler);
    signal(SIGUSR1, signalHandler);
    while (1) {
        puts("Wait ...");
        pause();
    }
    return 0;
}
void signalHandler(int signum) {
    struct shmid_ds buf;
    if (signum == SIGINT) {
        shmdt(shmaddr);
        shmctl(shmid, IPC_RMID, NULL);
        exit(0);
    }
    else if (signum == SIGUSR1) {
        myfunc();
    }
}
int calculate(Calc calc) {
    switch (calc.op) {
        case '+':
            return calc.x + calc.y; case '-':
            return calc.x - calc.y;
        case '*':
            return calc.x * calc.y;
        case '/':
            return (int)(calc.x / calc.y);
        default:
            return 0;
    }
}
void myfunc(void) {
    struct shmid_ds buf;
    Calc shmCalc;
    int result=0;
    memcpy(&shmCalc, shmaddr, sizeof(Calc));
    printf("Receive: %d %c %d\n", shmCalc.x, shmCalc.op,shmCalc.y);
    result=calculate(shmCalc);
    memcpy(shmaddr, &result, sizeof(int));
    printf("Send: %d\n", result);
    shmctl(shmid, IPC_STAT, &buf);
    kill(buf.shm_lpid, SIGUSR1);
}

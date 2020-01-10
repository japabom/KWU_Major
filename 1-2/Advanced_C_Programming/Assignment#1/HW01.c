/*
    File Name : C Programming assignment #1
    Student Number : 2017203053
    Name : Kim Hyoung Seok
 */

#include <stdio.h>
#include <stdlib.h>

int size; // global variable - width of 2d array

int introtateArray(int *x[size], int degree); // int x[][size]

int main(){

    int **arr; // 2 dimensional array variable
    int i,j; // variable for for loop
    int max; // for escape while loop
    int x=0;
    int y=0;
    int count=1; // variable for write numbers
    int degree;

    printf("Please input size of array : ");  // input width of array
    scanf("%d",&size);

    arr=(int**)malloc(sizeof(int*)*size); /* The malloc() function allocates size bytes and returns a pointer to
                                             the allocated memory */

    for(i=0;i<size;i++){
        arr[i]=(int*)malloc(sizeof(int)*size);
    }

    max=size*size; // initial condition for escape while loop

    while(max>0){ // Snail array
        for(i=y;i<size-x;i++){
            arr[x][i]=count;
            count+=1;
            max-=1;
        }
        y+=1;
        for(i=y;i<size-x;i++){
            arr[i][size-x-1]=count;
            count+=1;
            max-=1;
        }
        for(i=size-y-1;i>=x;i--){
            arr[size-x-1][i]=count;
            count+=1;
            max-=1;
        }
        x+=1;
        for(i=size-y-1;i>=x;i--){
            arr[i][x-1]=count;
            count+=1;
            max-=1;
        }

    }
    for(i=0;i<size;i++){    // print array
        for(j=0;j<size;j++){
            printf("%3d",arr[i][j]);
        }
        printf("\n");
    }


    printf("Please input angle of rotation : "); // input angle of rotation
    scanf("%d",&degree);
    if(introtateArray(arr,degree)==1) { // if the return value of function called introtateArray is 1, rotate the Array.
        switch (degree / 90) { // if degree is 90 or 180 or 270, rotate the Array.
            case 1: // rotate 90 degrees.
                break;
            case 2: // rotate 180 degrees.
                introtateArray(arr, degree);
                break;
            case 3: // rotate 270 degrees.
                introtateArray(arr, degree);
                introtateArray(arr, degree);
                break;
        }
    }
    else // if degree is not 90 or 180 or 270, don't rotate the Array.
        printf("Nothing happened\n");
    for (i = 0; i < size; i++) {    // After all, for check the values of the Array.
        for (j = 0; j < size; j++) {
            printf("%3d", arr[i][j]);
        }
        printf("\n");
    }

    for(i=0;i<size;i++){ // free the previously allocated memory
        free(arr[i]);
    }
    free(arr);

    return 0;
}

int introtateArray(int *x[size], int degree) {
    int i;
    int max=size*size;
    int col=0;
    int row=0;
    int *temp;

    temp= (int *) malloc(sizeof(int) * (size)); // for save the first column
    if(degree==90 || degree==180 || degree == 270) {
        while (max > 0) {
            for (i = col; i < size - col; i++) {
                temp[i] = x[row][i];
            }
            for (i = col; i < size - col; i++) {
                x[row][i] = x[size - i - 1][col];
                max -= 1;
            }
            row += 1;
            for (i = size - row; i > row - 1; i--) {
                x[i][col] = x[size - row][i];
                max -= 1;
            }
            col += 1;
            for (i = size - col; i > col - 1; i--) {
                x[size - row][i] = x[size - i - 1][size - col];
                max -= 1;
            }
            for (i = row - 1; i < size - row + 1; i++) {
                x[i][size - col] = temp[i];
                max -= 1;
            }


        }
        free(temp); // free the previously allocated memory
        return 1;
    }
    else {
        free(temp); // free the previously allocated memory
        return 0;
    }
}
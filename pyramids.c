#include <stdio.h>
#include <stdlib.h>

void printSpaces(int row_count, int column){
    for(int col=column;col<row_count;col++){
            printf(" ");
        }
}

void printStars(int row_count){
    for(int columns =1;columns <= (2*row_count)-1;columns++){
            printf("*");
        }

}

int main(){
    int row_count;
    printf("Enter the number of rows for the triangle: ");
    scanf("%d", &row_count);
    for(int row_num = 1; row_num <= row_count; row_num++){
        

        printSpaces(row_count, row_num);
        printStars(row_num);

        printf("\n");

    }
    return 0;
}


#include <stdio.h>
#include <stdlib.h>


void doTriangle(int row_count){
    for(int rows = 1; rows <= row_count; rows++){
        for(int columns = 0; columns < rows ; columns++){
            printf("*");
        }
        printf("\n");
    }
 
}


int main(){
    int row_count;
    printf("Enter the number of rows for the triangle: ");
    scanf("%d", &row_count);
    doTriangle(row_count);
    return 0;
}


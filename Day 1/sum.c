#include <stdio.h>
#include <stdlib.h>

void adder(char *num1,char *num2);

int main(){
    char num1[1000000], num2[1000000];
    printf("first num: ");
    scanf("%s", num1);

    printf("second num: ");
    scanf("%s", num2);
    adder(num1,num2);


}

void adder(char *num1,char *num2){
    int size1 = strlen(num1);
    int size2 = strlen(num2);
    char *big, *small;
    
    int size, sm, bound = 0;

    if(num1[0]==num2[0] && num1[0]=='-'){
        bound = 1;
    }

    if(size1>= size2){
        big = num1;
        small = num2;
        size = size1;
        sm = size2;
    }
    else{
        big = num2;
        small = num1;
        size = size2;
        sm = size1;
    }

    char sum[size];
    int carrySum = 0;
    int i;
    int dif = size - sm;

    for(i = size -1; i>= bound; i--){

        if(i-dif < bound){
            
           int sum_int = (big[i] - '0') + carrySum;
            carrySum = 0;
            sum[i] = (sum_int + carrySum) + '0';

        }
        else{

            int sum_int = (big[i] - '0') + (small[i-dif] - '0');
        if( sum_int > 9){
            int to_carry = sum_int;
            sum_int = sum_int % 10;
            sum[i] = (sum_int + carrySum) + '0';

            carrySum = to_carry / 10;
             
                
        }
        else{
            sum_int = sum_int + carrySum;
            sum[i] = (sum_int) + '0';
            carrySum = 0;
        }
        


        }
    }
    sum[size] = '\0';
    if(bound==1){
        sum[0]='-';
    }
    printf("%s\n", sum);
            
    
    
    
}
 

import java.util.ArrayList;

public class SortArray {
    public static void main(String[] args) {
        int[] arr = {4,2,5,7};
        arr = sortArrayByParityII(arr);
        for (int a:
             arr) {
            System.out.println(a);
        }


    }
    public static int[] sortArrayByParityII(int[] A) {

        int[] l = new int[A.length];
        int index = 0;
        for (int a: A) {
            if(a%2 == 0){
                l[index] = a;
                index +=2;
            }
        }
        index = 1;
        for (int a:A) {
            if(a%2 != 0){
                l[index] = a;
                index +=2;
            }
        }


        return l;

    }
}

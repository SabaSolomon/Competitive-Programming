import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class RelativeSort {
    public static void main(String[] args) {

        int[] a = {28,6,22,8,44,17};
        int[] b = {22,28,8,6};

        int[] r = relativeSortArray(a, b);
        System.out.println("+++++++++");
        for (int i:
             r) {
            System.out.println(i);
        }
        System.out.println("+++++++++");
    }
    public static int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] result = new int[arr1.length];
        int index = 0;
        for (int a:
             arr2) {
            for (int i = 0; i < arr1.length; i++) {
                if(a==arr1[i]){
                    result[index]=a;
                    index++;
                }
            }
        }

        ArrayList<Integer> left = new ArrayList<Integer>();

        for (int a : arr1) {
            boolean exists = false;
            for (int i = 0; i < result.length; i++) {
                if(a == result[i]){
                    exists = true;
                    break;
                }

            }
            if(!exists){
                left.add(a);
            }
        }

        Collections.sort(left);
        for (int n:
             left) {
            result[index] = n;
            index++;
        }


        return result;
    }
}

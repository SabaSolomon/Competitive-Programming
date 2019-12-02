import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Intersection {
    public static void main(String[] args) {
        int[] a ={4,9,5};
        int[] b = {9,4,9,8,4};
        int[] res = intersection(a, b);
        for (int r:
            res ) {
            System.out.println(r);
        }
    }
    public static int[] intersection(int[] nums1, int[] nums2) {
        List<Integer> num2Arr = Arrays.stream(nums2).boxed().collect(Collectors.toList());
        ArrayList<Integer> commons = new ArrayList<>();

        for (int a :
             nums1) {
            if(num2Arr.contains(a) && !commons.contains(a)){
                commons.add(a);
            }

        }

        int[] result = new int[commons.size()];
        int index = 0;
        for (int c:
             commons) {
            result[index] = c;
            index++;
        }
        return result;

    }
}

import java.util.ArrayList;

public class Solution {
    public static int[] twoSum(int[] nums, int target) {
        int sum = 0;
        ArrayList<Integer> x =new ArrayList<Integer>();

        int count = 0;
        for (int i = 0; i < nums.length; i++) {

            for (int j = i+1; j < nums.length; j++) {
                sum = nums[i] + nums[j];
                if(sum == target){
                    x.add(i);
                    x.add(j);
                    break;
                }
            }
        }
        int index[] = new int[x.size()];

        for (int i = 0; i < x.size(); i++) {
            index[i] = x.get(i);
        }

        return index;

    }

    public static void main(String[] args) {
        int x[] ={2,7, 11, 15};
        int res[] = twoSum(x, 17);
        for (int n:
             res) {
            System.out.println(n);

        }

    }
}

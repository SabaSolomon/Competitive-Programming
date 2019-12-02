public class ReverseInteger {
    public static void main(String[] args) {
        System.out.println(reverseInt(-120));
    }

    public static  int reverseInt(int x){
        int result = 0;
        while(x!=0){
            int last = x%10;
            x = x/10;
            if (result > Integer.MAX_VALUE/10 || (result == Integer.MAX_VALUE / 10 && last > 7)){
                return 0;
            }
            if (result < Integer.MIN_VALUE/10 || (result == Integer.MIN_VALUE / 10 && last < -8)){
                return 0;
            }
            result = result*10 + last;

        }
        return result;


        /*int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;*/
    }
}

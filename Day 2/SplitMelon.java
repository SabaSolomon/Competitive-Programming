import java.util.Scanner;

public class SplitMelon {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int inp = sc.nextInt();
        int intermediate = 1;
        if(inp>=1 && inp<=100){
            if(inp%2 == 0 && inp != 2) {
                System.out.println("YES");
            }
            else{
                System.out.println("NO");
            }
        }

    }
}

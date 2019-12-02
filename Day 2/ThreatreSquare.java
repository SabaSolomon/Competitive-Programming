import java.util.Scanner;

public class ThreatreSquare {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextInt();
        long m = sc.nextInt();
        long a = sc.nextInt();

        long count = 0;



        long x= m / a;
        if(m % a != 0){
            x += 1;
        }

        count = n / a;
        if(n%a != 0){
            count+=1;
        }



        System.out.println(count * x);


    }
}

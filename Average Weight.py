import java.util.Scanner;
public class weigh
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int X=sc.nextInt();
        int W1=sc.nextInt();
        int W2=sc.nextInt();
        int w3 = X*3-W1-W2;
        System.out.println(w3);
    }
}
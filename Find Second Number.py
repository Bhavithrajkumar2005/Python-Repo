import java.util.Scanner;
public class number
{
    public static void main(String args[])
    {
        Scanner sc= new Scanner(System.in);
        int X=sc.nextInt();
        int Y=sc.nextInt();
        int Z=2*X-Y;
        System.out.println(Z);
    }
}
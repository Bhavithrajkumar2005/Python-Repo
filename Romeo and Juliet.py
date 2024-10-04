import java.util.Scanner;
public class chocolate
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int X=sc.nextInt();
        int Y=sc.nextInt();
        int Z=sc.nextInt();
        int total=5*X+10*Y;
        int maxichocolatee=total/Z;
        System.out.println(maxichocolatee);
    }
}
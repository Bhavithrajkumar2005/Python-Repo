import java.util.Scanner;
public class Price
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        double X=sc.nextDouble();
        double Y=sc.nextDouble();
        double loss=X-Y;
        double Loss=(loss*100)/X;
        System.out.printf("%.2f",Loss); 
    }
}
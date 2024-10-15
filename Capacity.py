import java.util.Scanner;
public class diskkk
{
    public static void main(String args[])
    
    {
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt();
        int S=sc.nextInt();
        int B=sc.nextInt();
        int disk=T*S*B;
        System.out.println(disk+" "+"KB");
    }
}
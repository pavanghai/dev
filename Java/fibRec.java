// This is FibRecurdion Method , stops at it reaches 60
public class Main {
    public static void fibRec(int n1, int n2) {
        int f ; 
        f = n1 + n2 ;
        System.out.println("n1 "+n1 + " + n2 "+n2 + " = Fib " + f);
        n1 = n2;
        n2 = f;
        if (n1 + n2 <= 60) {
            //n1 = n2 ;
            //n2 = f ;
            fibRec(n1,n2);
        } else {
            System.out.println("Recursion over");
        }
    }

    public static void main(String[] args) {
        fibRec(0,1);
    }
}

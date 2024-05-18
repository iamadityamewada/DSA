public class fib{
    public static void main(String[] args){
       int ans = fibno(12); 
       System.out.println(ans);
    }
        static int fibno(int n){
            if(n<2){
                return 1;
            }else {
                return fibno(n-1)+fibno(n-2);
            }
        }
}
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package prac.pkg2;

/**
 *
 * @author Administrator
 */
import java.util.Scanner;
class Fib implements Runnable
{
 long a,b,c,n;
 Fib()
 {
     a=c=n=0;
     b=1
 }
 public void run()
 {
     while(n++<20)
     {
         system.out.println(n+"the Fib no:"+a);
         c=a+b;
         a=b;
         b=a;
         try{
             if(n==10)
                 system.out.println("Thread is sleeping");
             Thread.sleep(500);
         }
     }
     catch(InteruptedException e)
     {
         system.out.println("Error:"+e):
     }
     
     }
 }
public class MyFib1
{
    public static void main(String args[])
    {
        Thread ct=Thread.currentThread();
        system.out.println("Main thread name:"+ct.getName());
        Fib f=new Fib();
        Thread fib=new Thread(f,"fibonacci");
        
        fib.start();
        system.out.println("Thread"+fib.getName()+"started.");
    }
}
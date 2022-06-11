/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package projetj1;
import java.util.Scanner;

public class ProjetJ1 {
    
    public static int facto(int a){
        int b=1;
        for(int i=1;i<a;i++)
            b=b*i;
        return b;
    }
    
    public static double epar(){
        Scanner input=new Scanner(System.in);
        float a = input.nextInt();
        double s=200;
        double n=1.02;
        for (float i=1;i<=a;i++)
            s=s*n;
        return s;       
    }
    
    public static double eparg(){
        int s=200;
        Scanner input=new Scanner(System.in);
        int a=input.nextInt();
        for (int i=1;i<=a;i++)
            s=s+i*2;
        return s;            
    }
    
    public static void trian(){
        String e="";
        Scanner input=new Scanner(System.in);
        int n=input.nextInt();
        for (int i=1;i<=n;i++){
            e=e+"*";
        System.out.println(e);
        }       
    }
    
    public static void mdp(){
      int pass=1234;
      int count=0;
    while(count<3){
      System.out.print("Entrez votre mot de passe:");
      Scanner input=new Scanner(System.in);
      int n=input.nextInt();
    if (pass==n){
    System.out.println("OK");
    count=count+3;}
    else{
    System.out.println("ERREUR");
    count++;
    }
        
    }
    }
        
  
    public static void main(String[] args) {
       mdp();


}
}
    


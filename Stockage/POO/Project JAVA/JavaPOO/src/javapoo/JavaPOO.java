
package javapoo;


public class JavaPOO {
    
    public static void main(String[] args) {
        
        Poupee p0= new Poupee(3);
        Poupee p1= new Poupee(5,p0,null);
        Poupee p2= new Poupee(10);
        Poupee p3= new Poupee(15);
        Poupee p4= new Poupee(7,p1,p2);
        Poupee p5= new Poupee(20,p3,null);
        
        p3.setContenu(p4);
        
        System.out.println(p1);
        System.out.println(p2);
        System.out.println(p3);
        System.out.println(p4);
        System.out.println(p5);
        
    }
   
}

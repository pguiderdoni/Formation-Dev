package javarpg;
import java.util.ArrayList;

public class JavaRPG {

   
    public static void main(String[] args) {
        Perso play1= new Perso();
        Skaven mob1= new Vermine_Skaven();
        Skaven mob2= new Skaven();
        Skaven mob3= new Skaven_Guerrier();
        Skaven mob4= new Seigneur_des_Rats();            
       
        
        
        ArrayList<Skaven> Monstres= new ArrayList<>();
            Monstres.add(mob1);
            Monstres.add(mob2);
            Monstres.add(mob3);
            Monstres.add(mob4);
            
            
       
      int n=1;
      
       while ((Monstres.size()>0)&&(play1.getPersoHP() > 0)){
           System.out.println(play1);
           System.out.println("                             "+"||");
           System.out.println("                             "+"\\/");
           System.out.println("                           "+"Versus");
           System.out.println("                             "+"||");
           System.out.println("                             "+"\\/");
           System.out.println("  "+Monstres.get(0));
           System.out.println("");
        while (Monstres.get(0).getSkaLife()&&(play1.getPersoHP() > 0)){
            if ((n%2)==1){
            play1.Pjouer(Monstres.get(0));
            play1.PersoWin(Monstres.get(0));
        }
            if ((n%2)==0){
             Monstres.get(0).Ejouer(play1);
             Monstres.get(0).SkaWin(play1);
            }
            n=n+1;
        }
        Monstres.remove(0);
        n=1;
            
            
                                       
}    
}   
}

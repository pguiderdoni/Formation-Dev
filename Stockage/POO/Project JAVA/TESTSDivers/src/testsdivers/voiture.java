package testsdivers;

public class voiture extends vehicule {
    private int nbreRoues;
    
    
public voiture(String nom, int Km,int Ch,int roues){
    super(nom,Km,Ch);
    this.nbreRoues = roues;
      
}  
@Override
public void demarrer(){
    super.demarrer();
    System.out.println("et se prend un trottoir...");
}
}
    


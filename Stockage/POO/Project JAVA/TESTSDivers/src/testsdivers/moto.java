package testsdivers;

public class moto extends vehicule {
    private int nbreRoues;
    
    
public moto(String nom, int Km,int Ch,int roues){
    super(nom,Km,Ch);
    this.nbreRoues = roues;
      
}   
@Override
public void demarrer(){
    super.demarrer();
    System.out.println("et fais des wheeling comme un bouffon");
}
}
    


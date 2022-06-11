
package testsdivers;


public class vehicule {
    protected String nom;
    protected int kilometrage;
    protected int puissance;
    
    
public vehicule(String nom, int km, int Ch){
        this.nom = nom;
        this.kilometrage = km;
        this.puissance = Ch;
}

public String getNom(){
        return this.nom;
}
public int getkilometres(){
        return this.kilometrage;
}
public int getPuissance(){
        return this.puissance;
}
public void setNom(String nom ){
        this.nom=nom;
    }
public void setKilometre(int Km ){
        this.kilometrage=Km;
    }

public void demarrer(){
    System.out.print("\n" + "La " +this.getNom()+ " demarre"+"\n");
}

}

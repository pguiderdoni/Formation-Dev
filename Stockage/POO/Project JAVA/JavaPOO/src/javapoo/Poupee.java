
package javapoo;


public class Poupee {
    private int size;
    private Poupee contenu;
    private Poupee conteneur;
        
    public Poupee(int taille){
        this.size = taille;  
     }
    
    public Poupee(int taille,Poupee p1,Poupee p2){
        this.size = taille;
        setContenu(p1);
        setConteneur(p2);
        
    }
    
    public int getSize(){
        return this.size;
    }
    
    public Poupee getContenu(){
        return this.contenu;
    }
    
    public Poupee getConteneur(){
        return this.conteneur;
    }
    
    public void setSize(int taille){
        this.size=taille;
    }
    
    public void setContenu(Poupee contenu){        
        if (contenu!=null&& this.contenu!=contenu){
            if (this.size>contenu.getSize()){
        this.contenu=contenu;
        contenu.setConteneur(this);}
        }
    }
    
    public void setConteneur(Poupee conteneur){
        if (conteneur!=null&& this.conteneur!=conteneur){
            if (this.size>conteneur.getSize()){
        this.conteneur=conteneur;
        conteneur.setContenu(this);}
        }
    }
    @Override
    public String toString(){
        
        if (this.contenu!=null){
        return " "+size+"["+this.contenu.toString()+"]"; 
        }
        else{
            return " "+this.size;
        }
    }

}
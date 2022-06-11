
package javapoo;


public class Personnage {
    private String name;
    private int posX;
    private int posY;
    private String face;
        
    public Personnage(String nom, int X, int Y, String direction){
        this.name = nom;
        this.posX = X;
        this.posY = Y;
        this.face = direction;
     }   
    
    public String getName(){
        return name;
    }
    
    public String getFace(){
        return face;
    }
    
    public String getPosition(){
        return ""+this.posY+this.posX;
    }
    
    public void setName(String nom){
        this.name = nom;
    }
    
    public void setFace(String direction){
        this.face = direction;
    }
    
    public void setPosition(int x,int y){
        this.posX=x;
        this.posY=y;
    }
    
    public void setMove(int dist){
        if (this.face.equals("haut"))
            posY=posY+dist;
        if (this.face.equals("bas"))
            posY=posY-dist;
        if (this.face.equals("droite"))
            posX=posX+dist;
        if (this.face.equals("gauche"))
            posX=posX-dist;          
    }
    
    @Override
    public String toString(){
        return name+" "+posY+" "+posX+" "+face;
    }
   
    


}   


package javarpg;


public class Skaven_Guerrier extends Skaven {
    
    public Skaven_Guerrier() {
        super();
        this.SkaHP=SkaHP+15;
        this.SkaHPmax=SkaHP;
        this.SkaDef=SkaDef+3;
        this.SkaDmg=SkaDmg+3;
        this.SkaDmgH=SkaDmg+4;
        this.nom="Guerrier Skaven";
    }
    
@Override   
public String toString(){
    return super.toString();

}
    
    
}
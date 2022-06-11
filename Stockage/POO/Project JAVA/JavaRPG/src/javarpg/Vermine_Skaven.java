package javarpg;


public class Vermine_Skaven extends Skaven {
    
    
    public Vermine_Skaven() {
        super();
        this.SkaHP=SkaHP-10;
        this.SkaHPmax=SkaHP;
        this.SkaDef=SkaDef-1;
        this.nom="Skaven chetif";
    }
    
@Override   
public String toString(){
    return super.toString();

}    
}
package javarpg;

import java.util.Random;

public class Skaven {
    protected String nom;
    protected int SkaHP;
    protected int SkaHPmax;
    protected int SkaDmg;
    protected int SkaDmgH;
    protected int SkaDmgB;
    protected int SkaDef;
    protected int SkaArmu;
    protected boolean life;

    
public Skaven() {
    this.life=true;
    this.nom="Skaven";
    this.SkaHP = 30;
    this.SkaHPmax=SkaHP;
    this.SkaDmg = 6;
    this.SkaDmgH = this.SkaDmg + 3;
    this.SkaDmgB = this.SkaDmg - 2;
    this.SkaDef = 5;
    this.SkaArmu = 5;
}
public Skaven(int PV, int DPS, int Armure){
    this.SkaHP = PV;
    this.SkaDmg = DPS;
    this.SkaDmgH = DPS+4;
    this.SkaDmgB = DPS-2;
    this.SkaDef = Armure;
    this.SkaArmu = Armure;
    this.life=true;
     }
 
    public String toString(){
        return nom+": "+"Points de vie: " +SkaHP+"/"+SkaHPmax+" | "+"Degats: " +SkaDmg+" | "+ "Armure: " +SkaArmu;
    } 
    public String getNom(){
        return this.nom;
    }
    public int getSkaHP(){
        return this.SkaHP;
    }
    public int getSkaDmg(){
        return this.SkaDmg;
    }
    public int getSkaArmu(){
        return this.SkaArmu;
    }
    public boolean getSkaLife(){
        return this.life;
    }
    
    
    public void setSkaHP(int HP ){
        this.SkaHP=HP;
    }
    public void setSkaDmg(int Dmg ){
        this.SkaDmg=Dmg;
    }
    public void setSkaDef(int Def ){
        this.SkaDef=Def;
    }
    public void setSkaLife(boolean i){
        this.life=i;
    }
    
    
    
    public void Parry(){
        SkaArmu = SkaDef+(SkaDef/2);
    }
    
    public void SkaAtk(Perso p){
        SkaArmu = SkaDef;
        Random rand = new Random();
        int randomNum = SkaDmgB + rand.nextInt((SkaDmgH - SkaDmgB) + 1);
        int mit=randomNum - p.getPersoArmu();
        if (mit <= 0){    
            mit=1;
        }
        p.setPersoHP(p.getPersoHP()- mit);
        System.out.println("           Le "+this.nom+" attaque, vous perdez "+ mit+" PV"+"\n");
        System.out.println("");
        System.out.println("===========================Tour du Joueur==========================");
    }
    
    public void Ejouer(Perso p){
        Random result = new Random();
        int rng = result.nextInt(20);
        if (rng<=12){
            SkaAtk(p);
        }
        if (rng>12){
            Parry();
            System.out.println("               "+this.nom+" se prepare a parer"+"\n");
            System.out.println("");
        System.out.println("===========================Tour du Joueur==========================");
        }
        System.out.println(p);
    
    } 
    
    public void SkaWin(Perso p){
        if (p.getPersoHP()<=0){
            System.out.println("\n"+ "                     <<< VOUS ETES MORT >>> " + "\n");
        }
    }
}

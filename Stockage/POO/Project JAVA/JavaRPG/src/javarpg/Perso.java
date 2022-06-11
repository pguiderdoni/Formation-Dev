package javarpg;
import java.util.Random;
import java.util.Scanner;

public class Perso {
    private String PersoName;
    private int PersoHP;
    private int PersoHPmax;
    private int PersoDmg;
    private int PersoDmgH;
    private int PersoDmgB;
    private int PersoDef;
    private int PersoArmu;
    private int PersoPotNbre;
    private int PersoPot;
    
    public Perso() {
        this.PersoName = "Gerceval";
        this.PersoHPmax=50;
        this.PersoHP = 50;
        this.PersoDmg = 6;
        this.PersoDmgH = this.PersoDmg + 4;
        this.PersoDmgB = this.PersoDmg - 2;
        this.PersoDef = 7;
        this.PersoArmu = 7;
        this.PersoPotNbre=3;
        this.PersoPot=8;
    }
    public Perso(String nom, int PV, int DPS, int Armure){
        this.PersoName = nom;
        this.PersoHP = PV;
        this.PersoDmg = DPS;
        this.PersoDmgH = DPS+4;
        this.PersoDmgB = DPS-2;
        this.PersoDef = Armure;
        this.PersoArmu = Armure;
    }
    
    @Override
    public String toString(){
        return PersoName+": "+"Points de vie: " +PersoHP+"/"+PersoHPmax+" |"+" "+"Degats: " +PersoDmg+" | "+"Armure: " +PersoArmu+" | "+"Estus: "+this.PersoPotNbre+"("+this.PersoPot+"Pv"+")";
    } 
    
    public int getPersoHP(){
        return this.PersoHP;
    }
    public int getPersoDmg(){
        return this.PersoDmg;
    }
    public int getPersoArmu(){
        return this.PersoArmu;
    }
    
    
    public void setPersoHP(int HP ){
        this.PersoHP=HP;
    }
    public void setPersoDmg(int Dmg ){
        this.PersoDmg=Dmg;
    }
    public void setPersoDef(int Def ){
        this.PersoDef=Def;
    }
    
    
    public void Heal(){
        if (this.PersoPotNbre>0){
        this.PersoHP=this.PersoHP+this.PersoPot;
        if (PersoHP>PersoHPmax){
            PersoHP=PersoHPmax;
            System.out.println("Vous regagnez "+this.PersoPot+" points de vie");
        }
        this.PersoPotNbre-=1;
        }
        if (this.PersoPotNbre==0){
            System.out.println("Vous n'avez plus de potions !!");
        }   
    }
    
    public void Parry(){
        PersoArmu = PersoDef+(PersoDef/2);
    }
    public void PersoAtk(Skaven s){
        PersoArmu = PersoDef;
        Random rand = new Random();
        int randomNum = PersoDmgB + rand.nextInt((PersoDmgH - PersoDmgB) + 1);
        int mit=randomNum - s.getSkaArmu();
        if (mit <= 0){    
            mit=1;
        }
        s.setSkaHP(s.getSkaHP()- mit);
        System.out.println("   Vous frappez le "+ s.getNom()+" et lui enlevez "+ mit + " Points de vie"+ "\n");
        System.out.println("");
    }
    
    
    
     public void Pjouer(Skaven s){
        System.out.println("                    !! A vous de jouer !!");
        System.out.println("Tapez 1 pour attaquer, 2 pour parer, 3 pour votre fiole d'Estus");
        Scanner choix= new Scanner(System.in);
        int i = choix.nextInt();
        if (i==1){
            PersoAtk(s);
        }
        if (i==2){
            Parry();
            System.out.println("");
        }        
        if (i==3){
            Heal();
        }
    System.out.println("===========================Tour de l'Ennemi========================");
    System.out.println("    "+s); 

     }
    public void PersoWin(Skaven s){
        if (s.getSkaHP()<=0){
            s.setSkaLife(false);
            System.out.println(" Vous avez vaincu un Skaven, GG N00B ");
            this.PersoHPmax=this.PersoHPmax+5;
            this.PersoDmg=this.PersoDmg+2;
            this.PersoDef=this.PersoDef+2;
            System.out.println("========================= Niveau Superieur !!!=====================");
            System.out.println("Vous gagnez 5 points de vie max, 2 points de degats, 1 point d'armure");
            System.out.println("et votre Fiole d'Estus devient plus efficace...");
            this.PersoPot=this.PersoPot+=3;
            Random rand = new Random();
                int i = rand.nextInt(20);
            if ((i>4)&&(i<13)){
                this.PersoPotNbre+=1;
                System.out.println("     Vous gagnez une charge d'Estus!");
            }
            if ((i>12)&&(i<17)){
                this.PersoPotNbre+=2;
                System.out.println("     Vous gagnez 2 charges d'Estus!!");
            }
            if ((i>16)&&(i<=19)){
                this.PersoPotNbre+=3;
                this.PersoPot=PersoPot*2;
                System.out.println("Vous gagnez 3 charges d'Estus, et votre fiole devient 2 fois plus efficace!!");
            }
            
        }
    }        
} 
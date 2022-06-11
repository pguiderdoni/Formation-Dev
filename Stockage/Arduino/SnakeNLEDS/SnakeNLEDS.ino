
#include "LedControl.h"


LedControl lc = LedControl(12, 10, 11, 1);


unsigned long delaytime1 = 50;
unsigned long delaytime2 = 50;
int tabx[] = { -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
int taby[] = { -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};

void setup() {
  Serial.begin(9600);
  lc.shutdown(0, false);
  lc.setIntensity(0, 1);
  lc.clearDisplay(0);
}


void moveSingle(int i, int j) {

  lc.setLed(0, i, j, true);
  if (tabx[0] != i or taby[0] != j) {
    for (int s = 5; s >= 0; s--) {
      lc.setLed(0, tabx[5], taby[5], false);
      tabx[s] = tabx[s - 1];
      taby[s] = taby[s - 1];
      tabx[0] = i;
      taby[0] = j;
    }
  }

  if ( joystick() == 2) {       //droite
    //lc.setLed(0,i,j,false);
    if (i <= 0) {               // Le snake passe d'un coté à l'autre, pour bloquer, inverser 0 et 7
      i = 7;
    }
    else {
      i--;
    }
  }
  else if (joystick() == 1) {   //gauche
    //lc.setLed(0,i,j,false);
    if (i >= 7) {               // Le snake passe d'un coté à l'autre, pour bloquer, inverser 0 et 7
      i = 0;
    }
    else {
      i++;
    }
  }
  else if ( joystick() == 3) {   //haut
    //lc.setLed(0,i,j,false);
    if (j <= 0) {                // Le snake passe d'un coté à l'autre, pour bloquer, inverser 0 et 7
      j = 7;
    }
    else {
      j--;
    }
  }
  else if (joystick() == 4) {    //bas
    //lc.setLed(0,i,j,false);
    if (j >= 7) {                // Le snake passe d'un coté à l'autre, pour bloquer, inverser 0 et 7
      j = 0;
    }
    else {
      j++;
    }
  }
  }
delay(100;
moveSingle(i,j);

int directionToGo = 0;
int joystick() {

  int sensorValueX = analogRead(A0);
  int sensorValueY = analogRead(A1);

  if (sensorValueX < 40) {  //gauche
    directionToGo = 1;
  }
  if (sensorValueX > 999) { //droite
    directionToGo = 2;
  }
  if (sensorValueX >= 480 and sensorValueX <= 520 and sensorValueY >= 480 and sensorValueY <= 520) {
    directionToGo = 0;
  }
  if (sensorValueY < 40) {  //haut
    directionToGo = 3;
  }
  if (sensorValueY > 999) { //bas
    directionToGo = 4;
  }
  


  return directionToGo;
}


void loop() {
  moveSingle(2, 2);

}

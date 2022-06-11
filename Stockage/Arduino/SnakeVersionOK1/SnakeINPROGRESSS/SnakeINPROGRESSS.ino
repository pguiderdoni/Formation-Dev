
#include "LedControl.h"
#include "pitches.h"
#define buzzerpin 3

LedControl lc = LedControl(12, 10, 11, 1);


unsigned long delaytime1 = 50;
unsigned long delaytime2 = 50;
int tabx[] = { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int taby[] = { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
void setup() {
  Serial.begin(9600);
  lc.shutdown(0, false);
  lc.setIntensity(0, 1);
  lc.clearDisplay(0);
  pinMode(3, OUTPUT);//buzzer
  pinMode(13, OUTPUT);//led indicator when singing a note
  sing(1);
  
}
int a = -1;
int b = -1;
int stepSnake = 0;
int snakeLength = 1;

bool isFoodOnSnake(int afood, int bfood) {
  for (int i = 0; i < snakeLength; i++) {
    if ( afood == tabx[i] and bfood == taby[i] ) {
      Serial.print(afood);
      Serial.print(tabx[i]);
      Serial.print(bfood);
      Serial.print(taby[i]);
      Serial.println();
      return true;
    }
  }
}

void genereFood() {
  a = random(0, 7);
  b = random(0, 7);
  //while ( true ) {
  //if ( isFoodOnSnake(a, b) ) {
  //a = random(0, 7);
  //b = random(0, 7);
  //} else break;
  //}
  lc.setLed(0, a, b, true);
  //stepSnake = 0;
}

void moveSingle(int i, int j) {
  if (stepSnake == 12) genereFood();
  if (i == a and j == b) {
    if (snakeLength < 16) snakeLength++;
    a = -1;
    b = -1;
    genereFood();
    tone(3,3800,50);
    delay (150);
    tone(3,400,50);
    delay(100);
    if (snakeLength == 15) sing(2);
  }
  lc.setLed(0, i, j, true);
  if (tabx[0] != i or taby[0] != j) {
    for (int s = snakeLength + 1; s > 0; s--) {
      lc.setLed(0, tabx[snakeLength + 1], taby[snakeLength + 1], false);
      tabx[s] = tabx[s - 1];
      taby[s] = taby[s - 1];
      tabx[0] = i;
      taby[0] = j;
    }
  }
  if ( joystick() == 2) {       //droite
    //lc.setLed(0,i,j,false);
    if (i <= 0) {
      i = 0;
    }
    else {
      i--;
    }
    stepSnake++;
  }
  else if (joystick() == 1) {   //gauche
    //lc.setLed(0,i,j,false);
    if (i >= 7) {
      i = 7;
    }
    else {
      i++;
    }
    stepSnake++;
  }
  else if ( joystick() == 3) {   //haut
    //lc.setLed(0,i,j,false);
    if (j <= 0) {
      j = 0;
    }
    else {
      j--;
    }
    stepSnake++;
  }
  else if (joystick() == 4) {    //bas
    //lc.setLed(0,i,j,false);
    if (j >= 7) {
      j = 7;
    }
    else {
      j++;
    }
    stepSnake++;
    
  }

  delay(85);
  moveSingle(i, j);

}



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
  int initX = random(0, 7);
  int initY = random(0, 7);
  moveSingle(initX, initY);

}

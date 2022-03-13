/* Grove - Light Sensor demo v1.2
* 
* signal wire to A0.
* By: http://www.seeedstudio.com
*/
#include <math.h>
const int ledPin=13;                 //Connect the LED Grove module to Pin12, Digital 12
const int thresholdvalue=10;         //The threshold for which the LED should turn on. 
float Rsensor; //Resistance of sensor in K
void setup() {
  Serial.begin(9600);                //Start the Serial connection
  pinMode(ledPin,OUTPUT);            //Set the LED on Digital 12 as an OUTPUT
}
void loop() {
  int sensorValue = analogRead(0); 
  Rsensor=(float)(1023-sensorValue)*10/sensorValue;
  if(Rsensor>thresholdvalue)
  {
    digitalWrite(ledPin,HIGH);
  }
  else
  {
  digitalWrite(ledPin,LOW);
  }
  Serial.println("the analog read data is ");
  Serial.println(sensorValue);
  Serial.println("the sensor resistance is ");
  Serial.println(Rsensor,DEC);//show the light intensity on the serial monitor;
  delay(1000);
}

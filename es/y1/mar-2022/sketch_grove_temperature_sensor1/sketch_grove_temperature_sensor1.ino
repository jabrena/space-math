// Demo code for Grove - Temperature Sensor V1.1/1.2
// Loovee @ 2015-8-26
 
#include <math.h>
 
const int B=4275;                 // B value of the thermistor
const int R0 = 100000;            // R0 = 100k
const int pinTempSensor = A3;     // Grove - Temperature Sensor connect to A5
 
void setup()
{
    Serial.begin(9600);
}
 
void loop()
{
    int a = analogRead(pinTempSensor );
 
    float R = 1023.0/((float)a)-1.0;
    R = 100000.0*R;
 
    float temperature=1.0/(log(R/100000.0)/B+1/298.15)-273.15;//convert to temperature via datasheet ;
 
    Serial.print("temperature = ");
    Serial.println(temperature);
 
    delay(1000);
}

/*
 HC-SR04 Ping distance sensor:
 VCC to arduino 5v 
 GND to arduino GND
 Echo to Arduino pin 7 
 Trig to Arduino pin 8
 
 This sketch originates from Virtualmix: http://goo.gl/kJ8Gl
 Has been modified by Winkle ink here: http://winkleink.blogspot.com.au/2012/05/arduino-hc-sr04-ultrasonic-distance.html
 And modified further by ScottC here: http://arduinobasics.blogspot.com.au/2012/11/arduinobasics-hc-sr04-ultrasonic-sensor.html
 on 10 Nov 2012.
 */


#define echoPinA 5 // Echo Pin
#define trigPinA 6 // Trigger Pin
#define echoPinB 7 // Echo Pin
#define trigPinB 8 // Trigger Pin
#define LEDPin 13 // Onboard LED

int maximumRange = 40; // Maximum range needed
int minimumRange = 5; // Minimum range needed
long durationA, distanceA; // Duration used to calculate distance
long durationB, distanceB; // Duration used to calculate distance

void setup() {
 Serial.begin (9600);
 pinMode(trigPinA, OUTPUT);
 pinMode(echoPinA, INPUT);
 pinMode(trigPinB, OUTPUT);
 pinMode(echoPinB, INPUT);
 pinMode(LEDPin, OUTPUT); // Use LED indicator (if required)
}

void loop() {
/* The following trigPin/echoPin cycle is used to determine the
 distance of the nearest object by bouncing soundwaves off of it. */ 
 digitalWrite(trigPinA, LOW); 
 delayMicroseconds(2); 

 digitalWrite(trigPinA, HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPinA, LOW);
 durationA = pulseIn(echoPinA, HIGH);
 
 //Calculate the distance (in cm) based on the speed of sound.
 distanceA = durationA/58.2;
 
 if (distanceA >= maximumRange || distanceA <= minimumRange){
 /* Send a negative number to computer and Turn LED ON 
 to indicate "out of range" */
 //Serial.println("-1");
 digitalWrite(LEDPin, HIGH); 
 }
 else {
 /* Send the distance to the computer using Serial protocol, and
 turn LED OFF to indicate successful reading. */
 Serial.print("$A: ");
 Serial.print(distanceA);
 Serial.println(";");
 digitalWrite(LEDPin, LOW); 
 }
 
 digitalWrite(trigPinB, LOW); 
 delayMicroseconds(2); 

 digitalWrite(trigPinB, HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPinB, LOW);
 durationB = pulseIn(echoPinB, HIGH);
 
 //Calculate the distance (in cm) based on the speed of sound.
 distanceB = durationB/58.2;
 
 if (distanceB >= maximumRange || distanceB <= minimumRange){
 /* Send a negative number to computer and Turn LED ON 
 to indicate "out of range" */
 //Serial.println("-1");
 digitalWrite(LEDPin, HIGH); 
 }
 else {
 /* Send the distance to the computer using Serial protocol, and
 turn LED OFF to indicate successful reading. */
 Serial.print("$B: ");
 Serial.print(distanceB);
 Serial.println(";");
 digitalWrite(LEDPin, LOW); 
 }
 
 //Delay 50ms before next reading.
 delay(500);
}


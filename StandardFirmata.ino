int led1 = 23;
int led2 = 22;
int led3 = 21;
int led4 = 19;
int led5 = 18;

void setup() {

Serial.begin(115200);

pinMode(led1,OUTPUT);
pinMode(led2,OUTPUT);
pinMode(led3,OUTPUT);
pinMode(led4,OUTPUT);
pinMode(led5,OUTPUT);

}

void loop() {

if(Serial.available()>0){

String data = Serial.readStringUntil('\n');

digitalWrite(led1, data[0]=='1' ? HIGH : LOW);
digitalWrite(led2, data[1]=='1' ? HIGH : LOW);
digitalWrite(led3, data[2]=='1' ? HIGH : LOW);
digitalWrite(led4, data[3]=='1' ? HIGH : LOW);
digitalWrite(led5, data[4]=='1' ? HIGH : LOW);

}

}
void setup() {
  Serial.begin(9600);  
  pinMode(9, OUTPUT);  
  pinMode(8, OUTPUT);  
  pinMode(7, OUTPUT);  
}

void loop() {
  if (Serial.available() > 0) {  
    byte receivedByte = Serial.read();

    Serial.println(receivedByte);

    switch (receivedByte) {
      case 10:
        digitalWrite(8, LOW);
        break;

      case 11: 
        digitalWrite(8, HIGH);
        break;

      case 20: 
        digitalWrite(7, LOW);
        break;

      case 21:  
        digitalWrite(7, HIGH);
        break;

      case 30:  
        digitalWrite(9, LOW);
        break;

      case 31:  
        digitalWrite(9, HIGH);
        break;

      default:
        digitalWrite(9,LOW);
        digitalWrite(7,LOW);
        digitalWrite(8,LOW);
        break;
    }
  }
}

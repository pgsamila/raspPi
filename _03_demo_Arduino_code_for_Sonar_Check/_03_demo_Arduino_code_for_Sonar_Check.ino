#define ECHO_PIN  2
#define TRIG_PIN  4
#define GREEN     46
#define RED       44

long duration, distance;
int dist = 200;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(RED, OUTPUT);
  distance = 200;
  digitalWrite(GREEN, HIGH);
  digitalWrite(RED, LOW);
}

void loop() {
  while (Serial.available()) {
    // starts the program here
    char inChar = (char)Serial.read();
    distance = Check_Sonar_reading();

    if (distance >= 100) {
      digitalWrite(GREEN, HIGH);
      digitalWrite(RED, LOW);
      Serial.println("G");
    } else {
      digitalWrite(GREEN, LOW);
      digitalWrite(RED, HIGH);
      Serial.println("R");
    }

  }
  //waite for the signal from Pi
  delay(100);
}

long Check_Sonar_reading() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);

  digitalWrite(TRIG_PIN, LOW);
  duration = pulseIn(ECHO_PIN, HIGH);

  distance = duration / 58.2;

  delay(50);
  return distance;
}

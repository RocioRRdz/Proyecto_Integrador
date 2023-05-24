int trig = 11;
int echo = 12;

void setup() {
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  long tiempo = pulseIn (echo, HIGH);
  float distancia = tiempo / 2.0 * 0.0343 * 100; // Velocidad del sonido en el aire (aprox. 340 m/s)     //100 es por los centímetros.
  
  Serial.println(distancia);
  delay(1000);
}

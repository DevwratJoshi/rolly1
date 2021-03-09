// This code should receive left and right motor velocity commands through serial. 
// The code must parse the command line, and write the values to the appropriate motor
#define M_SPEED 100 // The default motor speed
#define MAX_INPUT_SIZE 10 // The max expected size of the input command
// right connections
int enA = 9;
int in1 = 8;
int in2 = 7;
// left connections
int enB = 3;
int in3 = 5;
int in4 = 6;

char command[MAX_INPUT_SIZE];
int right_pwm = 0;
int left_pwm = 0;
void setup() {
  Serial.begin(9600);
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

void loop() {
  if(Serial.available() > 0)
  {
    byte size = Serial.readBytesUntil('\n', command, MAX_INPUT_SIZE);
    // Add the final 0 to end the C string
    command[size] = 0;
    
    char *input = strtok(command, ":");
    right_pwm = atoi(input);
    input = strtok(NULL, "\n"); // The end of the line
    left_pwm = atoi(input);
    
    Serial.print("Right = ");
    Serial.print(right_pwm);
    Serial.print(" Left = ");
    Serial.println(left_pwm);
  }
  delay(2);
}

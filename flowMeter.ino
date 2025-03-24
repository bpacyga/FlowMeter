#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

const int buttonPin = 7;
const int flowMeterPin = 2;

float calibrationFactor = 4.5;

//Global variables 
volatile byte pulseCount;  
float flowRate;
unsigned int flowMilliLitres;
unsigned long totalMilliLitres;

unsigned long oldTime;

// LCD settings
int displaySetting = 1;
const int maxDisplays = 5;
unsigned long lastDisplaySwitch = millis();
const int displayDelay = 250;
int flag = 0;

void setup() {
  Serial.begin(9600);
  Serial.print("test");
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Output Liquid Quantity:");
  lcd.setCursor(0, 1);
  lcd.print(totalMilliLitres);
  pulseCount        = 0;
  flowRate          = 0.0;
  flowMilliLitres   = 0;
  totalMilliLitres  = 0;
  oldTime           = 0;

  pinMode(buttonPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(buttonPin), testMath, FALLING);
  pinMode(flowMeterPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(flowMeterPin), flowTrigger, FALLING);

}

void loop()
{
   
   if((millis() - oldTime) > 1000)    // Only process counters once per second
  { 
    // Disable the interrupt while calculating flow rate and sending the value to
    // the host
    detachInterrupt(digitalPinToInterrupt(flowMeterPin));
        
    // Because this loop may not complete in exactly 1 second intervals we calculate
    // the number of milliseconds that have passed since the last execution and use
    // that to scale the output. We also apply the calibrationFactor to scale the output
    // based on the number of pulses per second per units of measure (litres/minute in
    // this case) coming from the sensor.
    flowRate = ((1000.0 / (millis() - oldTime)) * pulseCount) / calibrationFactor;
    
    // Note the time this processing pass was executed. Note that because we've
    // disabled interrupts the millis() function won't actually be incrementing right
    // at this point, but it will still return the value it was set to just before
    // interrupts went away.
    oldTime = millis();
    
    // Divide the flow rate in litres/minute by 60 to determine how many litres have
    // passed through the sensor in this 1 second interval, then multiply by 1000 to
    // convert to millilitres.
    flowMilliLitres = (flowRate / 60) * 1000;
    
    // Add the millilitres passed in this second to the cumulative total
    totalMilliLitres += flowMilliLitres;
      
    unsigned int frac;
    
    // Print the flow rate for this second in litres / minute
    Serial.print("Flow rate: ");
    Serial.print(int(flowRate));  // Print the integer part of the variable
    Serial.print("L/min");
    Serial.print("\t");       // Print tab space

    // Print the cumulative total of litres flowed since starting
    Serial.print("Output Liquid Quantity: ");        
    Serial.print(totalMilliLitres);
    Serial.println("mL"); 
    Serial.print("\t");       // Print tab space
    Serial.print(totalMilliLitres/1000);
    Serial.print("L");
    delay(1000);
    displayLCD();
    

    // Reset the pulse counter so we can start incrementing again
    pulseCount = 0;
    
    // Enable the interrupt again now that we've finished sending output
    attachInterrupt(digitalPinToInterrupt(flowMeterPin), flowTrigger, FALLING);
  }
}


void flowTrigger(){
  //Trigger that is supposed to increment when water flows through sensor
  Serial.print("Entered flowTrigger");
  pulseCount++;
}

void displayLCD(){
   Serial.print("Entered LCD");
   lcd.clear();
   lcd.setCursor(0, 0);
   lcd.print("Output Liquid Quantity:");
   lcd.setCursor(0, 1);
   lcd.print(totalMilliLitres);
}

 void testMath(){
    //Interrupt so we can test the display and changing values using the button
    Serial.print("Entered testMath");
    pulseCount += 1000;
 }

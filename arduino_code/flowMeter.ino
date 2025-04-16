#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 6, 5, 4,7);

const int buttonPin = 3;
const int flowMeterPin = 2;

float calibrationFactor = 1;

//Global variables 
volatile int pulseCount;  
float flowRate;
unsigned int flowMilliLitres;
unsigned long totalMilliLitres;
unsigned long totalFlowRate;

unsigned long oldTime;

// LCD settings
int displaySetting = 1;
const int maxDisplays = 3;
unsigned long lastDisplaySwitch = millis();
const int displayDelay = 250;
int flag = 0;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(.1);
  lcd.begin(16, 2);
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
  totalFlowRate     = 0;

  pinMode(buttonPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(buttonPin), changeDisplaySettingFlag, FALLING);
  pinMode(flowMeterPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(flowMeterPin), flowTrigger, FALLING);

}

void loop()
{
   
   if((millis() - oldTime) > 5000)    // Only process counters once per second
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
    
    // Divide the flow rate in litres/minute by 300 to determine how many litres have
    // passed through the sensor in this 5 second interval, then multiply by 1000 to
    // convert to millilitres.
    flowMilliLitres = (flowRate / 300) * 1000;
    
    // Add the millilitres passed in this second to the cumulative total
    totalMilliLitres += flowMilliLitres;

    // Divide totalMilliLitres by time since start to get totalFlowRate (mL/sec)
    totalFlowRate = totalMilliLitres/(millis()/1000);
    
    unsigned int frac;
  

    // Send the total MiliLitres to the Serial port for reading in Python

    Serial.println(float(flowRate));
    Serial.println(long(totalMilliLitres));
    Serial.println(long(millis()));
    Serial.println(long(totalFlowRate));
    //Serial.println(float(flowRate));

    if(flag == 1)
    {
      flag = 0;
      changeDisplaySetting();
    }
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
  pulseCount++;
}

void displayLCD(){
   //Serial.print("Entered LCD");
   lcd.clear();
   lcd.setCursor(0, 0);
   switch(displaySetting)
   {
     case 1:
     lcd.print("Total Quantity:");
     lcd.setCursor(0, 1);
     lcd.print(totalMilliLitres);
     break;
     case 2:
     lcd.print("Flow rate:");
     lcd.setCursor(0, 1);
     lcd.print(flowRate);
     break;
     case 3:
     lcd.print("Total Flow rate:");
     lcd.setCursor(0, 1);
     lcd.print(totalFlowRate);
     break;
     default:
     lcd.print("Unknown Setting!");
   }
}

 void changeDisplaySettingFlag() {
    flag = 1;
}
void changeDisplaySetting() {
    if(lastDisplaySwitch + displayDelay < millis()) { // this limits how quickly the LCD Display can switch
    lastDisplaySwitch = millis();
    displaySetting++;
    if(displaySetting > maxDisplays) {
      displaySetting = 1;
    }
    displayLCD();
  }
}

#include <FastLED.h>

#define NUM_LEDS 1 
//Define number of LEDs 
#define LED_PIN 13 
//Pin to connect WS2812 LED strip [we used this one!] (GPIO12 on NodeMCU)
CRGB leds[NUM_LEDS];

void setup() {
  Serial.begin(9600);

  //Initialize FastLED with the number of LEDs and LED strip type
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
}

void loop() {
  //Wait for incoming data from the computer
  if (Serial.available() > 0) {
    //Read the incoming byte
    byte digit = Serial.read();
    //Set the appropriate color based on the received digit
    switch (digit) {
      case 0:
        // Angry
        setColor(108, 174, 117); //Green
        break;
      case 1:
        // Disgust
        setColor(255, 165, 0); //Orange
        break;
      case 2:
        // Fear
        setColor(0, 119, 190); //Blue
        break;
      case 3:
        // Happy
        setColor(226, 80, 152); //Pink
        break;
      case 4:
        // Sad
        setColor(255, 223, 0); //Golden Yellow
        break;
      case 5:
        // Surprise
        setColor(138, 43, 226); //Violet
        break;
    }
  }
}

//Function to set the color of the LED
void setColor(uint8_t r, uint8_t g, uint8_t b) {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CRGB(r, g, b); //Set the color of each LED
  }
  FastLED.show(); //Display the color
}

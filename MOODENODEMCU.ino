#include <FastLED.h>

#define NUM_LEDS 1 // Define the number of LEDs in your strip
#define LED_PIN 13 // Pin to connect WS2812 LED strip (GPIO12 on NodeMCU)

CRGB leds[NUM_LEDS];

void setup() {
  // Set up serial communication
  Serial.begin(9600);

  // Initialize FastLED with the number of LEDs and the correct LED strip type
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
}

void loop() {
  // Wait for incoming data from the computer
  if (Serial.available() > 0) {
    // Read the incoming byte
    byte digit = Serial.read();

    // Set the appropriate color based on the received digit
    switch (digit) {
      case 0:
        // Angry
        setColor(108, 174, 117); // Green Oasis (Serenity)
        break;
      case 1:
        // Disgust
        setColor(152, 255, 152); // Tranquil Mint (Disgust)
        break;
      case 2:
        // Fear
        setColor(0, 119, 190); // Ocean Blue (Fear)
        break;
      case 3:
        // Happy
        setColor(226, 80, 152); // Pink Blossom (Happy)
        break;
      case 4:
        // Neutral
        setColor(255, 255, 255); // White (Neutral)
        break;
      case 5:
        // Sad
        setColor(108, 142, 191); // Tranquil Teardrop (Sad)
        break;
      case 6:
        // Surprise
        setColor(138, 43, 226); // Enchanted Violet (Surprise)
        break;
    }
  }
}

// Function to set the color of the LED
void setColor(uint8_t r, uint8_t g, uint8_t b) {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CRGB(r, g, b); // Set the color of each LED
  }
  FastLED.show(); // Display the color
}
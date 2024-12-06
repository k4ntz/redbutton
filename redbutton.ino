#include <Keyboard.h>

const int switchPin = 2; // Define the pin connected to the switch
int switchState = 0;
int RXLED = 17;  // The RX LED has a defined Arduino pin

int counter = 0;

bool ctrlPressed = false;

void setup() {

  Serial.begin(9600); //This pipes to the serial monitor
  Serial.println("Initialize Serial Monitor");

  // Initialize keyboard emulation
  Keyboard.begin();

  pinMode(switchPin, INPUT_PULLUP); // Use internal pull-up resistor
  pinMode(RXLED, OUTPUT);  // Set RX LED as an output
}

void loop() {
  switchState = digitalRead(switchPin); // Read the state of the switch
  if (switchState == LOW) {
      digitalWrite(RXLED, HIGH);   // set the RX LED ON
      delay(1000);              // wait for a second
      digitalWrite(RXLED, LOW);
      Serial.println("Switch is pressed");
      performShortcuts();
  } else {
      Serial.println("Switch is not pressed");
  }
  delay(100); // Small delay for debouncing
}

// Function to emulate the shortcut actions
void performShortcuts() {
  counter++;
  if (counter == 5) {
    showCats();
    counter = 0;
  } else{
  // Focus on the address bar (Ctrl + L)
    Keyboard.press(KEY_LEFT_CTRL);
    Keyboard.press('l');
    delay(100);
    Keyboard.releaseAll();

    // Copy address bar content (Ctrl + C)
    Keyboard.press(KEY_LEFT_CTRL);
    Keyboard.press('c');
    delay(100);
    Keyboard.releaseAll();

    // Switch to the first tab (Alt + 1)
    Keyboard.press(KEY_LEFT_ALT);
    Keyboard.press(KEY_TAB);
    delay(100);
    Keyboard.releaseAll();

    delay(1000);
    // Paste content (Ctrl + V)
    Keyboard.press(KEY_LEFT_CTRL);
    Keyboard.press('v');
    delay(100);
    Keyboard.releaseAll();

    // Press Enter
    Keyboard.press(KEY_RETURN);
    delay(100);
    Keyboard.releaseAll();
  }
}

void showCats() {
   // open new tab
    Keyboard.press(KEY_LEFT_CTRL); // Press Control (for Windows/Linux)
    Keyboard.press('t');           // Press 'T'
    delay(100);
    Keyboard.releaseAll();
    delay(500); // Wait for the new tab to open

    // Type the URL
    Keyboard.print("https://thesecatsdonotexist.com/");
    delay(500);
    Keyboard.press(KEY_RETURN); // Press Enter
    Keyboard.release(KEY_RETURN);
}

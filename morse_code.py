# ENDG 233 F23
# Hardware Project
# Anas Chowdhury
# morse_code.py

import machine
import time

# Provided dictionary for morse code encoding.
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

# These constants time values allow us to determine the length of time each on/off pulse will be transmitted.
TIME_UNIT = 0.1;
DOT = 1;
DASH = 3;
LETTER_SPACE = 3;
WORD_SPACE = 7;

output_string = "ENDG 233 is complete".upper().split()

# Both LED pin and the GPIO pin are being sent the signal simultaneously. This allows you to test your code via the built-in LED
# while also remaining compatible with the grading decoder.

led_pin = machine.Pin('LED', machine.Pin.OUT)
output_pin = machine.Pin(16, machine.Pin.OUT)

# This provided function will send the data that represents a dot.
def dot():
    led_pin.on()
    output_pin.on()
    time.sleep(TIME_UNIT*DOT)
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT)

# This provided function will send the data that represents a dash.
def dash():
    led_pin.on()
    output_pin.on()
    time.sleep(TIME_UNIT*DASH)
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT)

# This provided function will send the data that represents a space between letters.
def letter_space():
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT*LETTER_SPACE)

# This provided function will send the data that represents a space between words.
def word_space():
    led_pin.off()
    output_pin.off()
    time.sleep(TIME_UNIT*WORD_SPACE)


# Main function
def main():    
    while True:
        morse_string = ''
        morse_numbers = ''
        for word in output_string:
            for letter in word:
                morse_string += '['
                for i in morse_code[letter]:
                    if i == '-':
                        dash()
                        morse_string += '1110'
                    
                    else:
                        dot()
                        morse_string += '10'
                letter_space()
                morse_string += '][000]'
            word_space()
            morse_string += '[0000000]'
        
        morse_string = morse_string[:-14]
        print('ENDGG 233 is complete')
        print(morse_string)

if __name__ == "__main__":
    main()
    

#Make a list for the english alphabet and the morse code alphabet

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
              '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-',
              '.--', '-..-', '-.--', '--..', '.......']

#Use a for loop to make a dictionary from the 2 lists

morse_alphabet = {}
for num in range(27):
    morse_alphabet[alphabet[num]] = morse_code[num]

# Test the above code worked the way I was expecting, commented out after I finished the code.
# print(morse_alphabet)
# print(morse_alphabet['a'])

#Make an input for the translated message, use .lower to make sure it works with my list
#Make a while loop to convert message to morse code. The message is currently set to make
#a list of characters in morse code

on = True
while on:
    message = input("What do you need translated? ").lower()
    try:
        translate = [morse_alphabet[letter] for letter in message]
    # Create an exception if the user inputs a value that doesn't map to the morse code dictionary (e.g. '!')
    except KeyError:
        print("Sorry, all values must be letters and spaces. Please try again and make sure your message "
              "doesn't include any punctuation marks or special characters")
    # Print the morse code message using .join() to merge the morse code letters from the 'translate' variable
    else:
        on = False
        print(' '.join(translate))

# Possible future steps: Add a function to allow the program to translate from morse code to English.



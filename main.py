from time import sleep
import RPi.GPIO as GPIO
# Usimg GPIO 24 (Pin 18) as output and Pin 6 as Ground

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#If you're not using GPIO 24, chage number here
pin = 18

GPIO.setup(pin, GPIO.OUT)

Rate=0.25

def pause():
    sleep(Rate)

def dash():
    GPIO.output(pin, 1)
    sleep(4*Rate)
    GPIO.output(pin, 0)
    sleep(Rate)

def dot():
    GPIO.output(pin, 1)
    sleep(Rate)
    GPIO.output(pin, 0)
    sleep(Rate)

CODE = {' ': '_',
"'": '.----.',
'(': '-.--.-',
')': '-.--.-',
',': '--..--',
'-': '-....-',
'.': '.-.-.-',
'/': '-..-.',
'0': '-----',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.',
':': '---...',
';': '-.-.-.',
'?': '..--..',
'A': '.-',
'B': '-...',
'C': '-.-.',
'D': '-..',
'E': '.',
'F': '..-.',
'G': '--.',
'H': '....',
'I': '..',
'J': '.---',
'K': '-.-',
'L': '.-..',
'M': '--',
'N': '-.',
'O': '---',
'P': '.--.',
'Q': '--.-',
'R': '.-.',
'S': '...',
'T': '-',
'U': '..-',
'V': '...-',
'W': '.--',
'X': '-..-',
'Y': '-.--',
'Z': '--..',
'_': '..--.-'}

def Encription(sentence):
    sentence = sentence.upper()
    encocdingPhrase= ""
    for character in sentence:
        encodingPhrase += CODE[character] + " "
    return encodingPhrase

while True:
    Phrase = input("Enter sentence: ")
    encodingPhrase = Encription(Phrase)
    print(encodingPhrase)
    for i in encodingPhrase:
        if i == ".":
            dot()
        elif i == "-":
            dash()
        else:
            pause()
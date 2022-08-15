import os
import time

def animate_text(text):
    number_of_chars = 1
    while True:
        print('\n')
        print(text[0:number_of_chars])
        number_of_chars += 1

        if number_of_chars > len(text):
            number_of_chars = 0

        time.sleep(0.2)
        os.system('clear')

animate_text('Hello SoftUni!')
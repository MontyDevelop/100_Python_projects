from time import time
import random as r

test = [
    "A Paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
    "My name is Monty",
    "Our country just celebrated the republic day 2026"
]

test1 = r.choice(test)

def mistake(text, original):
    error = 0

    for i in range(len(original)):
        try:
            if text[i] != original[i]:
                error += 1
        except:
            error += 1

    error += abs(len(text) - len(original))
    print("No of mistakes:", error)

def speed():
    print("TYPING SPEED CALCULATOR")
    print(test1)
    print()

    start_time = time()
    test_input = input("Enter: ")
    end_time = time()

    time_taken = end_time - start_time
    words = len(test1.split())
    wpm = round((words / time_taken) * 60)

    print("\nTime Taken:", round(time_taken, 2), "seconds")
    print("Typing Speed:", wpm, "WPM")

    mistake(test_input, test1)

speed()

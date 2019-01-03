#!/usr/bin/env python

text = ""
while text != "quit":
    text = input("Please enter chemical formula or 'quit' for exit: ")
    if text == "quit":
        print("...exiting program")
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Amonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")

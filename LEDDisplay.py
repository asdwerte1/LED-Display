def led_display():
    try:
        # User input number
        num = int(input("Please enter a number: "))
    except ValueError:
        print("Value entered is not a number")
        led_display()

    # Create a list of the values to print
    values = {
        "1": "  #  \n  #  \n  #  \n  #  \n  #  ",
        "2": "###  \n  #  \n###  \n#    \n###  ",
        "3": "###  \n  #  \n###  \n  #  \n###  ",
        "4": "# #  \n# #  \n###  \n  #  \n  #  ",
        "5": "###  \n#    \n###  \n  #  \n###  ",
        "6": "###  \n#    \n###  \n# #  \n###  ",
        "7": "###  \n  #  \n  #  \n  #  \n  #  ",
        "8": "###  \n# #  \n###  \n# #  \n###  ",
        "9": "###  \n# #  \n###  \n  #  \n###  ",
        "0": "###  \n# #  \n# #  \n# #  \n###  "
    }

    # Take user input and cast it to a list
    stringInput = str(num)
    numList = []
    for i in stringInput:
        numList.append(values[i])

    # Output the values on one line
    for row in range(5):
        for i in numList:
            print(i.split('\n')[row], end="  ")
        print()

led_display()

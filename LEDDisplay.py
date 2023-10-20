def led_display():
    try:
        #User input number
        num = int(input("Please enter a number: "))
    except ValueError:
        print("Value entered is not a number")
        led_display()

    #create a list of the values to print
    values = [
        "  #\n" * 5,
        "###\n  #\n###\n#  \n###",
        "###\n  #\n###\n  #\n###",
        "# #\n# #\n###\n  #\n  #",
        "###\n#  \n###\n  #\n###",
        "###\n#  \n###\n# #\n###",
        "###\n  #\n  #\n  #\n  #",
        "###\n# #\n###\n# #\n###",
        "###\n# #\n###\n  #\n###",
        "###\n# #\n# #\n# #\n###"
    ]

    for i in values:
        print(i)
        print("")


led_display()
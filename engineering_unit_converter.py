# ENGINEERING UNIT CONVERTER

history = []

while True:
    print("\nENGINEERING UNIT CONVERTER")
    print("1. Length Conversion")
    print("2. Temperature Conversion")
    print("3. Weight Conversion")
    print("4. Speed Conversion")
    print("5. View History")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("1. mm to inches")
        print("2. inches to mm")
        option = input("Choose conversion: ")
        value = float(input("Enter value: "))

        if option == "1":
            answer = value / 25.4
            print("Answer:", round(answer, 2), "inches")
            history.append("mm to inches")
        elif option == "2":
            answer = value * 25.4
            print("Answer:", round(answer, 2), "mm")
            history.append("inches to mm")
        else:
            print("Invalid choice")

    elif choice == "2":
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        option = input("Choose conversion: ")
        value = float(input("Enter temperature: "))

        if option == "1":
            answer = (value * 9 / 5) + 32
            print("Answer:", round(answer, 2), "F")
            history.append("Celsius to Fahrenheit")
        elif option == "2":
            answer = (value - 32) * 5 / 9
            print("Answer:", round(answer, 2), "C")
            history.append("Fahrenheit to Celsius")
        else:
            print("Invalid choice")

    elif choice == "3":
        print("1. kg to pounds")
        print("2. pounds to kg")
        option = input("Choose conversion: ")
        value = float(input("Enter weight: "))

        if option == "1":
            answer = value * 2.20462
            print("Answer:", round(answer, 2), "pounds")
            history.append("kg to pounds")
        elif option == "2":
            answer = value / 2.20462
            print("Answer:", round(answer, 2), "kg")
            history.append("pounds to kg")
        else:
            print("Invalid choice")

    elif choice == "4":
        print("1. km/h to m/s")
        print("2. m/s to km/h")
        option = input("Choose conversion: ")
        value = float(input("Enter speed: "))

        if option == "1":
            answer = value / 3.6
            print("Answer:", round(answer, 2), "m/s")
            history.append("km/h to m/s")
        elif option == "2":
            answer = value * 3.6
            print("Answer:", round(answer, 2), "km/h")
            history.append("m/s to km/h")
        else:
            print("Invalid choice")

    elif choice == "5":
        print("\nCONVERSION HISTORY")
        for item in history:
            print(item)

    elif choice == "6":
        print("Thank you for using the converter!")
        break

    else:
        print("Invalid choice")

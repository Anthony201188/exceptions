while True:
    try:
        num = int(input("Enter a number: "))
        result = num / 1
        print("Result: ", result)
        break  # exit the loop if no exception is raised
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please try again.")

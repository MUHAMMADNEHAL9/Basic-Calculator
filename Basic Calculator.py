while True:
    op = input("Enter operation (1 for add \n 2 for sub \n 3 for mul \n 4 for dvide) or 5 for 'exit' to quit: ")
    if op == '5':
      print("thank")
      break
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if op == '1':
        print(f"Result: {num1 + num2}")
    elif op == '2':
        print(f"Result: {num1 - num2}")
    elif op == '3':
        print(f"Result: {num1 * num2}")
    elif op == '4':
        if num2 == 0:
            print("Error: Division by zero.")
        else:
            print(f"Result: {num1 //num2}")
    else:
        print("0 can not dvid by any number.")

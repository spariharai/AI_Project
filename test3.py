def multiply(a, b):
    return a * b


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    print(f"Product: {multiply(a, b)}")


if __name__ == "__main__":
    main()

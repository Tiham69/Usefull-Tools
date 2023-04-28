try:
    a = int(input('Enter a year: '))
except ValueError:
    print("Input is not a year")

if (a%400 == 0 or a%4 == 0) and a%100 != 0:

    print(f"{a} is a leap year", end="")

else:

    print(f"{a} is not a leap year")


def convert_int2fizzbuzz(number: int):
    if number == 0:
        return "0"

    elif number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"

    elif number % 3 == 0:
        return "Fizz"

    elif number % 5 == 0:
        return "Buzz"

    else:
        return str(number)


def main():
    for num in range(1,101):
        print(f"{num} : {convert_int2fizzbuzz(num)}")

if __name__ == "__main__":
    main()
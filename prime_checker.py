# prime_checker.py
# fast with primes up to 13 digits

def is_prime(n):
    # Function to check if a number is prime
    for i in range(2, n):
        if i**2 > n:
            break
        list = str(n/i).split('.')
        if list[1] == '0':
            if i != 1 and i != n:
                print(f"{n} is divisible by {i}, hence it is not a prime number.")
                return False
    return True

while True:
    try:
        number = int(input("Enter a positive integer (or -1 to exit): "))
        while number < -1:
            print("Please enter a positive integer or -1 to exit.")
            number = int(input("Enter a positive integer (or -1 to exit): "))
        if number == -1:
            print("Exiting the program.")
            break

        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
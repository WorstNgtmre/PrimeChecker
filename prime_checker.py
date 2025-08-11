# prime_checker.py
# fast with primes up to 15-16 digits

def is_prime(n):
    # Function to check if a number is prime

    if n % 2 == 0 or n % 3 == 0:
        print(f"{n} is even or divisible by 3, hence it is not a prime number.")
        return False

    # Suboptimal aparently
    """if n % 2 == 0:
        print(f"{n} is even, hence it is not a prime number.")
        return False
    
    primes = [2]"""

    for i in range(5, n, 2):  # Check only odd numbers starting from 3
        if i**2 > n:
            break
        # This part is commented out because it is not optimal and was not used in the final version but made by ME
        """i_is_prime = True
        # Check if the number is divisible by any previously found primes
        for prime in primes:
            if i % prime == 0:
                i_is_prime = False
                break
        # If the number is divisible by any of the previously found primes, skip further checks
        if i_is_prime == False:
            continue
        else:
            primes.append(i)"""
        
        # Check if n is divisible by i
        if n % i == 0:
            print(f"{n} is divisible by {i}, hence it is not a prime number.")
            return False

        # This part is commented out because it is not optimal and was not used in the final version but made by ME
        """
        list = str(n/i).split('.')
        if list[1] == '0':
            if i != 1 and i != n:   
                print(f"{n} is divisible by {i}, hence it is not a prime number.")
                return False
        """
        
    #print(primes)
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
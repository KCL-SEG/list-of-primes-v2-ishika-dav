"""List of prime numbers generator."""

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Number of primes must be a positive integer.")
    
    list = []
    num = 2  
    while len(list) < number_of_primes:
        if is_prime(num):
            list.append(num)
        num += 1
    return list

try:
    number_of_primes = int(input("How many prime numbers do you want? "))
    prime_numbers = primes(number_of_primes)
    print(prime_numbers)  
except ValueError as e:
    print("Error: ",e)    




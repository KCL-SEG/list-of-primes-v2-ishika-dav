"""List of prime numbers generator."""

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer greater than one")
    
    prime_list = []
    num = 2  
    while len(prime_list) < number_of_primes:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

try:
    number_of_primes = 20
    prime_numbers = primes(number_of_primes)
    print(prime_numbers)  

except ValueError as e:
    print("Error:",e)  
  




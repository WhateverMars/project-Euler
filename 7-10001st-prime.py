#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10001st prime number?


# this test function checks to see if there exists any factors between 1 and num not inclusive. If so, then num is not prime.
def is_prime(num):

    # prime numbers cannot be below 2
    if num < 2:
        return False
    
    # we are looking to see if there are any factors other than 1 and num, if so then not prime
    for i in range( 2, num):
        if num%i == 0:
            return False

    return True


# this function finds the nth prime function
def nth_prime(n):
    count = 0
    i = 1

    # repeat until the count reaches the nth prime
    while count < n:

        if is_prime(i):
            count += 1
            if count == n:
                return i
        i += 1
    

print(nth_prime(10001))

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10001st prime number?
import time

st_time = time.time()

# this test function checks to see if there exists any factors between 1 and num not inclusive. If so, then num is not prime.
def is_prime(num):

    # prime numbers cannot be below 2
    if num < 2:
        return False

    # special cases for 2 and 3 allows us to iterate by 2 in the future. No even primes other than 2
    if num == 2: 
        return True

    if num == 3:
        return True

    # we are looking to see if there are any factors other than 1 and itself, if so then not prime   
    i = 3
    while i < num:
        if num%i == 0: 
            return False
        i += 2


    return True


# this function finds the nth prime function
def nth_prime(n):
    count = 0
    i = 1

    # repeat until the count reaches the nth prime
    while count < n:
        if is_prime(i):
            count += 1
            #print('primes found: '+str(count))
            if count == n:
                return i

        # can increment by 2 as all prime numbers above 2 are odd
        if i<3:
            i += 1
        else:
            i += 2
    

print(nth_prime(10001))
print('time: '+ str(time.time()-st_time))
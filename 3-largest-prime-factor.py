# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# first get a list of prime numbers

import time



# this test function checks to see if there exists any factors between 1 and num not inclusive. If so, then num is not prime.
def is_prime_alt(num):

    # we are looking to see if there are any factors other than 1 and num, if so then not prime
    for i in range( 2, num):
        if num%i == 0:
            return False

    return True


# this function checks for factors by dividing down the original number by each factor it finds 
def largest_prime_factor(num):

    i = 2
    highest_factor = 1

    # loop until we reduce num to it's smallest factor, one
    while num > 1:

        # if factor is a factor
        if num % i == 0:

            # update our highest confirmed factor
            highest_factor = i

            # divide num by the factor 
            while num % i == 0:
                num = num // i

        # increment through i
        i += 1
        
    return highest_factor



st_time = time.time()      

print('largest prime factor: ' + str(largest_prime_factor(600851475143)))

print('runtime: '+ str(time.time()-st_time))

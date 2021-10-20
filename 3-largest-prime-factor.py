# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# first get a list of prime numbers

import time



# this function checks for factors by dividing down the original number by each factor it finds 
def largest_prime_factor(num):

    i = 2
    highest_factor = 1

    # loop until we reduce num to it's smallest factor, one
    while num > 1:

        # if i is a factor
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

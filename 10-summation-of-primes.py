# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

import time

st_time = time.time()

def is_prime(num):
    
    if num < 2:
        return False

    if num == 2:
        return True

    if num == 3:
        return True

    if num % 2 == 0:
        return False

    if num % 3 == 0:
        return False

    if num < 9:
        return True


    i = 5

    # we limit our check to factors below sqrt(num). If no factors below this, num is prime.
    while i <= num**(1/2):
        
        # all primes above 3 can be written as 6x+1 or 6x-1

        # if 6x - 1 is a factor
        if num % i == 0:

            return False

        # is 6x + 1 is a factor
        if num % (i+2) == 0:
        
            return False

        # increment by 6 to reach the next possible prime pair
        i += 6
    
    return True


def summation_of_primes(num):
    sum = 0 

    i = 1
    while i < num:       

        # if below 3 increment by 1
        if i < 3:

            if is_prime(i):

                sum += i

            i += 1 

        # if 3 incement by 2
        if i == 3:

            if is_prime(i):

                sum += i

            i += 2

        # if above 3 increment by 6 because primes must be 6x + 1 or 6x - 1
        if i > 3:

            if is_prime(i):

                sum += i
                
            if is_prime(i+2):

                sum += i+2

            i += 6
       
    return sum


print(summation_of_primes(2000000))

print('Time: '+ str(time.time()- st_time))

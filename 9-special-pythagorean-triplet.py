# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time


st_time = time.time()

# This fn finds the pythagorean triplet whose sum adds to num and then returns their product
def pythagorean_triplet_prod(num):

    for a in range(1, num):

        for b in range(1, num):

            # this condition must be satisfied for it to be the pythagorean triplet we're looking for
            if ((a**2 + b**2)**(1/2)) == num - b - a:
                c = num - b - a

                # this optional print statment will print out what the triplet actually is.
                #print('a = '+str(a)+' b = '+str(b)+' c = '+str(c))
                return a*b*c

    # in case one does not exist
    return 'Not Found'


print(pythagorean_triplet_prod(1000))

# print out the runtime if required
#print('runtime = ' + str(time.time() - st_time))

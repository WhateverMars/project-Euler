# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# this function returns the smallest integer I that leaves no remainder for I%n where n is the series of numbers [1,2,3,4,... max]
def smallest_multiple(max):

    # start at 1 as 0 gives mod division issues
    i = 1

    # this loop checks each number increasing by 1 for each completed loop without finding the answer
    while True:

        # restart at 1 for each new test integer
        j = 1

        # while division leaves no remainder keep checking how high this is true
        while i % j == 0:

            # check if the max is reached, if true, return value, otherwise test next higher j
            if j == max:
                return(i)
            j += 1

        i += 1


print(smallest_multiple(20))

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_sum(num1, num2, max):
    
    sum = 0

    for i in range(1,max):

        if i%num1 == 0:

            sum += i

        # elif means there will be no repeated values such as 15 and it's multiples
        elif i%num2 == 0:

            sum += i

    return sum

print(multiples_of_sum(3, 5, 1000))
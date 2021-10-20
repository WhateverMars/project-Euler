#The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2 = 385

#The square of the sum of the first ten natural numbers is, (1+2+...+10)^2 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# this function finds the difference between the sum of the squares of a given numbers and the square of the sum.
def square_sum_diff(max):
    sum_of_squares = 0
    squares_of_sum = 0

    # square each value first and then add to the total sum
    for i in range(1, max + 1):
        sum_of_squares += i**2

    # sum all the numbers first and then square the result
    sum = 0
    for i in range(1, max + 1):
        sum += i

    squares_of_sum = sum**2

    # find the difference
    square_sum_diff = squares_of_sum - sum_of_squares
    return square_sum_diff


print(square_sum_diff(100))

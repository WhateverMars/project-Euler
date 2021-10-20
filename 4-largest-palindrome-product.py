# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# this function checks if a number is a palindrome by converting to a string and seeing if it matches its reverse
def is_palindrome(num):
    string = str(num)

    if string == string[::-1]:
        return True
    else:
        return False


# this function returns the largest palindrome number which has 2 factors of 3 digits each.
def largest_palindrome_factor():

    largest_palindrome = 0

    # the range of numbers with 2 3 digit factors is 10001 to 998001 which we step through backwards to save time 
    for i in range(998001, 10001, -1):

        # check if each number is a palindrome
        if is_palindrome(i):
            largest_palindrome = i

            # check if it has 2 factors with 3 digits, ie between 100 and 1000
            for i in range(100, 1000):
                if largest_palindrome%i == 0 and largest_palindrome/i < 1000:
                    print(str(largest_palindrome)+ ' = '+str(i) +' x ' + str(largest_palindrome//i))
                    return(largest_palindrome)
            
    return 'Error: not found'

print(largest_palindrome_factor())


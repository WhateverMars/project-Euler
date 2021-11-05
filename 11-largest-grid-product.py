'''
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
'''

grid_string = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'


# This fn converts the grid which is given as a string into an array of numbers. 
# It assumes each number is given as a 2 digit string and separated by a space.
def read_grid(string):

    grid = []
    i = 0
    while i < len(string):
        # converts the 2 digits into an int and adds to the grid array, then skips the space.
        grid.append(int(string[i]+string[i+1]))
        i += 3

    return grid


# This fn returns the largest product of 4 adjacent values in a vertical, horizontal or diagonal line.
# It assumes the original grid is 20*20.
def largest_grid_product(grid):

    product = 1
    
    # each of the below lambda functions calculates the product of 4 adjacent values in a specific direction.

    # h_product is in the horizontal direction
    h_product = lambda i : grid[i]*grid[i+1]*grid[i+2]*grid[i+3]

    # v_product is in the vertical direction 
    v_product = lambda i : grid[i]*grid[i+20]*grid[i+40]*grid[i+60]
    # dd_product is in the down-right diagonal direction
    dd_product = lambda i : grid[i]*grid[i+21]*grid[i+42]*grid[i+63]
    # du_product is in the up-right diagonal direction
    du_product = lambda i : grid[i]*grid[i-19]*grid[i-38]*grid[i-57]

    j = 0
    while j < len(grid):

        # in the first 3 rows we do not check du_product as there they are out of bounds
        if j < 60: 

            # in the last 3 columns we also do not check h_product or dd_product as they are out of bounds
            if j%20 < 17:
                if max(h_product(j), v_product(j), dd_product(j)) > product:
                    product = max(h_product(j), v_product(j), dd_product(j))
            else:
                if v_product(j)>product:
                    product = v_product(j)

        # after the first 3 rows and before the last 3 rows we check all 4 directions
        elif j < 340: 

            # again in the last 3 columns we only check v_product as all others are out of bounds
            if j%20 < 17:
                if max(h_product(j), v_product(j), dd_product(j), du_product(j)) > product:
                    product = max(h_product(j), v_product(j), dd_product(j), du_product(j))
            else:
                if v_product(j)>product:
                    product = v_product(j)

        # in the last 3 rows we only check h_product and du_product as the others are out of bounds
        else: 
            if j%20 < 17:
                if max(h_product(j), du_product(j)) > product:
                    product = max(h_product(j), du_product(j))
            else:
                # do nothing, everything is out of bounds
                pass
        
        j += 1

    return product

print(largest_grid_product(read_grid(grid_string)))
'''
[mohammad],3 => [mm] , [oamd] , [ha]
m = 1
o = 2
h = 3
a = 2
m = 1
m = 2
a = 3
d = 2
'''

def zigzag(array,num_rows):
    # If number of rows is 1, return the original text (no zigzag needed)
    if num_rows == 1:
        return array

    # Create a list to store strings for each row
    rows = num_rows*['']

    # Current row index
    curr_row = 0

    # Direction controller:
    # -1 means going up, 1 means going down
    going_down = -1

    # Loop through each character in the input text
    for i in array:
        rows[curr_row] += i

        # If we are at the top or bottom row, change direction
        if curr_row == 0 or curr_row == (num_rows-1) :
            going_down = -1 * going_down

        # Move to the next row based on the current direction
        going_down += 1 if going_down > 0 else -1
        
    return rows


print(zigzag('mohammad',3))
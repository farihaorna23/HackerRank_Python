# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example

# There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

# 0.400000
# 0.400000
# 0.200000
# Function Description

# Complete the plusMinus function in the editor below.

# plusMinus has the following parameter(s):

# int arr[n]: an array of integers
# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

# Input Format

# The first line contains an integer, , the size of the array.
# The second line contains  space-separated integers that describe .

# Constraints



# Output Format

# Print the following  lines, each to  decimals:

# proportion of positive values
# proportion of negative values
# proportion of zeros
# Sample Input

# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
# Sample Output

# 0.500000
# 0.333333
# 0.166667


def plusMinus(arr):
    # Write your code here
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_count += 1
        elif arr[i] < 0:
            negative_count += 1
        elif arr[i] > 0:
            positive_count += 1
    
    length_of_arr = len(arr)
    ratio_of_positive = positive_count/length_of_arr
    ratio_of_negative = negative_count/length_of_arr
    ratio_of_zero = zero_count/length_of_arr
    
    print(f"{round(ratio_of_positive, 6)} \n"
    f"{round(ratio_of_negative, 6)} \n"
    f"{round(ratio_of_zero, 6)} \n")

plusMinus([-4, 3, -9, 0, 4, 1])
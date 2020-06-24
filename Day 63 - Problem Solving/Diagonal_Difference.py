# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown below:
# 1 2 3
# 4 5 6
# 9 8 9  


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d1 = 0
    d2 = 0
  
    for i in range(0, n): 
      
        for j in range(0, n): 
          
            # finding sum of primary diagonal 
            if (i == j): 
                d1 += arr[i][j] 
  
            # finding sum of secondary diagonal 
            if (i == n - j - 1): 
                d2 += arr[i][j] 
          
    # Absolute difference of the sums 
    # across the diagonals 
    return abs(d1 - d2); 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

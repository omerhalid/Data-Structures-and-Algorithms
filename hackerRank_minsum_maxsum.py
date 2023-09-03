#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0
    
    arr.sort()
    
    for index, value in enumerate (arr):
        if index != 0:
            max_sum += value       
        if index != len(arr)-1:
            min_sum += value 

    
    print(f'{min_sum} {max_sum}')
        

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)

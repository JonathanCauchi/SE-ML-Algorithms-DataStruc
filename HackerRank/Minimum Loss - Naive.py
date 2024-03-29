#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#


def minimumLoss(price):
    # Write your code here
    min_value = sys.maxsize
    prices = [(price[i], i) for i in range(len(price))]
    prices = sorted(prices, reverse=True)
    
    for i in range(len(prices)-1):
        if prices[i][0] - prices[i+1][0] < min_value and prices[i][1] < prices[i+1][1]:
            min_value = prices[i][0] - prices[i+1][0]
            
    return min_value
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)
    
    # print(result)

    fptr.write(str(result) + '\n')

    fptr.close()


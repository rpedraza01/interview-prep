# sock_merchant.py

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
# n is the number of socks, ar is the list of individual socks in the function sockMerchant
def sockMerchant(n, ar):
    # create the variable unique_nums and set it to equal a list() which has removed all duplicate numbers thanks to set()
    unique_nums = list(set(ar))
    # create the variable total_pairs and set it to equal 0
    total_pairs = 0
    # create a for loop that looks at num in variable unqiue_nums
    for num in unique_nums:
        # total_pairs is then += to the ar array that returns the number of occurrences a sock pair comes up thanks to the count() // 2
        total_pairs += ar.count(num) // 2
        # function then returns the final number of total sock pairs by returning the variable total_pairs
    return total_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

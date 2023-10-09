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
    if len(price) >= 2 and len(price) <= 2 * 10**5:
        loss_dct = {}
        
        for i in range(0, len(price)-1):
            purchase = price[i]
            if purchase >= 1 and purchase <= 10**16:
                min_loss = None
                if i not in loss_dct:
                    loss_dct[i] = None
                for j in range(i+1, len(price)):
                    compare = price[j]
                    if compare >= purchase:
                        continue
                    else:
                        value = purchase - compare
                        if min_loss and value < min_loss:
                            min_loss = value
                        if min_loss is None:
                            min_loss = value
                    loss_dct[i] = min_loss
                    
        result = loss_dct.values()
        result = [value for value in result if value is not None]
        
        return min(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)
    
    # print(result)

    fptr.write(str(result) + '\n')

    fptr.close()


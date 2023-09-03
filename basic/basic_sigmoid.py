"""
  𝑠𝑖𝑔𝑚𝑜𝑖𝑑(𝑥)=1/1+𝑒−𝑥
  is sometimes also known as the logistic function. It is a non-linear function used not only in Machine Learning (Logistic Regression), but also in Deep Learning.
"""

import math

# GRADED FUNCTION: basic_sigmoid

def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    # (≈ 1 line of code)
    # s = 
    # YOUR CODE STARTS HERE
    s=1/(1+(math.exp(-x)))
    
    # YOUR CODE ENDS HERE
    
    return s
print("basic_sigmoid(1) = " + str(basic_sigmoid(1)))

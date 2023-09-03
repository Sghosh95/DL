# GRADED FUNCTION: sigmoid
import numpy as np
def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """
    
    # (≈ 1 line of code)
    # s = 
    # YOUR CODE STARTS HERE
    s=1/(1+np.exp(-x))
    
    # YOUR CODE ENDS HERE
    
    return s

a=np.array([1,2,3])
print("sigmoid(a) = " + str(sigmoid(a)))

# GRADED FUNCTION: sigmoid_derivative

def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    
    #(≈ 2 lines of code)
    # s = 
    # ds = 
    # YOUR CODE STARTS HERE
    s=1/(1+np.exp(-x))
    ds=s*(1-s)
    
    # YOUR CODE ENDS HERE
    
    return ds

t_x = np.array([1, 2, 3])
print ("sigmoid_derivative(t_x) = " + str(sigmoid_derivative(t_x)))
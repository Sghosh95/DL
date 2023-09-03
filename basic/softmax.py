"""You can think of softmax as a normalizing function used when your algorithm needs to classify two or more classes.
for 𝑥∈ℝ1×𝑛, 
 
𝑠𝑜𝑓𝑡𝑚𝑎𝑥(𝑥)=𝑠𝑜𝑓𝑡𝑚𝑎𝑥([𝑥1  𝑥2.. .𝑥𝑛])
                =[𝑒𝑥1/∑𝑗𝑒𝑥   𝑗𝑒𝑥2/∑𝑗𝑒𝑥𝑗...𝑒𝑥𝑛/∑𝑗𝑒𝑥𝑗]"""

import numpy as np
def softmax(x):
    """Calculates the softmax for each row of the input x.

    Your code should work for a row vector and also for matrices of shape (m,n).

    Argument:
    x -- A numpy matrix of shape (m,n)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (m,n)
    """
    
    #(≈ 3 lines of code)
    # Apply exp() element-wise to x. Use np.exp(...).
    # x_exp = ...

    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).
    # x_sum = ...
    
    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.
    # s = ...
    
    # YOUR CODE STARTS HERE
    x_exp=np.exp(x)
    x_sum=np.sum(x_exp,axis=1,keepdims=True)
    s=x_exp/x_sum
    
    # YOUR CODE ENDS HERE
    
    return s


t_x = np.array([[9, 2, 5, 0, 0],
                [7, 5, 0, 0 ,0]])
print("softmax(x) = " + str(softmax(t_x)))
# x_exp=np.exp(t_x)
# print(x_exp)
# x_sum=np.sum(x_exp,axis=1,keepdims=True)
# print(x_sum)
# s=x_exp/x_sum
# print(s)


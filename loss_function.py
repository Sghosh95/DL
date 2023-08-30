import numpy as np
def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L1 loss function defined above
    """
    
    #(≈ 1 line of code)
    # loss = 
    # YOUR CODE STARTS HERE
    loss=-(1/5) * np.sum(y * np.log(yhat) + (1 - y) * np.log(1 - yhat))
    
    # YOUR CODE ENDS HERE
    
    return loss

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1(yhat, y)))


# GRADED FUNCTION: L2

"""mplement the numpy vectorized version of the L2 loss. There are several way of implementing the L2 loss but you may find the function np.dot() useful. As a reminder, if  𝑥=[𝑥1,𝑥2,...,𝑥𝑛]
 , then np.dot(x,x) =  ∑𝑛𝑗=1𝑥2𝑗
 ."""

def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L2 loss function defined above
    """
    
    #(≈ 1 line of code)
    # loss = ...
    # YOUR CODE STARTS HERE
    loss=np.dot(yhat-y,yhat-y)
    
    # YOUR CODE ENDS HERE
    
    return loss
yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])

print("L2 = " + str(L2(yhat, y)))
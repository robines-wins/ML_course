# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np

def compute_cost_MSE(y,tx,w):
    e=y-(tx @ w)
    return (1/(2*y.shape[0]))*(e.T @ e)

def least_squares(y, tx):
    """calculate the least squares."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    # ***************************************************

    w = np.linalg.solve(tx.T.dot(tx),tx.T.dot(y)) #return best weight
    return compute_cost_MSE(y, tx, w), w

# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares solution."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    # ***************************************************
    return np.linalg.solve(tx.T.dot(tx),tx.T.dot(y))
    #return np.linalg.inv(tx.T.dot(tx)).dot(tx.T).dot(y)
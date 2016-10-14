# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lamb):
    """implement ridge regression."""
    lambp = lamb*(2*tx.shape[0])
    #return np.linalg.inv(tx.T.dot(tx)+lambp*np.eye(tx.shape[1])).dot(tx.T).dot(y)
    #return np.linalg.inv((tx.T @ tx) + lambp*np.eye(tx.shape[1])) @ tx.T @ y
    return np.linalg.solve(tx.T.dot(tx)+lambp*np.eye(tx.shape[1]),tx.T.dot(y))
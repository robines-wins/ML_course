# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    m =np.ones((x.shape[0],degree+1))
    for i in range(x.shape[0]):
    #m =np.ones((len(x),degree+1))
    #for i in range(len(x)):
        for j in range(1,degree+1):
            m[i][j] = x[i]**j#x[i]*m[i][j-1] #
    return m

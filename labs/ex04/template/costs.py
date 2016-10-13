# -*- coding: utf-8 -*-
"""A function to compute the cost."""


def compute_mse(y, tx, beta):
    """compute the loss by mse."""
    e = y - tx.dot(beta)
    mse = e.dot(e) / (2.0 * len(e))
    return mse
    """e=y-(tx @ beta)
    return 1/2/y.shape[0]*(e.T @ e)"""

import numpy as np

def future_value(P, r, n, t):
    return P * (((1 + r/n)**(n*t) - 1) / (r/n)) * (1 + r/n)

def select_companies(roi, volatility, roi_threshold, volatility_threshold):
    return roi[(roi > roi_threshold) & (volatility < volatility_threshold)]

def calculate_investment_ratios(volatility):
    inverse_volatility = 1 / volatility
    return inverse_volatility / inverse_volatility.sum()
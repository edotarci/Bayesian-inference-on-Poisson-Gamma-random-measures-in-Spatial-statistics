import numpy as np
from scipy.stats import chi2

def E1_inverse(x):
    d_E1 = 1e-9
    return chi2.ppf(1-d_E1/2*x, d_E1)/2

def E1(x):
    d_E1 = 1e-9
    return 2/d_E1 * (1-chi2.cdf(2*x, d_E1))

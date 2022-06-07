# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 08:57:44 2022

@author: Sascha

Daily Coding Problem #32 (Jane Street)

Suppose you are given a table of currency exchange rates, represented as a 2D 
array. Determine whether there is a possible arbitrage: that is, whether there 
is some sequence of trades you can make, starting with some amount A of any 
currency, so that you can end up with some amount greater than A of that 
currency.

There are no transaction costs and you can trade fractional quantities.
"""

import numpy as np

EUR = [1,       1.07184, 0.85779, 140.175, 7.13646]
USD = [0.93275, 1,       0.80052, 130.808, 6.65813]
GBP = [1.16428, 1.24859, 1,       163.337, 8.31326]
JPY = [0.00713, 0.00764, 0.00612, 1,       0.05088]
CNY = [0.14000, 0.15009, 0.12015, 19.6335, 1      ]

# taken from https://www.oanda.com/currency-converter/ on the 6th of June 2022.

exchange_rates = np.array([EUR, USD, GBP, JPY, CNY])

def arbitrage(exchange_rates):
    '''
    Reference: https://github.com/r1cc4rdo/daily_coding_problem
    
    The general idea is to calculate (starting from the first currency in the
        array), what the exchange rates for all other transactions should be,
        based on the exchange rates for your starting currency. If the calculated
        exchange rates differ too much from the original ones, there is possible
        arbitrage.
    
    For example, for five currencies and given the exchange rates from the 
        first to the other 4 [b, c, d, e]:
            
      |  A   B   C   D   E
    --+------------------
    A |  1   b   c   d   e
    B | 1/b  1  c/b d/b e/b
    C | 1/c b/c  1  d/b e/c
    D | 1/d b/d c/d  1  e/d
    E | 1/e b/e c/e d/e  1

    Parameters
    ----------
    exchange_rates : 2D array
        an array of currency exchange rates.

    Returns
    -------
    Boolean
        True if there is possible arbitrage; False if there is no possible 
            arbitrage.

    '''
    computed_exchange_rates = np.zeros((5,5))
    
    for currency in range(len(exchange_rates)):
        computed_exchange_rates[currency,:] = exchange_rates[0,:] / exchange_rates[0,currency]
        
    return np.allclose(exchange_rates, computed_exchange_rates)
    # np.allclose checks if two arrays are element-wise equal within tolerance
    # returns True if absolute(a - b) <= (atol + rtol * absolute(b))
    # with standard values rtol=1e-05, atol=1e-08

print(arbitrage(exchange_rates))
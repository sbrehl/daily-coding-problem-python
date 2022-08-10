# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 08:58:08 2022

@author: Sascha

Daily Coding Problem #47 (Facebook)

Given a array of numbers representing the stock prices of a company in 
chronological order, write a function that calculates the maximum profit 
you could have made from buying and selling that stock once. You must buy 
before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could 
buy the stock at 5 dollars and sell it at 10 dollars.
"""

import math

def stock_profit(array):
    '''
    This funcion calculates the maximum profit one could have made from buying
    and selling a stock of a certain company once.
    The idea is to check every possible combination of buying and selling
    prices (within the constraint that the index of the selling price has to 
    be higher than the index of the buying price), and return the maximum

    Parameters
    ----------
    array : array
        stock prices of a company in chronological order.

    Returns
    -------
    max(profit) : int
        the maximum profit to be made by buying and selling the stock once.

    '''
    
    # looks complicated, but e.g. for an array of length 5 we have to check
    # (n(n+1) / 2) combinations of prices, which is the length that the profit
    # list needs to have
    profit = [0] * int((((len(array) -  1)  * (len(array))) / 2))
    count = 0
    
    # loop with buy = index of the current buying price
    for buy in range(len(array)):
        # loop with sell = index of the current selling price
        for sell in range(buy + 1, len(array)):
            # calculates the profit by subtracting the buying price from the
            # selling price
            profit[count] = array[sell] - array[buy]
            count += 1    
    
    return max(profit)

a = [9, 11, 8, 5, 7, 10]
print(stock_profit(a))
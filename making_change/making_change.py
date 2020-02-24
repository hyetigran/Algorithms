#!/usr/bin/python

import sys


def making_change(amount, denominations):
    ways = [1] + [0] * amount

    for coin in denominations:
        for i in range(coin, amount+1):
            ways[i] += ways[i - coin]

    print(ways)
    return ways[amount]


def count(S, m, n):

    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1

    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <= 0 and n >= 1):
        return 0

    # count is sum of solutions (i)
    # including S[m-1] (ii) excluding S[m-1]
    return count(S, m - 1, n) + count(S, m, n-S[m-1])


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")

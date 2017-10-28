# A permutation of length nn is an ordering of the positive integers {1,2,…,n}{1,2,…,n}.
# For example, π=(5,3,2,1,4)π=(5,3,2,1,4) is a permutation of length 55.

# Given: A positive integer n≤7n≤7.
# Return: The total number of permutations of length nn, followed by a list of all such permutations (in any order).
from itertools import permutations


def enumerategene(n):
    order = list(permutations(range(1, n + 1)))
    print(order)
    count = 1
    while n > 0:
        count *= n
        n -= 1
    print(count)
    print(order)

enumerategene(5)
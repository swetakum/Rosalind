"""
P = (x/2)^GC + (1-x/2)^AT
"""

import math

def calcProbability(dna, arr):
    gc = dna.count('G') + dna.count('C')
    at = dna.count('A') + dna.count('T')
    probarray =[]
    for i in range(len(arr)):
        probarray.append('%0.3f'%math.log10(((arr[i]/2)**gc)*(((1- arr[i])/2)**at)))
    print (probarray)
    return probarray

dna = 'CTGCCTAGAGCGGCTATAAGTGGATTTGTGTCAAGTTGATTGAAACGTGCCCTAAGCATTGACGAGATATAGTATGTTGGGAATAGGGTCTGG'
arr = [0.076, 0.136, 0.164, 0.208, 0.258, 0.333, 0.398, 0.424, 0.467, 0.526, 0.589, 0.611, 0.699, 0.744, 0.757, 0.829, 0.868, 0.917]
calcProbability(dna, arr)
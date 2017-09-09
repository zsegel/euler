"""
https://projecteuler.net/problem=75

Okay. Let's start with the triples and work backwards to the wires.
There's apparently a formula for generating 'primitive' Pythagorean triples (a, b, c):

	any positive integers m and n, such that
		m > n
		m is even XOR n is even
		m and n are coprime

	produce a Pythagorean triple (a, b, c):
		a = m**2 - n**2
		b = 2*m*n
		c = m**2 + n**2

This doesn't produce all Pythagorean triples, but all triples can be found by 
multiplying the primitive ones we generate by a constant k.
"""
import time
start = time.time()

def are_coprime(m, n):
    """uses Euclid's algorithm to test coprimality; m > n"""
    while m%n:
        m, n = (n, m%n)
    return n == 1

# W's keys will be wire lengths; values will be Pythagorean triplets for each wire length
W = {}

# m's greater than 865 don't make any triangles with perimeters less than 1,500,000
for m in range(2, 866):
    for n in range(1, m):
        if are_coprime(m, n) and (m%2 ^ n%2) and 2*m * (m+n) <= 1500000:
            
            # make the primitive triple and put it in W
            t = sorted([m**2 - n**2, 2*m*n, m**2 + n**2])
            wire = sum(t)
            
            if wire in W:
                if t not in W[wire]:
                    W[wire].append(t[:])
            else:
                W[wire] = [t[:]]
            
            # add relevant multiples of the primitive triple to W
            k = 2
            while k*wire <= 1500000:
                if k*wire in W:
                    if [k*side for side in t] not in W[k*wire]:
                        W[k*wire].append([k*side for side in t])
                else:
                    W[k*wire] = [[k*side for side in t]]
                k += 1

# count the wire lengths in W that only correspond to one triple
count = 0
for wire in W.keys():
    if len(W[wire]) == 1:
        count += 1
        
end = time.time()
print count, end-start

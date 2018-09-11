from math import factorial

def solution(n):
    return factorial(n*2) // (factorial(n+1) * factorial(n))

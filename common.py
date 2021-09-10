import math
from re import X

from matplotlib.pyplot import axes

def getHarmonicFunction(a, maxN, phi, f):
    return lambda n, a = a, maxN = maxN, phi = phi, f = f: a * math.sin(2 * math.pi * f * n / maxN + phi)

def getPowersOfTwo(stop, start):
    return list(map(lambda x: 2 ** x, range(stop, start)))

def getpip():
    pass

def parsePiExpression(str):
    try:
        return eval(str, {"pi": math.pi})
    except:
        raise ValueError
        
def parseArray(str):
    return list(map(parsePiExpression, str.replace(" ", "").split(",")))

def parseNatural(str):
    try:
        value = int(str)
    except:
        raise ValueError
    if (value < 1):
        raise ValueError
    return value

def getSampledFunc(func, sampleStep):
    def calculate(x):
        return func(x - (x % sampleStep))
    return lambda x: calculate(x)
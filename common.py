import math
from re import X

from matplotlib.pyplot import axes

def getHarmonicFunc(a, maxN, phi, f):
    return lambda n: a * math.sin(2 * math.pi * f * n / maxN + phi)

def getSawFunc(a, t, phi):
    def calculate(x):
        param = x % t
        if (param != float(t)):
            return param / (t) * a
        else:
            return (param  - float(t)) / (t / 4) * a
    return lambda x: calculate(x)

def getTriangleFunc(a, t, phi):
    def calculate(x):
        param = (x - phi) % t
        if (param < float(t) / 4):
            return param / (t / 4) * a
        elif (param < float(t) * 3 / 4):
            return -(param - float(t) / 2) / (t / 4) * a
        else:
            return (param  - float(t)) / (t / 4) * a
    return lambda x: calculate(x)

def getSampledFunc(func, sampleStep):
    def calculate(x):
        return func(x - (x % sampleStep))
    return lambda x: calculate(x)

def sumFuncs(funcs):
    return lambda x: sum([func(x) for func in funcs])

def getTaylorHarmonicFunc(a, maxN, phi, f, k):
    func = getTaylorSinFunc(k)
    return lambda n: a * func(2 * math.pi * f * n / maxN + phi)

def getTaylorSinFunc(k):
    return getTaylorFunc(lambda x, i: ((-1) ** (i % 2)) * math.pow(x, 2 * i + 1) / math.factorial(2 * i + 1), k)

def getTaylorFunc(elementFunc, k):
    return lambda x: sum([elementFunc(x, i) for i in range(k)])

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

def getPowersOfTwo(start, stop):
    return [2 ** x for x in range(start, stop)]

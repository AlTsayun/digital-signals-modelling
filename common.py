import math
from re import X

from matplotlib.pyplot import axes

def getHarmonicFunc(a, maxN, phi, f):
    return lambda n: a * math.sin(2 * math.pi * f * n / maxN + phi)

def getSawFunc(a, t, phi):
    def calculate(x, a, t, phi):
        try:
            t = float(t(x))
            phi = float(phi(x))
            a = float(a(x))
            param = x % t
            if (param != t):
                return param / t * a
            else:
                return (param  - t) / (t / 4) * a
        except:
            raise ValueError
    return lambda x, a=a, t=t, phi=phi: calculate(x, a, t, phi)

def getTriangleFunc(a, t, phi):
    def calculate(x, a, t, phi):
        try:
            t = float(t(x))
            phi = float(phi(x))
            a = float(a(x))
            param = (x - phi) % t
            if (param < t / 4):
                return param / (t / 4) * a
            elif (param < t * 3 / 4):
                return -(param - t / 2) / (t / 4) * a
            else:
                return (param  - t) / (t / 4) * a
        except:
            raise ValueError
    return lambda x, a=a, t=t, phi=phi: calculate(x, a, t, phi)

def getSampledFunc(func, sampleStep):
    def calculate(x):
        return func(x // sampleStep)
    return lambda x: calculate(x)

def sumFuncs(funcs):
    return lambda x: sum([func(x) for func in funcs])

def getTaylorHarmonicFunc(a, maxN, phi, f, k):
    func = getTaylorSinFunc(k)
    return lambda n: a(n) * func(2 * math.pi * f(n) * n / maxN + phi(n))

def getTaylorSinFunc(k):
    return getTaylorFunc(lambda x, i: ((-1) ** (i % 2)) * math.pow(x, 2 * i + 1) / math.factorial(2 * i + 1), k)

def getTaylorFunc(elementFunc, k):
    return lambda x: sum([elementFunc(x, i) for i in range(k)])

def parsePiExpression(str):
    try:
        return eval(str, {"pi": math.pi})
    except:
        raise ValueError

def parseMathExpression(str):
    def calculate(x, str):
        try:
            str = str.replace("^", "**")
            return float(eval(str, {"pi": math.pi, "sin": math.sin, "cos": math.cos, "x": x}))
        except:
            ValueError
    return lambda x, str=str: calculate(x, str)
        
def parseArray(str):
    return list(map(parseMathExpression, str.replace(" ", "").split(",")))

def parseNatural(str):
    try:
        value = int(str)
    except:
        raise ValueError
    if (value < 1):
        raise ValueError
    return value

def getPowersOfTwo(start, stop):
    return [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576][start: stop]

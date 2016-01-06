import random
import argparse


def add2(end, start=1, bitflag=False):
    if bitflag:
        x = random.randrange(start, end / 2)
        y = random.randrange(10 - x%10, end-x)
    else:
        x = random.randrange(start, end)
        y = random.randrange(start, end-x)
    return (x, "+", y)


def minus2(end, start=1, bitflag=False):
    if bitflag:
        x = random.randrange(10, end)
        y = random.randrange(x - 10, x)
    else:
        x = random.randrange(start+1, end)
        y = random.randrange(start, x)
    return (x, "-", y)


def format_exp(eles):
    fmt = "{0} {1} {2}"
    exp = fmt.format(eles[0], eles[1], eles[2])
    if len(exp) < 8:
        exp += " " * (8 - len(exp))
    return exp + "= ___"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    cols = 4
    rows = 10
    limits = 20
    count = cols * rows
    exps = []
    for i in xrange(count):
        exps.append(random.choice((add2, minus2))(limits))
    line = ""
    for i in xrange(len(exps)):
        line += format_exp(exps[i]) + "  "
        if i % cols == 3:
            print line
            line = ""
            

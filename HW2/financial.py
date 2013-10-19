#!/usr/bin/python

import scipy
import scipy.linalg
import pylab
import sys

# Fits a line y = ax + b to a signal
# Finds the minimum a, b of the objective
# sum_i w[i] * (signal[i] - (a*i + b))**2
def weighted_leastsq(signal, weights):
    w = scipy.sqrt(weights)
    X = scipy.array([[w[i]*i, w[i]] for i in xrange(len(signal))])
    a, b = scipy.linalg.lstsq(X, w*signal)[0]
    return a, b



if __name__ == '__main__':
    f = open('EUR-JPY.data')

    signal = [float(line) for line in f]
    weights = [1.0 for i in xrange(len(signal))]

    a, b = weighted_leastsq(signal, weights)

    x_axis = scipy.array(xrange(len(signal)))

    pylab.ion()
    pylab.figure()
    pylab.plot(signal, 'g')
    pylab.plot(a*x_axis + b, 'r')
    #pylab.savefig('EUR-JPY.png')
    pylab.ioff()

    raw_input('Press [enter] to continue')

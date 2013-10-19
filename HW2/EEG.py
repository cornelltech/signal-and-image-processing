#!/usr/bin/python

import scipy
import pylab
import sys

def graph(signal):
    pylab.ion()
    pylab.figure()
    pylab.plot(signal)
    pylab.ioff()

if __name__ == '__main__':
    freq = 200      # frequency of the sample points in Hz

    f = open('seizure1.data')
    seizure = [float(l) for l in f]
    # graph 3 seconds worth of the data
    graph(seizure[10*freq:13*freq])
    #pylab.savefig('seizure.png')

    f = open('normal2.data')
    normal = [float(l) for l in f]
    graph(normal[10*freq:13*freq])
    #pylab.savefig('normal.png')

    raw_input('Press [enter] to continue')

#!/usr/bin/env python3
import sys
import subprocess
import numpy as np
import PyGnuplot as gp

ctffindOutputTxt = sys.argv[1]
logfile = 'log.txt'
outputPlot = 'plot.png'

def parseCtffindOutput(outputTxt):
    try:
        with open(outputTxt) as f:
            lines = f.readlines()
    except Exception as e:
        print("Error parsing ctffind output file")
        print(e)
        sys.exit(1)
    # expected filename format: *_1234_ali.mrc
    filename = lines[1].split()[3]
    picNumber = int(filename.split('_')[-2])
    values = [float(x) for x in lines[5].split()][1:]
    # convert phase shift to degrees
    values[3] = float('%.6f' % (values[3] * 180/3.14))
    # convert defocus 1 and 2 to microns
    values[0] = float('%.6f' % (values[0] / 10000))
    values[1] = float('%.6f' % (values[1] / 10000))
    return tuple([picNumber] + values)

def readLog(log):
    try:
        data = np.genfromtxt(log, delimiter=' ')
        if len(data.shape) == 1: # 1d edge case
            data = np.array([data])
        return data
    except OSError: # empty log
        open(log, 'a').close()
        return np.array([[]])

def updateLog(log, outputTxt, debug=False):
    # read data and sort
    data = readLog(log).tolist()
    if data[0] == []: # handle empty log
        data.pop(0)
    data.append(parseCtffindOutput(outputTxt))
    data = [list(x) for x in set(tuple(x) for x in data)]
    data.sort(key=lambda x: x[0])
    # write back
    with open(log, 'w') as f:
        for picNumber, *values in data:
            f.write(' '.join((1+len(values)) * ['{}'])
                    .format(picNumber, *values) + '\n')
    if debug:
        subprocess.call("cat %s" % log, shell=True)
    return data

def plot(log, *columns, title='', ylabel=''):
    gp.c("set key off")
    if title:
        gp.c("set title '%s'" % title)
    if ylabel:
        gp.c("set ylabel '%s'" % ylabel)

    if len(columns) == 1:
        if title == 'Resolution of Fit, Å':
            gp.c("set yrange [0:20]")
        gp.c("plot '{}' u 1:{} w lp".format(log, columns[0]))
    elif len(columns) == 2:
        gp.c("plot '{0}' u 1:{1} w lp, '{0}' u 1:{2} w lp"
             .format(log, *columns))


if __name__ == "__main__":
    updateLog(logfile, ctffindOutputTxt)
    gp.c("set terminal pngcairo dashed enhanced size 1500, 1500")
    gp.c("set output '%s'" % outputPlot)
    gp.c("set multiplot layout 5,1")
    gp.c("set lmargin at screen 0.05")
    gp.c("set tmargin 2")
    plot(logfile, 2, 3, title='Defocus 1 and 2')
    plot(logfile, 4, title='Azimuth of Astigmatism')
    plot(logfile, 5, title='Phase Shift, Degrees')
    plot(logfile, 6, title='Cross Correlation')
    plot(logfile, 7, title='Resolution of Fit, Å')
    gp.c("unset multiplot")


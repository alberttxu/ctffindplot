#!/usr/bin/env python3
import sys
import numpy as np

ctffind_txt = sys.argv[1]
logfile = 'log.txt'
pngOut = 'plot.png'

def ctffindPhase():
    try:
        with open(ctffind_txt) as f:
            lines = f.readlines()
    except Exception as e:
        print("Error parsing ctffind output file")
        print(e)
        sys.exit(1)
    # filename expected format: *_1234_ali.mrc
    filename = lines[1].split()[3]
    picNumber = int(filename.split('_')[-2])
    phaseShiftRad = float(lines[5].split()[4])
    phaseShiftDeg = phaseShiftRad * 180 / 3.14
    return picNumber, float("%.2f" % phaseShiftDeg)

def readLog():
    try:
        data = np.genfromtxt(logfile, delimiter=' ')
        if len(data.shape) == 1: # 1d edge case
            data = np.array([data])
        return data
    except OSError: # empty log
        open(logfile, 'a').close()
        return np.array([[]])

def updateLog(debug=False):
    data = readLog().tolist()
    if data[0] == []:
        data.pop(0)
    data.append(ctffindPhase())
    data = [list(x) for x in set(tuple(x) for x in data)]
    data.sort(key=lambda x: x[0])

    with open(logfile, 'w') as f:
        for picNumber, phaseShift in data:
            f.write("%d %.2f\n" % (int(picNumber), phaseShift))
    if debug:
        import subprocess
        subprocess.call("cat %s" % logfile, shell=True)
    return data

def savePlot(pngOut):
    import PyGnuplot as gp
    gp.c("set terminal pngcairo")
    gp.c("set output '%s'" % pngOut)
    gp.c("set key off")
    gp.c("set xtics 1")
    gp.c("plot '%s' u 1:2 w lp" % logfile)

if __name__ == "__main__":
    savePlot(pngOut)

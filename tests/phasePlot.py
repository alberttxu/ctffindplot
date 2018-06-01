#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
import numpy as np

#ctffind_txt = "WL2121S-Ag2_1378_output.txt"
logfile = 'log.txt'
#logfile = 'log2.txt'
#logfile = 'asdf.txt'

ctffind_txt = sys.argv[1]
#logfile = sys.argv[2] # space separated csv
pngOut = "plot.png"

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
    #print(picNumber, float("%.2f" % phaseShiftDeg))
    return picNumber, float("%.2f" % phaseShiftDeg)

#print(ctffindPhase())

def readLog():
    try:
        data = np.genfromtxt(logfile, delimiter=' ')
        if len(data.shape) == 1: # 1d edge case
            data = np.array([data])
        return data
    except OSError: # empty log
        open(logfile, 'a').close()
        return np.array()

#print(readLog())

def updateLog(debug=False):
    data = readLog().tolist()
    if data[0] == []:
        data.pop(0)
    data.append(ctffindPhase())
    data = [list(x) for x in set(tuple(x) for x in data)]
    data.sort(key=lambda x: x[0])
    #print(data)
    with open(logfile, 'w') as f:
        for picNumber, phaseShift in data:
            f.write("%d %.2f\n" % (int(picNumber), phaseShift))
    if debug:
        import subprocess
        subprocess.call("cat %s" % logfile, shell=True)
    return data

#updateLog()

def savePlot(pngOut):
    data = np.array(updateLog()).T
    plt.plot(*data)
    plt.savefig(pngOut)

if __name__ == "__main__":
    savePlot(pngOut)

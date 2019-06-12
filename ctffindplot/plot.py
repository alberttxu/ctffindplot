import PyGnuplot as gp


def parseCtffindOutput(outputTxt):
    with open(outputTxt) as f:
        lines = f.readlines()
    # expected filename format: *_1234_ali.mrc
    filename = lines[1].split()[3]
    picNumber = int(filename.split('_')[-2])
    values = [float(x) for x in lines[5].split()][1:]
    # convert phase shift to degrees
    values[3] = float('%.6f' % (values[3] * 180/3.14))
    # convert defocus 1 and 2 to microns
    values[0] = float('%.6f' % (values[0] / 10000))
    values[1] = float('%.6f' % (values[1] / 10000))
    # calculate size of difference between defocus values
    values.insert(2, float('%.6f' % (abs(values[0]-values[1]) * 1000)))
    return tuple([picNumber] + values)

def updateLog(log, outputTxt):
    # read data and sort
    newLine = ' '.join(str(x) for x in parseCtffindOutput(outputTxt))
    with open(log, 'a') as f:
        f.write(newLine + '\n')

def subplot(log, *columns, title='', ylabel=''):
    gp.c("set key off")
    if title:
        gp.c("set title '%s'" % title)
    if ylabel:
        gp.c("set ylabel '%s'" % ylabel)

    if len(columns) == 1:
        if columns[0] == 8:
            gp.c("plot [ ] [0:10] '{}' u 1:{} w lp".format(log, columns[0]))
        else:
            gp.c("plot '{}' u 1:{} w lp".format(log, columns[0]))
    elif len(columns) == 2:
        gp.c("plot '{0}' u 1:{1} w lp, '{0}' u 1:{2} w lp"
             .format(log, *columns))

def plot_ctffind_output(log, ctffindOutputTxt, outputPlot):
    updateLog(log, ctffindOutputTxt)
    gp.c("set terminal pngcairo dashed enhanced size 1500, 1500")
    gp.c("set output '%s'" % outputPlot)
    gp.c("set multiplot layout 6,1")
    gp.c("set lmargin at screen 0.05")
    gp.c("set tmargin 2")
    subplot(log, 2, 3, title='Defocus 1 and 2')
    subplot(log, 4, title='abs(defocus1 - defocus2), nm')
    subplot(log, 5, title='Azimuth of Astigmatism')
    subplot(log, 6, title='Phase Shift, Degrees')
    subplot(log, 7, title='Cross Correlation')
    subplot(log, 8, title='Resolution of Fit, A')
    gp.c("unset multiplot")


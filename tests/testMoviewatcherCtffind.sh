#!/bin/sh
TESTDIR="$(cd "$(dirname "$0")"; pwd -P)"
cd $TESTDIR
mv done/*_ali.mrc . 2>/dev/null
../ctffindPlot

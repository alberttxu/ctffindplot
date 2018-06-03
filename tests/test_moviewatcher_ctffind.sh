#!/bin/sh
TESTDIR="$(cd "$(dirname "$0")"; pwd -P)"
cd $TESTDIR
mv done/*_ali.mrc .
../phasePlot

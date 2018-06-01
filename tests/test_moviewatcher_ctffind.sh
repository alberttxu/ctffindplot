#!/bin/sh
TESTDIR="$(cd "$(dirname "$0")"; pwd -P)"
mv $TESTDIR/done/*_ali.mrc .
$TESTDIR/../phasePlot

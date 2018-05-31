#!/bin/sh
TESTDIR=$(dirname "$0")
echo "resetting test: rm $TESTDIR/done/*_output*; mv $TESTDIR/done/*.mrc ."
rm $TESTDIR/done/*_output*
mv $TESTDIR/done/*.mrc .
$TESTDIR/../lib/moviewatcher/moviewatcher -d $TESTDIR/done -c $TESTDIR/ctffindoptions -ext .mrc

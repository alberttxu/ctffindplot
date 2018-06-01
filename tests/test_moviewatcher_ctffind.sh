#!/bin/sh
TESTDIR=$(dirname "$0")
#echo "resetting test: rm $TESTDIR/*_output*; mv $TESTDIR/done/*.mrc ."
#rm $TESTDIR/*_output*
#mv $TESTDIR/done/*_ali.mrc .
#$TESTDIR/../lib/moviewatcher/moviewatcher \
    #-d $TESTDIR/done \
    #-ext _ali.mrc \
    #-c $TESTDIR/ctffindoptions

cd $TESTDIR
echo "resetting test: rm _output*; mv done/*.mrc ."
rm _output*
mv done/*_ali.mrc .
../lib/moviewatcher/moviewatcher \
    -d done \
    -ext _ali.mrc \
    -c ctffindoptions

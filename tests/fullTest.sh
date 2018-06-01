#!/bin/sh
TESTDIR="$(cd "$(dirname "$0")"; pwd -P)"
cd $TESTDIR
./downloadTestFiles.sh
./test_moviewatcher_ctffind.sh

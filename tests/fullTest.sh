#!/bin/sh
TESTDIR=$(dirname "$0")
$TESTDIR/downloadTestFiles.sh
$TESTDIR/test_moviewatcher_ctffind.sh

#!/bin/sh
curl http://grigoriefflab.janelia.org/sites/default/files/ctffind-4.1.10.tar.gz | tar xz
cd ctffind-4.1.10
./configure --with-wx-config=wx-config-3.0 && make && make install


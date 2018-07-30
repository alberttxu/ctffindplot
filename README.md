# ctffindPlot

ctffindPlot generates png graphs of the results from ctffind. It watches the current working directory for aligned mrc files of the format ...\_(picture#)\_ali.mrc. It runs them through ctffind using parameters from the ctffindoptions.txt file, updates a plot.png graph and a log.txt file, then moves the mrc file into a created "done" folder. It can also process a single mrc manually as an argument.

## Installation

### Cygwin
1. Installing Cygwin with required dependencies
- Download the Cygwin [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe)
- Download this repository's [cygwin_install_script.bat](https://cdn.rawgit.com/alberttxu/ctffindPlot/d9ec4e9f/cygwin_install_scripts/cygwinInstallScript.bat)
  into the same folder.
- Double click the cygwinInstallScript.bat to start the installer. Continue clicking next until the installation is finished.
  > If you are on Windows 10 and get a popup error: "This app can't run on your PC. To find a version for your PC, check with the software publisher", this is a security warning. You can go into Settings > Updates and Security > For developers, and under Use developer features, select Sideload apps.

2. Installing Python dependencies and ctffind4
- Open Cygwin terminal
- `bash -c "git clone --recursive https://github.com/alberttxu/ctffindPlot /usr/local/ctffindPlot; cd /usr/local/ctffindPlot; python3 -m pip install -r requirements.txt; cygwin_install_scripts/cygwinInstallCtffind4.sh; echo 'export PATH=/usr/local/ctffindPlot/bin:$PATH' >> ~/.bashrc; source ~/.bashrc"`

3. Test installation
- `cd /usr/local/ctffindPlot/tests`
- `./fullTest.sh`
  > This downloads several aligned mrc example files, feeds them into ctffind4, and updates a plot.png graph of the ctffind results. The filename format is ...\_(picture #)\_ali.mrc

### Linux (Centos 7)
1. `sudo bash -c 'yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm; curl http://grigoriefflab.janelia.org/sites/default/files/ctffind-4.1.10-linux64.tar.gz | tar xvz -C /usr/local/; yum install -y git gnuplot python36 python36-setuptools; easy_install-3.6 pip; ln -s /usr/bin/python36 /usr/bin/python3; git clone --recursive https://github.com/alberttxu/ctffindPlot.git /usr/local/ctffindPlot'; cd /usr/local/ctffindPlot; python3 -m pip install --user -r requirements.txt; echo 'export PATH=$PATH:/usr/local/ctffindPlot/bin' >> ~/.bashrc; source ~/.bashrc`

2. Test (this clones another copy of the repository to home because of file permissions in /usr/local. You can remove this folder afterwards.
`cd ~; git clone --recursive https://github.com/alberttxu/ctffindPlot.git; cd ctffindPlot/tests; ./fullTest.sh`

## Usage

First, have a ctffindoptions.txt file in the current working directory.

ctffindPlot can either watch a directory for new \_ali.mrc files or can process a single image as an argument.
- To watch a directory just type `ctffindPlot`
  > Note: If multiple files are already present, they will be processed in ascending order.
- For a single image, type `ctffindPlot (filename)`



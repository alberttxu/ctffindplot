# ctffindPlot

ctffindPlot generates and updates graphs of the results from ctffind. It watches the current working directory for new aligned micrographs of the format \_(picture#)\_ali.mrc, runs them through ctffind using a ctffindoptions.txt file, then moves the mrc file into the "done" folder, and updates a plot.png graph.

## Installation

1. Installing Cygwin with required dependencies
- Download the Cygwin [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe)
- Download this repository's [cygwin_install_script.bat](https://cdn.rawgit.com/alberttxu/ctffindPlot/d9ec4e9f/cygwin_install_scripts/cygwinInstallScript.bat)
  into the same folder.
- Double click the cygwinInstallScript.bat to start the installer. Continue clicking next until the installation is finished.
  > If you are on Windows 10 and get a popup error: "This app can't run on your PC. To find a version for your PC, check with the software publisher", this is a security warning. You can go into Settings > Updates and Security > For developers, and under Use developer features, select Sideload apps.

2. Installing Python dependencies and ctffind4
- Open Cygwin terminal
- `bash -c "git clone --recursive https://github.com/alberttxu/ctffindPlot /usr/local/ctffindPlot; cd /usr/local/ctffindPlot; python3 -m pip install requirements.txt; cygwin_install_scripts/cygwinInstallCtffind4.sh; echo 'export PATH=/usr/local/ctffindPlot/bin:$PATH' >> ~/.bashrc; source ~/.bashrc"`

3. Test installation
- `cd /usr/local/ctffindPlot/tests`
- `./fullTest.sh`
  > This downloads several aligned mrc example files, feeds them into ctffind4, and updates a plot.png graph of the ctffind results. The filename format is ..._(picture #)_ali.mrc

## Usage
- have a ctffindoption.txt file in the current directory
- `ctffindPlot`

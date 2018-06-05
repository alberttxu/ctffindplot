# PhasePlot

## Installation

1. Installing Cygwin with required dependencies
- Download the Cygwin [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe)
- Download this repository's [cygwin_install_script.bat](https://cdn.rawgit.com/alberttxu/PhasePlot/9d844f56/tools/cygwin_install_script.bat)
  into the same folder.
- Double click the cygwin_install_script.bat to start the installer. Continue clicking next until the installation is finished.
  > If you get a windows popup error: "This app can't run on your PC. To find a version for your PC, check with the software publisher", this is a security warning. On Windows 10 you can go into Settings > Updates and Security > For developers, and under Use developer features, select Sideload apps.

2. Installing Python dependencies and ctffind4
- Open Cygwin terminal
- `git clone --recursive https://github.com/alberttxu/PhasePlot /usr/local/PhasePlot`
- `cd /usr/local/PhasePlot`
- `python3 -m pip install requirements.txt`
- `tools/installCtffind4.sh`
- Add phasePlot to path: `echo 'export PATH=/usr/local/PhasePlot:$PATH' >> ~/.bashrc; source ~/.bashrc`

3. Test installation
- `cd tests`
- `./fullTest.sh`
  > This downloads several aligned mrc example files, feeds them into ctffind4, and updates a plot.png graph of the phase shift. The filename format is ..._(picture #)_ali.mrc

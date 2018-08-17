# ctffindPlot

ctffindPlot generates png graphs of the results from ctffind. It watches the current working directory for aligned mrc files of the format `*_(picture#)_ali.mrc`. It runs them through ctffind using a parameters file, updates a png graph and a log file, then moves the mrc file into a finished folder. It can also process a single mrc manually as an argument.

## Installation

### Cygwin
1. Installing Cygwin with required dependencies
- Download the Cygwin [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe)
- Download this repository's [cygwin_install_script.bat](https://cdn.rawgit.com/alberttxu/ctffindPlot/d9ec4e9f/cygwin_install_scripts/cygwinInstallScript.bat)
  into the same folder.
- Double click the cygwinInstallScript.bat to start the installer. Continue clicking next until the installation is finished.
  > If you are on Windows 10 and get a popup error: "This app can't run on your PC. To find a version for your PC, check with the software publisher", this is a security warning. You can go into Settings > Updates and Security > For developers, and under Use developer features, select Sideload apps.

2. Installing dependencies and ctffind4
- Open Cygwin terminal
- Download this repository and install dependencies
	- `git clone --recursive https://github.com/alberttxu/ctffindPlot /usr/local/ctffindPlot; cd /usr/local/ctffindPlot; python3 -m pip install -r requirements.txt;`
- Install ctffind
    - `cd /usr/local/ctffindPlot; cygwin_install_scripts/cygwinInstallCtffind4.sh;`
- Add to ctffindPlot to PATH
	- `echo 'export PATH=/usr/local/ctffindPlot/bin:$PATH' >> ~/.bashrc; source ~/.bashrc`

3. TLDR
`bash -c "git clone --recursive https://github.com/alberttxu/ctffindPlot /usr/local/ctffindPlot; cd /usr/local/ctffindPlot; python3 -m pip install -r requirements.txt; cygwin_install_scripts/cygwinInstallCtffind4.sh; echo 'export PATH=/usr/local/ctffindPlot/bin:$PATH' >> ~/.bashrc; source ~/.bashrc"`

3. Test installation
- `cd /usr/local/ctffindPlot/tests`
- `./fullTest.sh`
  > This downloads 4 example aligned mrc files, and runs ctffindPlot in watching mode using default values.

### Linux (Centos 7)
1. Installing ctffind and python3 and dependencies
- ctffind
	- `sudo bash -c "curl http://grigoriefflab.janelia.org/sites/default/files/ctffind-4.1.10-linux64.tar.gz | tar xvz -C /usr/local/"`
- python3
	> On Centos python3 is named with a subversion (i.e. python34, python3.4, python36, python3.6, etc). You will need to point to it with a symlink named python3.
	 - `sudo bash -c "yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm; yum install -y git gnuplot python36 python36-setuptools; easy_install-3.6 pip; ln -s /usr/bin/python36 /usr/bin/python3"`
- Download this repository and install dependencies
	- `sudo bash -c "git clone --recursive https://github.com/alberttxu/ctffindPlot.git /usr/local/ctffindPlot"; cd /usr/local/ctffindPlot; python3 -m pip install --user -r requirements.txt`
- Add to ctffindPlot to PATH
- `echo 'export PATH=$PATH:/usr/local/ctffindPlot/bin' >> ~/.bashrc; source ~/.bashrc`

2. TLDR
`sudo bash -c 'yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm; curl http://grigoriefflab.janelia.org/sites/default/files/ctffind-4.1.10-linux64.tar.gz | tar xvz -C /usr/local/; yum install -y git gnuplot python36 python36-setuptools; easy_install-3.6 pip; ln -s /usr/bin/python36 /usr/bin/python3; git clone --recursive https://github.com/alberttxu/ctffindPlot.git /usr/local/ctffindPlot'; cd /usr/local/ctffindPlot; python3 -m pip install --user -r requirements.txt; echo 'export PATH=$PATH:/usr/local/ctffindPlot/bin' >> ~/.bashrc; source ~/.bashrc`

5. Test (this clones another copy of the repository to home because of file permissions in /usr/local. You can remove this folder afterwards.
`cd ~; git clone --recursive https://github.com/alberttxu/ctffindPlot.git; cd ctffindPlot/tests; ./fullTest.sh`

## Usage
```
ctffindPlot [-h]
              Print shortened usage prompt.
            [-o output_png]
              Name of output png graph. (default = ctf_plot.png)
            [-p aligned_mrc_dir]
              (only applies to watching mode)
              Directory that processed files get moved to. (default = alignedMRC)
            [-t ctffind_params_file]
              Name of the parameters file for ctffind. (default = ctffindoptions.txt)
            [-c ctf_fits_dir]
              Directory to place ctffind's fitted mrcs. (default = ctf_fits)
            [-l logfile]
              Name of the log file used by this program to record data. (default = ctf_log.txt)
              This file is a space separated csv.
            [aligned_mrc]
              (only applies to processing a single file)
              Name of the aligned mrc file to be processed.
              This file is not moved into the aligned mrc directory.
```

First, have a ctffindoptions.txt file in the current working directory, or use the -t flag to specify a filename.

ctffindPlot can either watch a directory for new \_ali.mrc files or can process a single image as an argument.
- To watch a directory just type `ctffindPlot` without specifying an mrc file.
  > If multiple files are already present, they will be processed in ascending order.
- For a single image, type `ctffindPlot (filename)`
  > Using the p flag does not apply for single images. (I.e., the file will not be moved to the processed directory.)

### Using with framewatcher
If you are using framewatcher from the IMOD suite to do alignments, ctffindPlot can be run using the after flag. `framewatcher -pr processedTiffs -after 'ctffindPlot %{outputFile}’`


## Dependencies
- python3
- ctffind4
- gnuplot
  > If you are running Centos 6, the default yum repositories have outdated versions of gnuplot (required) and curl (optional, version with -j flag is needed to run the fullTest script), so you will have to manually install them.


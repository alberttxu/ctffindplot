
# ctffindplot

ctffindplot generates a real-time graph of the summary results of ctffind4. It watches the current directory for files ending in `ali.mrc`, runs ctffind using a parameters file, creates a png, then moves the original mrc file into a different folder.

## Requires
- ctffind4
- python3
- gnuplot
- curl (for installing ctffind4)

## Installation

### Linux

1. Install ctffind4 if not already installed

`sudo sh -c 'curl http://grigoriefflab.janelia.org/sites/default/files/ctffind-4.1.13-linux64.tar.gz | tar xvz -C /usr/local/'`

2. Install ctffindplot

Ubuntu

`sudo apt update && sudo apt install -y curl gnuplot python3-pip && sudo python3 -m pip install ctffindplot`

Centos

`sudo yum install -y --enablerepo=extras epel-release && sudo yum install -y python36-pip gnuplot curl && sudo python36 -m pip install ctffindplot`

### Windows (Cygwin)

1. Install Cygwin with required packages
- Download the Cygwin [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe) installer
- Download this repository's [cygwin_install_script.bat](https://raw.githack.com/alberttxu/ctffindplot/master/cygwin_install_scripts/cygwinInstallScript.bat)
  into the same folder.
- Double click the cygwinInstallScript.bat to start the installer. Continue clicking next until the installation is finished.

2. Install ctffind4
- Open Cygwin terminal
- `curl http://grigoriefflab.janelia.org/sites/default/files/ctffind-4.1.10.tar.gz | tar xz && cd ctffind-4.1.10 && ./configure --with-wx-config=wx-config-3.0 && make && make install`

3. Install ctffindplot
- `python3 -m pip install ctffindplot`


## Usage
```
usage: ctffindplot [-h] [-o OUTPUT] [-p ALIGNED_MRC_DIR]
                   [-t CTFFIND_PARAMS_FILE] [-c CTF_FITS_DIR] [-l LOGFILE]

plot summary results from ctffind

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output png file (default = ctffindplot_plot.png)
  -p ALIGNED_MRC_DIR, --aligned_mrc_dir ALIGNED_MRC_DIR
                        destination for processed mrc files (default =
                        alignedMRC)
  -t CTFFIND_PARAMS_FILE, --ctffind_params_file CTFFIND_PARAMS_FILE
                        ctffind parameters file (default = ctffindoptions.txt)
  -c CTF_FITS_DIR, --ctf_fits_dir CTF_FITS_DIR
                        destination for ctffind diagnostic images (default =
                        ctffind_fits)
  -l LOGFILE, --logfile LOGFILE
                        data file for plotting (default = ctffindplot_log.txt)
```

First, have a ctffindoptions.txt file in the current working directory, or use the -t flag to specify a filename.
Next, type `ctffindplot` and ...ali.mrc files will be fed through ctffind and a png graph will be created and continuously updated.
> The last `ali.mrc` file in sorted alphabetical order will not be processed since it may be in use by other real-time programs like IMOD's framewatcher.

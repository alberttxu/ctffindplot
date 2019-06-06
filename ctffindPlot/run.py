import os
import shutil
import subprocess

def ctffind(alimrc, params_file):
    with open(params_file) as f:
        ctffind_command = f.read()
    before_ali = alimrc[:alimrc.rfind('_ali.mrc')]
    ctffind_command.replace('(filename)', alimrc)
    ctffind_command.replace('(basename)', before_ali)
    subprocess(ctffind_command, shell=True)

def cleanup(alimrc, ali_done_dir, ctf_fits_dir):
    before_ali = alimrc[:alimrc.rfind('_ali.mrc')]
    os.remove(before_ali + '_ali_output.txt')
    os.remove(before_ali + '_ali_output_avrot.txt')
    shutil.move(before_ali + '_ali_output.mrc', ctf_fits_dir)
    shutil.move(alimrc, ali_done_dir)


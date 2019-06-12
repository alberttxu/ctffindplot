import os
import shutil
import subprocess

def ctffind(alimrc, params_file):
    with open(params_file) as f:
        ctffind_command = f.read()
    before_ali = alimrc[:alimrc.rfind('_ali.mrc')]
    ctffind_command = ctffind_command.replace('(filename)', alimrc)
    ctffind_command = ctffind_command.replace('(basename)', before_ali)
    subprocess.run(ctffind_command, shell=True)

def cleanup(alimrc, ali_done_dir, ctf_fits_dir):
    before_ali = alimrc[:alimrc.rfind('_ali.mrc')]
    os.remove(before_ali + '_ali_output.txt')
    os.remove(before_ali + '_ali_output_avrot.txt')
    ctf_fit = before_ali + '_ali_output.mrc'
    shutil.move(ctf_fit, os.path.join(ctf_fits_dir, ctf_fit))
    shutil.move(alimrc, os.path.join(ali_done_dir, alimrc))


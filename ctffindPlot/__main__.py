def main():
    import argparse
    import os
    import os.path
    import shutil
    from plot import plot_ctffind_output
    from run import ctffind
    from watch import isReady

    if shutil.which('ctffind') == None:
        print("can't find ctffind")
        exit()
    if shutil.which('gnuplot') == None:
        print("can't find gnuplot")
        exit()

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-o', '--output', default='ctffind_plot.png')
    parser.add_argument('-p', '--aligned_mrc_dir', default='alignedMRC')
    parser.add_argument('-t', '--ctffind_params_file', default='ctffindoptions.txt')
    parser.add_argument('-c', '--ctf_fits_dir', default='ctffind_fits')
    parser.add_argument('-l', '--logfile', default='ctffindPlot_log.txt')
    args.parser.parse_args()

    if not os.path.isfile(args.ctffind_params_file):
        print("%s not found" % args.ctffind_params_file)
        exit()

    if not os.path.isdir(args.ctf_fits_dir):
        print("creating %s" % args.ctf_fits_dir)
        os.mkdir(args.ctf_fits_dir)

    while True:
        aliMrcFiles= sorted(f for f in os.listdir(".") if f.endswith("ali.mrc"))
        for f in aliMrcFiles:
            if isReady(f):
                ctffind(f, args.ctffind_params_file)
                root, ext = os.path.splitext(f)
                ctffindOutputTxt = root + '_output.txt'
                plot_ctffind_output(args.logfile, ctffindOutputTxt, args.output)
                cleanup(f, args.aligned_mrc_dir, args.ctf_fits_dir)


if __name__ == '__main__':
    main()

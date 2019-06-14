def main():
    import argparse
    import os
    import os.path
    import shutil
    import time
    from ctffindplot.plot import plot_ctffind_output
    from ctffindplot.run import ctffind, cleanup
    from ctffindplot.watch import isReady

    parser = argparse.ArgumentParser(description="plot summary results from ctffind")
    parser.add_argument(
        "-o",
        "--output",
        help="output png file (default = ctffindplot_plot.png)",
        default="ctffindplot_plot.png",
    )
    parser.add_argument(
        "-p",
        "--aligned_mrc_dir",
        help="destination for processed mrc files (default = alignedMRC)",
        default="alignedMRC",
    )
    parser.add_argument(
        "-t",
        "--ctffind_params_file",
        help="ctffind parameters file (default = ctffindoptions.txt)",
        default="ctffindoptions.txt",
    )
    parser.add_argument(
        "-c",
        "--ctf_fits_dir",
        help="destination for ctffind diagnostic images (default = ctffind_fits)",
        default="ctffind_fits",
    )
    parser.add_argument(
        "-l",
        "--logfile",
        help="data file for plotting (default = ctffindplot_log.txt)",
        default="ctffindplot_log.txt",
    )

    args = parser.parse_args()

    output = os.path.abspath(args.output)
    aligned_dir = os.path.abspath(args.aligned_mrc_dir)
    params_file = os.path.abspath(args.ctffind_params_file)
    ctf_fits_dir = os.path.abspath(args.ctf_fits_dir)
    logfile = os.path.abspath(args.logfile)

    # error checking
    if shutil.which("ctffind") == None:
        print("can't find ctffind")
        exit()
    if shutil.which("gnuplot") == None:
        print("can't find gnuplot")
        exit()

    if os.path.isdir(output):
        print("invalid output file: %s is a directory" % output)
        exit()

    if os.path.isfile(aligned_dir):
        print("invalid aligned_mrc_dir: %s is not a directory" % aligned_dir)
        exit()

    if os.path.isfile(ctf_fits_dir):
        print("invalid ctf_fits_dir: %s is not a directory" % ctf_fits_dir)
        exit()

    if os.path.isdir(params_file):
        print("invalid ctffind_params_file: %s is a directory" % params_file)
        exit()
    elif not os.path.isfile(params_file):
        print("invalid ctffind_params_file: %s not found" % params_file)
        exit()

    if os.path.isdir(logfile):
        print("invalid logfile: %s is a directory" % logfile)
        exit()

    # create directories if not existing
    if not os.path.isdir(ctf_fits_dir):
        print("creating %s" % ctf_fits_dir)
        os.mkdir(ctf_fits_dir)

    if not os.path.isdir(aligned_dir):
        print("creating %s" % aligned_dir)
        os.mkdir(aligned_dir)

    while True:
        try:
            aliMrcFiles = sorted(f for f in os.listdir(".") if f.endswith("ali.mrc"))
            aliMrcFiles.pop()
            for f in aliMrcFiles:
                if isReady(f):
                    start = time.time()
                    ctffind(f, params_file)
                    root, ext = os.path.splitext(f)
                    ctffindOutputTxt = root + "_output.txt"
                    plot_ctffind_output(logfile, ctffindOutputTxt, output)
                    cleanup(f, aligned_dir, ctf_fits_dir)
                    end = time.time()
                    print("processed in %.2f sec" % (end - start))
        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    main()

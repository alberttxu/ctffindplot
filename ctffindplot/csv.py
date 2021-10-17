def read_csv(logfile):
    result = {}
    lines = []
    with open(logfile) as f:
        for line in f.readlines():
            l_clean = [float(x) for x in line.strip().split()]
            lines.append(l_clean)
    column_data = zip(*lines)
    labels = [
        "index",
        "defocus1",
        "defocus2",
        "astig",
        "azimuth_astig",
        "phase_shift",
        "xcorr",
        "res_fit",
    ]
    for label, series in zip(labels, column_data):
        result[label] = series
    return result

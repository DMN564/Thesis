from numpy.typing import NDArray

import numpy as np

type Histogram = tuple[
    NDArray,  # xpoints
    NDArray,  # xedges
    NDArray,  # yvals
    NDArray,  # xerrs
    NDArray   # yerrs
]

def get_histograms(filepath: str) -> tuple[Histogram, ...] | None:
    namespace: dict = {}

    with open(f"{filepath}__data.py") as f:
        source: str = f.read()

    exec(source, namespace)

    try:
        handles: tuple[str] = namespace["add_legend_handle"]
    except KeyError:
        print(f"add_legend_handle not defined! You need to use a '{filepath}__data.py' file!")
        return None

    histograms: list[Histogram] = []

    for handle in handles:
        try:
            x_points = np.array(namespace["xpoints"][handle], dtype=np.float64)
            x_edges  = np.array(namespace["xedges"][handle], dtype=np.float64)
            y_values = np.array(namespace["yvals"][handle], dtype=np.float64)
            x_err    = np.array(namespace["xerrs"][handle], dtype=np.float64)
            y_err    = np.array(namespace["yerrs"][handle], dtype=np.float64)
        except KeyError:
            print(f"There is a missing property (one of 'xpoints', 'xedges', 'yvals', 'xerrs', 'yerrs') for {handle}!")
            return None

        num_bins = len(y_values)
        if num_bins != len(x_points):
            print("Mismatch between number of buckets and values!!")
            return None
        if num_bins != len(x_edges) - 1:
            print("Mismatch between number of buckets and edges!!")
            return None

        if len(x_err) != 2 or not np.array_equal(x_err[0], x_err[1]):
            print("No idea what is going on but something is different with the errors for x. Check the files,"
                  "you can likely ignore this warning. I will still bail out here though. Ask Niklas.")
            return None
        x_err = x_err[0]

        if len(y_err) != 2 or not np.array_equal(y_err[0], y_err[1]):
            print("No idea what is going on but something is different with the errors for y. Check the files,"
                  "you can likely ignore this warning. I will still bail out here though. Ask Niklas.")
            return None
        y_err = y_err[0]

        histograms.append((x_points, x_edges, y_values, x_err, y_err))

    return tuple(histograms)


if __name__ == "__main__":
    x_points, _, y_values, x_err, y_err = get_histograms("data/In_Plane_Low_Q2")[0]
    #print(x_points)
    #print(x_edges)
    print(y_values)
    #print(x_err)
    #print(y_err)

    print("---")

    x_points, x_edges, y_values, x_err, y_err = get_histograms("data/Out_Plane_Low_Q2")[0]
    #print(x_points)
    #print(x_edges)
    print(y_values)
    #print(x_err)
    #print(y_err)

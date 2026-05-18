import numpy as np

import matplotlib.pyplot as plt


_FMT = lambda f: np.format_float_positional(f, precision=6, trim="-")

_ID, _Q2, _PSI, _EPS2, _PHI2 = np.loadtxt(
    "txt_files/final_events.txt",
    dtype=float
).T


def main():
    print(_Q2.min())
    print(_Q2.max())

    q2_20, q2_80 = np.percentile(_Q2, (20, 80))
    #eps2_20, eps2_80 = np.percentile(_EPS2, (20, 80))

    print(f"20th percentile q2 value: {_FMT(q2_20)}")
    print(f"80th percentile a2 value: {_FMT(q2_80)}")

    h, b = np.histogram(
        _Q2,
        bins=50,
        range=(0, 7),
    )
    # strip trailing zeros
    last = np.nonzero(h != 0)[0][-1]

    print(b[last + 2])

    x = b[:last + 2]

    with open("hist.dat", "w") as fd:
        print(
            *(f"{_FMT(x_i)},{_FMT(h_i)}" for x_i, h_i in zip(x, h)),
            sep="\n",
            file=fd,
        )

    return

    plt.hist(
        _EPS2,
        bins=40,
        alpha=0.6,
        label="Eccentricity distribution"
    )

    plt.axvspan(
        _EPS2.min(),
        eps2_20,
        alpha=0.3,
        label=rf"Bottom 20% ($\epsilon$ < {eps2_20:.3f})"
    )
    plt.axvspan(
        eps2_80,
        _EPS2.max(),
        alpha=0.3,
        label=rf"Top 20% ($\epsilon$ > {eps2_80:.3f})"
    )

    plt.axvline(
        eps2_20,
        linestyle="--",
        linewidth=2,
        label="20th percentile"
    )
    plt.axvline(
        eps2_80,
        linestyle="--",
        linewidth=2,
        label="80th percentile"
    )

    plt.xlabel(r"$\epsilon$")
    plt.ylabel("Counts")
    plt.title(r"Eccentricity Distribution with Event Shape Percentiles")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()

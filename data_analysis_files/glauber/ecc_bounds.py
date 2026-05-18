from data import ecc__data

import numpy as np
import matplotlib.pyplot as plt


_ID, = ecc__data.add_legend_handle

_X_DATA = np.asarray(ecc__data.xpoints[_ID], dtype=float)
_Y_DATA = np.asarray(ecc__data.yvals[_ID], dtype=float)

#assert len(_X_DATA) == len(_Y_DATA)

_EVENT_COUNT = len(_X_DATA)  # 1000

_X_ERR = np.asarray(ecc__data.xerrs[_ID][0], dtype=float)
#_Y_ERR = np.asarray(ecc__data.yerrs[_ID][0], dtype=float)

#assert len(_X_ERR) == len(_Y_ERR) == _EVENT_COUNT

_X_LEFT  = _X_DATA - _X_ERR
_X_RIGHT = _X_DATA + _X_ERR

_WIDTH = 2 * _X_ERR  # 0.002

_REBIN = 10


def main():
    cdf = np.cumsum(_Y_DATA * _WIDTH)
    cdf /= cdf[-1]

    q20, q80 = np.interp((.2, .8), cdf, _X_RIGHT)

    h = _Y_DATA * _EVENT_COUNT

    last = np.nonzero(h != 0)[0][-1]

    x_min = _X_LEFT[0]
    x_max = _X_RIGHT[last]

    h = h[:last + 1]
    x = _X_LEFT[:last + 1]

    h = np.add.reduceat(
        h,
        np.arange(0, len(h), _REBIN)
    )
    x = x[::_REBIN]

    fmt = lambda f: np.format_float_positional(f, precision=6, trim="-")

    with open("hist.dat", "w") as fd:
        print(
            f"# xmin,xmax = ({fmt(x_min)},{fmt(x_max)})",
            f"# ymin,ymax = ({fmt(h.min())},{fmt(h.max())})",
            f"# <20%, >80% = ({fmt(q20)},{fmt(q80)})",
            "x,h",
            *(f"{fmt(xi)},{fmt(hi)}" for xi, hi in zip(x, h)),
            f"{fmt(x_max)},0",
            sep="\n",
            file=fd,
        )

    return

    plt.bar(
        x,
        h,
        width=_WIDTH,
        alpha=0.8,
    )

    plt.axvspan(
        x_min,
        q20,
        alpha=0.3,
        label=rf"Bottom 20% ($\epsilon < {q20:.3f}$)",
    )
    plt.axvspan(
        q80,
        x_max,
        alpha=0.3,
        label=rf"Top 20% ($\epsilon > {q80:.3f}$)",
    )

    plt.axvline(
        q20,
        linestyle="--",
        linewidth=2,
        label=f"20%: {q20:.3f}",
    )
    plt.axvline(
        q80,
        linestyle="--",
        linewidth=2,
        label=f"80%: {q80:.3f}",
    )

    plt.title("Eccentricity Distribution with Event Shape Percentiles")
    plt.xlabel(r"Eccentricity $\epsilon$")
    plt.ylabel("Counts")
    plt.xlim((x_min, x_max))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

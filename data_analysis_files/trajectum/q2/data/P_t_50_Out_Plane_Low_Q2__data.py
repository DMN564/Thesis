
import numpy as np
from numpy import nan, inf

add_legend_handle = [
  'rivet_hydro_merged.yoda'
]

xpoints = {
    'rivet_hydro_merged.yoda' : [5.350000e+01, 6.050000e+01, 6.750000e+01, 7.450000e+01, 8.150000e+01,
                                 8.850000e+01, 9.550000e+01, 1.025000e+02, 1.095000e+02, 1.165000e+02],
}

xedges = {
    'rivet_hydro_merged.yoda' : [5.000000e+01, 5.700000e+01, 6.400000e+01, 7.100000e+01, 7.800000e+01,
                                 8.500000e+01, 9.200000e+01, 9.900000e+01, 1.060000e+02, 1.130000e+02,
                                 1.200000e+02],
}

ref_xerrs = [
  [abs(xpoints['rivet_hydro_merged.yoda'][i]   - xedges['rivet_hydro_merged.yoda'][i]) for i in range(len(xpoints['rivet_hydro_merged.yoda']))],
  [abs(xedges['rivet_hydro_merged.yoda'][i+1] - xpoints['rivet_hydro_merged.yoda'][i]) for i in range(len(xpoints['rivet_hydro_merged.yoda']))]
]

yvals = {
    'rivet_hydro_merged.yoda' : [2.992131e-06, 1.702516e-06, 9.335867e-07, 5.503111e-07, 3.872029e-07,
                                 2.505713e-07, 1.839130e-07, 1.180502e-07, 7.935086e-08, 6.752364e-08],
}

xerrs = {
    'rivet_hydro_merged.yoda' : [
                                   [3.500000e+00, 3.500000e+00, 3.500000e+00, 3.500000e+00, 3.500000e+00,
                                    3.500000e+00, 3.500000e+00, 3.500000e+00, 3.500000e+00, 3.500000e+00],
                                   [3.500000e+00, 3.500000e+00, 3.500000e+00, 3.500000e+00, 3.500000e+00,
                                    3.500000e+00, 3.500000e+00, 3.500000e+00, 3.500000e+00, 3.500000e+00],
                                ],
}

yerrs = {
    'rivet_hydro_merged.yoda' : [
                                   [1.124093e-07, 7.144434e-08, 3.490850e-08, 2.026842e-08, 1.700293e-08,
                                    1.136779e-08, 1.078026e-08, 6.179210e-09, 3.438585e-09, 3.869151e-09],
                                   [1.124093e-07, 7.144434e-08, 3.490850e-08, 2.026842e-08, 1.700293e-08,
                                    1.136779e-08, 1.078026e-08, 6.179210e-09, 3.438585e-09, 3.869151e-09],
                                ],
}

variation_yvals = {
}



# lists for ratio plot
ratio0_yvals = {
    'rivet_hydro_merged.yoda' : [1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00,
                                 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00],
}

ratio0_yerrs = {
    'rivet_hydro_merged.yoda' : [
                                   [3.756831e-02, 4.196398e-02, 3.739181e-02, 3.683084e-02, 4.391220e-02,
                                    4.536750e-02, 5.861607e-02, 5.234393e-02, 4.333394e-02, 5.730068e-02],
                                   [3.756831e-02, 4.196398e-02, 3.739181e-02, 3.683084e-02, 4.391220e-02,
                                    4.536750e-02, 5.861607e-02, 5.234393e-02, 4.333394e-02, 5.730068e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

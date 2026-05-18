
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
    'rivet_hydro_merged.yoda' : [1.404814e-05, 7.868563e-06, 4.721180e-06, 2.759530e-06, 1.788189e-06,
                                 1.154537e-06, 7.847343e-07, 5.369641e-07, 3.809153e-07, 2.749874e-07],
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
                                   [2.348153e-07, 1.539331e-07, 9.978421e-08, 5.061894e-08, 3.277241e-08,
                                    3.028441e-08, 1.729950e-08, 1.207419e-08, 8.985325e-09, 6.297152e-09],
                                   [2.348153e-07, 1.539331e-07, 9.978421e-08, 5.061894e-08, 3.277241e-08,
                                    3.028441e-08, 1.729950e-08, 1.207419e-08, 8.985325e-09, 6.297152e-09],
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
                                   [1.671504e-02, 1.956306e-02, 2.113544e-02, 1.834332e-02, 1.832716e-02,
                                    2.623080e-02, 2.204505e-02, 2.248602e-02, 2.358877e-02, 2.289978e-02],
                                   [1.671504e-02, 1.956306e-02, 2.113544e-02, 1.834332e-02, 1.832716e-02,
                                    2.623080e-02, 2.204505e-02, 2.248602e-02, 2.358877e-02, 2.289978e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

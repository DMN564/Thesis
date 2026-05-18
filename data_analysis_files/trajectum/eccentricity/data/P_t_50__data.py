
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
    'rivet_hydro_merged.yoda' : [4.431894e-05, 2.486839e-05, 1.425114e-05, 8.614714e-06, 5.486199e-06,
                                 3.584760e-06, 2.386227e-06, 1.648031e-06, 1.167679e-06, 8.161483e-07],
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
                                   [4.328135e-07, 2.807626e-07, 1.553051e-07, 9.482109e-08, 6.471678e-08,
                                    4.714063e-08, 2.785496e-08, 2.196988e-08, 1.534178e-08, 9.905623e-09],
                                   [4.328135e-07, 2.807626e-07, 1.553051e-07, 9.482109e-08, 6.471678e-08,
                                    4.714063e-08, 2.785496e-08, 2.196988e-08, 1.534178e-08, 9.905623e-09],
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
                                   [9.765880e-03, 1.128994e-02, 1.089773e-02, 1.100688e-02, 1.179629e-02,
                                    1.315029e-02, 1.167322e-02, 1.333098e-02, 1.313870e-02, 1.213704e-02],
                                   [9.765880e-03, 1.128994e-02, 1.089773e-02, 1.100688e-02, 1.179629e-02,
                                    1.315029e-02, 1.167322e-02, 1.333098e-02, 1.313870e-02, 1.213704e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

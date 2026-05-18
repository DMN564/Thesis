
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
    'rivet_hydro_merged.yoda' : [2.852584e-06, 1.600450e-06, 9.905143e-07, 5.698920e-07, 3.779911e-07,
                                 2.541260e-07, 1.598161e-07, 1.148320e-07, 8.409790e-08, 5.668277e-08],
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
                                   [9.045362e-08, 8.100215e-08, 3.800609e-08, 2.303649e-08, 1.423571e-08,
                                    1.239895e-08, 7.237899e-09, 5.703107e-09, 4.119730e-09, 3.145930e-09],
                                   [9.045362e-08, 8.100215e-08, 3.800609e-08, 2.303649e-08, 1.423571e-08,
                                    1.239895e-08, 7.237899e-09, 5.703107e-09, 4.119730e-09, 3.145930e-09],
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
                                   [3.170936e-02, 5.061211e-02, 3.837006e-02, 4.042256e-02, 3.766148e-02,
                                    4.879055e-02, 4.528891e-02, 4.966478e-02, 4.898731e-02, 5.550064e-02],
                                   [3.170936e-02, 5.061211e-02, 3.837006e-02, 4.042256e-02, 3.766148e-02,
                                    4.879055e-02, 4.528891e-02, 4.966478e-02, 4.898731e-02, 5.550064e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

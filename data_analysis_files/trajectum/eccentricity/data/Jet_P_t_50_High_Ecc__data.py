
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
    'rivet_hydro_merged.yoda' : [9.299790e-06, 5.108386e-06, 3.068869e-06, 1.809823e-06, 1.126326e-06,
                                 7.555956e-07, 5.009409e-07, 3.472151e-07, 2.487514e-07, 1.733369e-07],
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
                                   [1.875443e-07, 1.180956e-07, 6.765127e-08, 4.003865e-08, 2.453672e-08,
                                    1.843011e-08, 1.199419e-08, 9.965169e-09, 7.126801e-09, 4.852374e-09],
                                   [1.875443e-07, 1.180956e-07, 6.765127e-08, 4.003865e-08, 2.453672e-08,
                                    1.843011e-08, 1.199419e-08, 9.965169e-09, 7.126801e-09, 4.852374e-09],
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
                                   [2.016651e-02, 2.311798e-02, 2.204437e-02, 2.212296e-02, 2.178475e-02,
                                    2.439150e-02, 2.394333e-02, 2.870027e-02, 2.865029e-02, 2.799389e-02],
                                   [2.016651e-02, 2.311798e-02, 2.204437e-02, 2.212296e-02, 2.178475e-02,
                                    2.439150e-02, 2.394333e-02, 2.870027e-02, 2.865029e-02, 2.799389e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

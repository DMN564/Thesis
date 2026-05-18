
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
    'rivet_hydro_merged.yoda' : [8.497371e-06, 4.675389e-06, 2.734193e-06, 1.716106e-06, 1.057925e-06,
                                 6.989063e-07, 4.673126e-07, 3.225936e-07, 2.304691e-07, 1.634066e-07],
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
                                   [1.685688e-07, 9.849356e-08, 6.272473e-08, 4.019821e-08, 2.365470e-08,
                                    2.687840e-08, 1.187747e-08, 9.835466e-09, 5.832004e-09, 4.561688e-09],
                                   [1.685688e-07, 9.849356e-08, 6.272473e-08, 4.019821e-08, 2.365470e-08,
                                    2.687840e-08, 1.187747e-08, 9.835466e-09, 5.832004e-09, 4.561688e-09],
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
                                   [1.983776e-02, 2.106639e-02, 2.294086e-02, 2.342408e-02, 2.235953e-02,
                                    3.845780e-02, 2.541654e-02, 3.048872e-02, 2.530492e-02, 2.791619e-02],
                                   [1.983776e-02, 2.106639e-02, 2.294086e-02, 2.342408e-02, 2.235953e-02,
                                    3.845780e-02, 2.541654e-02, 3.048872e-02, 2.530492e-02, 2.791619e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

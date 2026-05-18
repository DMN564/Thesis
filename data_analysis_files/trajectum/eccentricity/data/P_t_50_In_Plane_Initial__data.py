
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
    'rivet_hydro_merged.yoda' : [1.546200e-05, 8.826999e-06, 4.936696e-06, 3.027783e-06, 1.840229e-06,
                                 1.231321e-06, 8.385080e-07, 5.558931e-07, 4.098443e-07, 2.748853e-07],
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
                                   [2.581153e-07, 1.756395e-07, 8.928117e-08, 6.429836e-08, 4.402684e-08,
                                    2.402522e-08, 1.734970e-08, 1.414965e-08, 1.014259e-08, 5.568567e-09],
                                   [2.581153e-07, 1.756395e-07, 8.928117e-08, 6.429836e-08, 4.402684e-08,
                                    2.402522e-08, 1.734970e-08, 1.414965e-08, 1.014259e-08, 5.568567e-09],
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
                                   [1.669353e-02, 1.989799e-02, 1.808521e-02, 2.123612e-02, 2.392466e-02,
                                    1.951175e-02, 2.069116e-02, 2.545391e-02, 2.474742e-02, 2.025779e-02],
                                   [1.669353e-02, 1.989799e-02, 1.808521e-02, 2.123612e-02, 2.392466e-02,
                                    1.951175e-02, 2.069116e-02, 2.545391e-02, 2.474742e-02, 2.025779e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

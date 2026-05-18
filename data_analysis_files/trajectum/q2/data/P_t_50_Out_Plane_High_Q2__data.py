
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
    'rivet_hydro_merged.yoda' : [2.651814e-06, 1.541390e-06, 8.651836e-07, 5.583239e-07, 3.358769e-07,
                                 2.409819e-07, 1.446759e-07, 1.065220e-07, 7.420413e-08, 5.460314e-08],
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
                                   [8.782323e-08, 6.492759e-08, 3.107385e-08, 2.373831e-08, 1.265717e-08,
                                    2.321590e-08, 6.451473e-09, 5.062332e-09, 2.933913e-09, 3.055802e-09],
                                   [8.782323e-08, 6.492759e-08, 3.107385e-08, 2.373831e-08, 1.265717e-08,
                                    2.321590e-08, 6.451473e-09, 5.062332e-09, 2.933913e-09, 3.055802e-09],
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
                                   [3.311817e-02, 4.212275e-02, 3.591590e-02, 4.251710e-02, 3.768396e-02,
                                    9.633878e-02, 4.459261e-02, 4.752380e-02, 3.953841e-02, 5.596386e-02],
                                   [3.311817e-02, 4.212275e-02, 3.591590e-02, 4.251710e-02, 3.768396e-02,
                                    9.633878e-02, 4.459261e-02, 4.752380e-02, 3.953841e-02, 5.596386e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}


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
    'rivet_hydro_merged.yoda' : [3.029081e-06, 1.681646e-06, 9.423641e-07, 5.957960e-07, 3.748956e-07,
                                 2.318834e-07, 1.715986e-07, 1.109329e-07, 8.223973e-08, 5.424719e-08],
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
                                   [1.085391e-07, 5.749106e-08, 3.880903e-08, 2.322471e-08, 1.501342e-08,
                                    8.687275e-09, 7.929187e-09, 6.584129e-09, 3.776809e-09, 2.427221e-09],
                                   [1.085391e-07, 5.749106e-08, 3.880903e-08, 2.322471e-08, 1.501342e-08,
                                    8.687275e-09, 7.929187e-09, 6.584129e-09, 3.776809e-09, 2.427221e-09],
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
                                   [3.583234e-02, 3.418738e-02, 4.118262e-02, 3.898098e-02, 4.004693e-02,
                                    3.746398e-02, 4.620777e-02, 5.935236e-02, 4.592439e-02, 4.474373e-02],
                                   [3.583234e-02, 3.418738e-02, 4.118262e-02, 3.898098e-02, 4.004693e-02,
                                    3.746398e-02, 4.620777e-02, 5.935236e-02, 4.592439e-02, 4.474373e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

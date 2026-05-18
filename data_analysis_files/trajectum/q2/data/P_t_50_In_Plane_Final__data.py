
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
    'rivet_hydro_merged.yoda' : [1.543419e-05, 8.714644e-06, 4.900671e-06, 3.011766e-06, 1.812654e-06,
                                 1.241528e-06, 8.445999e-07, 5.459907e-07, 4.063830e-07, 2.705939e-07],
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
                                   [2.568356e-07, 1.705226e-07, 9.152378e-08, 5.349665e-08, 3.176409e-08,
                                    2.785524e-08, 1.728035e-08, 1.185748e-08, 9.740908e-09, 5.318293e-09],
                                   [2.568356e-07, 1.705226e-07, 9.152378e-08, 5.349665e-08, 3.176409e-08,
                                    2.785524e-08, 1.728035e-08, 1.185748e-08, 9.740908e-09, 5.318293e-09],
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
                                   [1.664069e-02, 1.956736e-02, 1.867576e-02, 1.776255e-02, 1.752352e-02,
                                    2.243626e-02, 2.045980e-02, 2.171736e-02, 2.396977e-02, 1.965415e-02],
                                   [1.664069e-02, 1.956736e-02, 1.867576e-02, 1.776255e-02, 1.752352e-02,
                                    2.243626e-02, 2.045980e-02, 2.171736e-02, 2.396977e-02, 1.965415e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

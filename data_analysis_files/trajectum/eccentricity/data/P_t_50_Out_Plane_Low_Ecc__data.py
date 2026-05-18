
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
    'rivet_hydro_merged.yoda' : [2.848051e-06, 1.656597e-06, 9.473356e-07, 5.530340e-07, 3.522256e-07,
                                 2.244760e-07, 1.759229e-07, 1.052166e-07, 7.518731e-08, 5.855207e-08],
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
                                   [1.176332e-07, 6.721132e-08, 4.343101e-08, 2.407536e-08, 1.451974e-08,
                                    9.936670e-09, 7.986145e-09, 5.335306e-09, 3.806213e-09, 3.154785e-09],
                                   [1.176332e-07, 6.721132e-08, 4.343101e-08, 2.407536e-08, 1.451974e-08,
                                    9.936670e-09, 7.986145e-09, 5.335306e-09, 3.806213e-09, 3.154785e-09],
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
                                   [4.130303e-02, 4.057191e-02, 4.584543e-02, 4.353323e-02, 4.122285e-02,
                                    4.426607e-02, 4.539572e-02, 5.070781e-02, 5.062307e-02, 5.388000e-02],
                                   [4.130303e-02, 4.057191e-02, 4.584543e-02, 4.353323e-02, 4.122285e-02,
                                    4.426607e-02, 4.539572e-02, 5.070781e-02, 5.062307e-02, 5.388000e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

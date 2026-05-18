
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
    'rivet_hydro_merged.yoda' : [1.415418e-05, 7.920410e-06, 4.655857e-06, 2.747860e-06, 1.807613e-06,
                                 1.152646e-06, 7.776173e-07, 5.446607e-07, 3.800936e-07, 2.767974e-07],
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
                                   [2.394442e-07, 1.535137e-07, 9.467115e-08, 4.951275e-08, 3.357933e-08,
                                    3.025981e-08, 1.718899e-08, 1.212477e-08, 8.743610e-09, 6.278688e-09],
                                   [2.394442e-07, 1.535137e-07, 9.467115e-08, 4.951275e-08, 3.357933e-08,
                                    3.025981e-08, 1.718899e-08, 1.212477e-08, 8.743610e-09, 6.278688e-09],
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
                                   [1.691685e-02, 1.938204e-02, 2.033377e-02, 1.801866e-02, 1.857662e-02,
                                    2.625248e-02, 2.210469e-02, 2.226115e-02, 2.300384e-02, 2.268333e-02],
                                   [1.691685e-02, 1.938204e-02, 2.033377e-02, 1.801866e-02, 1.857662e-02,
                                    2.625248e-02, 2.210469e-02, 2.226115e-02, 2.300384e-02, 2.268333e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

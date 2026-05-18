
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
    'rivet_hydro_merged.yoda' : [2.950706e-06, 1.650831e-06, 9.649814e-07, 6.111447e-07, 3.405576e-07,
                                 2.487399e-07, 1.590583e-07, 1.134659e-07, 8.160180e-08, 5.434444e-08],
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
                                   [1.094221e-07, 7.413940e-08, 4.582794e-08, 4.392207e-08, 1.393554e-08,
                                    1.252050e-08, 7.552040e-09, 8.729389e-09, 4.073230e-09, 2.656032e-09],
                                   [1.094221e-07, 7.413940e-08, 4.582794e-08, 4.392207e-08, 1.393554e-08,
                                    1.252050e-08, 7.552040e-09, 8.729389e-09, 4.073230e-09, 2.656032e-09],
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
                                   [3.708338e-02, 4.491034e-02, 4.749101e-02, 7.186852e-02, 4.091979e-02,
                                    5.033571e-02, 4.747970e-02, 7.693402e-02, 4.991594e-02, 4.887403e-02],
                                   [3.708338e-02, 4.491034e-02, 4.749101e-02, 7.186852e-02, 4.091979e-02,
                                    5.033571e-02, 4.747970e-02, 7.693402e-02, 4.991594e-02, 4.887403e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}


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
    'rivet_hydro_merged.yoda' : [8.704240e-06, 5.023939e-06, 2.813007e-06, 1.697393e-06, 1.097616e-06,
                                 7.295963e-07, 4.867360e-07, 3.277496e-07, 2.306196e-07, 1.677040e-07],
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
                                   [1.905404e-07, 1.384605e-07, 7.290916e-08, 5.398042e-08, 2.697547e-08,
                                    2.422129e-08, 1.250575e-08, 1.176304e-08, 6.266132e-09, 4.809629e-09],
                                   [1.905404e-07, 1.384605e-07, 7.290916e-08, 5.398042e-08, 2.697547e-08,
                                    2.422129e-08, 1.250575e-08, 1.176304e-08, 6.266132e-09, 4.809629e-09],
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
                                   [2.189053e-02, 2.756016e-02, 2.591858e-02, 3.180196e-02, 2.457643e-02,
                                    3.319821e-02, 2.569309e-02, 3.589033e-02, 2.717086e-02, 2.867927e-02],
                                   [2.189053e-02, 2.756016e-02, 2.591858e-02, 3.180196e-02, 2.457643e-02,
                                    3.319821e-02, 2.569309e-02, 3.589033e-02, 2.717086e-02, 2.867927e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

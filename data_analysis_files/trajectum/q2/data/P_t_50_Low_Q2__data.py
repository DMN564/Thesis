
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
    'rivet_hydro_merged.yoda' : [9.203097e-06, 5.367631e-06, 2.944866e-06, 1.791373e-06, 1.169979e-06,
                                 7.526153e-07, 5.068283e-07, 3.448257e-07, 2.357081e-07, 1.753287e-07],
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
                                   [1.875481e-07, 1.369058e-07, 6.940076e-08, 5.450958e-08, 4.056977e-08,
                                    1.946817e-08, 1.365767e-08, 9.879586e-09, 6.105748e-09, 4.864442e-09],
                                   [1.875481e-07, 1.369058e-07, 6.940076e-08, 5.450958e-08, 4.056977e-08,
                                    1.946817e-08, 1.365767e-08, 9.879586e-09, 6.105748e-09, 4.864442e-09],
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
                                   [2.037881e-02, 2.550581e-02, 2.356670e-02, 3.042894e-02, 3.467564e-02,
                                    2.586736e-02, 2.694733e-02, 2.865096e-02, 2.590385e-02, 2.774470e-02],
                                   [2.037881e-02, 2.550581e-02, 2.356670e-02, 3.042894e-02, 3.467564e-02,
                                    2.586736e-02, 2.694733e-02, 2.865096e-02, 2.590385e-02, 2.774470e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

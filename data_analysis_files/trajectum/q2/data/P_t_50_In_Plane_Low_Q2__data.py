
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
    'rivet_hydro_merged.yoda' : [3.101493e-06, 1.776549e-06, 1.033308e-06, 6.365999e-07, 3.571006e-07,
                                 2.567180e-07, 1.628650e-07, 1.133576e-07, 7.871943e-08, 5.248674e-08],
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
                                   [1.060959e-07, 8.186684e-08, 4.339696e-08, 2.819549e-08, 1.321796e-08,
                                    1.280776e-08, 6.229233e-09, 5.080744e-09, 3.680589e-09, 1.934141e-09],
                                   [1.060959e-07, 8.186684e-08, 4.339696e-08, 2.819549e-08, 1.321796e-08,
                                    1.280776e-08, 6.229233e-09, 5.080744e-09, 3.680589e-09, 1.934141e-09],
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
                                   [3.420800e-02, 4.608196e-02, 4.199808e-02, 4.429076e-02, 3.701467e-02,
                                    4.989040e-02, 3.824783e-02, 4.482049e-02, 4.675579e-02, 3.685008e-02],
                                   [3.420800e-02, 4.608196e-02, 4.199808e-02, 4.429076e-02, 3.701467e-02,
                                    4.989040e-02, 3.824783e-02, 4.482049e-02, 4.675579e-02, 3.685008e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

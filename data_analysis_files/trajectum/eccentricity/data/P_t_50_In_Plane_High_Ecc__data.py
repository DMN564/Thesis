
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
    'rivet_hydro_merged.yoda' : [3.450249e-06, 1.871066e-06, 1.093029e-06, 6.292424e-07, 3.719943e-07,
                                 2.613281e-07, 1.769743e-07, 1.171049e-07, 8.595410e-08, 5.924679e-08],
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
                                   [1.326041e-07, 6.717467e-08, 4.319050e-08, 2.564901e-08, 1.292550e-08,
                                    9.638778e-09, 7.598747e-09, 6.778646e-09, 4.774022e-09, 2.688137e-09],
                                   [1.326041e-07, 6.717467e-08, 4.319050e-08, 2.564901e-08, 1.292550e-08,
                                    9.638778e-09, 7.598747e-09, 6.778646e-09, 4.774022e-09, 2.688137e-09],
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
                                   [3.843321e-02, 3.590182e-02, 3.951452e-02, 4.076173e-02, 3.474651e-02,
                                    3.688381e-02, 4.293701e-02, 5.788525e-02, 5.554153e-02, 4.537187e-02],
                                   [3.843321e-02, 3.590182e-02, 3.951452e-02, 4.076173e-02, 3.474651e-02,
                                    3.688381e-02, 4.293701e-02, 5.788525e-02, 5.554153e-02, 4.537187e-02],
                                ],
}

ratio0_variation_vals = {
}

ratio_band_edges = {
}

import yoda

from histogram import get_histograms

import numpy as np


import matplotlib.pyplot as plt

x_in, _, y_in, x_in_err, y_in_err = get_histograms("/home/dahamvin/2. Glauber_Plots/Comparison_Plots/30_50_Eccentricity/data/P_t_50_In_Plane_Low_ecc")[0]
x_out, _, y_out, x_out_err, y_out_err = get_histograms("/home/dahamvin/2. Glauber_Plots/Comparison_Plots/30_50_Eccentricity/data/P_t_50_Out_Plane_Low_ecc")[0]
x_all, _, y_all, x_all_err, y_all_err = get_histograms("/home/dahamvin/2. Glauber_Plots/Comparison_Plots/30_50_Eccentricity/data/Jet_P_t_50")[0]

aos = yoda.read("rivet_merged.yoda")
N_all    = aos["/MC_GLAUBER_PT/N_EVENTS"].numEntries()
N_highEcc = aos["/MC_GLAUBER_PT/N_EVENTS_HIGH_ECC"].numEntries()
N_lowEcc  = aos["/MC_GLAUBER_PT/N_EVENTS_LOW_ECC"].numEntries()




y_in     = y_in * (N_all / N_lowEcc)
y_in_err = y_in_err * (N_all / N_lowEcc)

y_out      = y_out * (N_all / N_lowEcc)
y_out_err  = y_out_err * (N_all / N_lowEcc)

y_ref     = y_all * (1./3.)
y_ref_err = y_all_err * (1./3.)

ratio_in = y_in / y_ref
ratio_out  = y_out / y_ref

ratio_err_in = ratio_in * np.hypot(y_in_err / y_in, y_ref_err / y_ref)
ratio_err_out  = ratio_out * np.hypot(y_out_err / y_out, y_ref_err / y_ref)


def main():
    # 3. Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True,
                                   gridspec_kw={'height_ratios': [3, 1]})

    # --- Top panel: Use 'mid' for histograms ---
    ax1.step(x_in, y_in, where='mid', color='firebrick', label=r'In-Plane', lw=1.5)
    ax1.step(x_out, y_out, where='mid', color='royalblue', label=r'Out-of-Plane', lw=1.5)
    ax1.step(x_all, y_ref, where='mid', color='black', label='Inclusive (Baseline) x (1/3)', lw=1.2)

    ax1.errorbar(x_in, y_in, yerr=y_in_err, fmt='none', ecolor='firebrick', alpha=0.5)
    ax1.errorbar(x_out, y_out, yerr=y_out_err, fmt='none', ecolor='royalblue', alpha=0.5)

    ax1.set_yscale('log')
    ax1.set_ylabel(r'$\frac{1}{N_{\mathrm{evt}}}dN_{jets}/dp_T$',fontsize=16)
    ax1.legend(frameon=False, fontsize=14)

    # --- Bottom panel: Ratios ---
    ax2.step(x_in, ratio_in, where='mid', color='firebrick')
    ax2.step(x_out, ratio_out, where='mid', color='royalblue')

    ax2.errorbar(x_in, ratio_in, yerr=ratio_err_in, fmt='none', ecolor='firebrick', alpha=0.4)
    ax2.errorbar(x_out, ratio_out, yerr=ratio_err_out, fmt='none', ecolor='royalblue', alpha=0.4)

    ax2.axhline(1.0, color='black', lw=0.8, ls='-')
    ax2.set_ylabel('Ratio to Inclusive',fontsize=14)
    ax2.set_ylim(0.5, 1.5)
    ax2.set_xlabel(r'Jet $p_T$ [GeV/c]',fontsize=16)
    ax1.set_title(r'Jet Spectra: 30-50% Centrality In-Plane vs Out-of-Plane with Low Eccentricity',fontsize=12)
    fig.tight_layout()
    fig.savefig('/home/dahamvin/2. Glauber_Plots/Comparison_Plots/30_50_Eccentricity/Jet_Comparison_30_50_Low_ecc.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()

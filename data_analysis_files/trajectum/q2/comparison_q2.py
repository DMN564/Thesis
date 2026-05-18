import yoda

from histogram import get_histograms

import numpy as np

import matplotlib.pyplot as plt

x_in, _, y_in, x_in_err, y_in_err = get_histograms("data/P_t_50_High_Q2")[0]
x_out, _, y_out, x_out_err, y_out_err = get_histograms("data/P_t_50_Low_Q2")[0]
x_all,  _, y_all,  _, y_all_err  = get_histograms("data/P_t_50")[0]

aos = yoda.read("rivet_hydro_merged.yoda")
N_all    = aos["/MC_TRAJECTUM_PT/N_EVENTS"].numEntries()
N_highQ2 = aos["/MC_TRAJECTUM_PT/N_EVENTS_HIGH_Q2"].numEntries()
N_lowQ2  = aos["/MC_TRAJECTUM_PT/N_EVENTS_LOW_Q2"].numEntries()

print(N_all)
print(N_highQ2)
print(N_lowQ2)



y_in     = y_in * (N_all / N_highQ2)
y_in_err = y_in_err * (N_all / N_highQ2)

y_out      = y_out * (N_all / N_lowQ2)
y_out_err  = y_out_err * (N_all / N_lowQ2)

y_ref     = y_all
y_ref_err = y_all_err

ratio_in = y_in / y_ref
ratio_out  = y_out / y_ref

ratio_err_in = ratio_in * np.hypot(y_in_err / y_in, y_ref_err / y_ref)
ratio_err_out  = ratio_out * np.hypot(y_out_err / y_out, y_ref_err / y_ref)


def main():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True,
                                   gridspec_kw={'height_ratios': [3, 1]})

    # --- Top panel: Use 'mid' for histograms ---
    ax1.step(x_in, y_in, where='mid', color='firebrick', label=r'High $q_2$', lw=1.5)
    ax1.step(x_out, y_out, where='mid', color='royalblue', label=r'Low $q_2$', lw=1.5)
    ax1.step(x_all, y_ref, where='mid', color='black', label='Inclusive (Baseline)', lw=1.2)

    ax1.errorbar(x_in, y_in, yerr=y_in_err, fmt='none', ecolor='firebrick', alpha=0.5)
    ax1.errorbar(x_out, y_out, yerr=y_out_err, fmt='none', ecolor='royalblue', alpha=0.5)

    ax1.set_yscale('log')
    ax1.set_ylabel(r'$\frac{1}{N_{\mathrm{evt}}}dN_{jets}/dp_T$',fontsize=16)
    ax1.legend(frameon=False, fontsize=14)

    ax2.step(x_in, ratio_in, where='mid', color='firebrick')
    ax2.step(x_out, ratio_out, where='mid', color='royalblue')

    ax2.errorbar(x_in, ratio_in, yerr=ratio_err_in, fmt='none', ecolor='firebrick', alpha=0.4)
    ax2.errorbar(x_out, ratio_out, yerr=ratio_err_out, fmt='none', ecolor='royalblue', alpha=0.4)

    ax2.axhline(1.0, color='black', lw=0.8, ls='-')
    ax2.set_ylabel('Ratio to Inclusive',fontsize=14)
    ax2.set_ylim(0.8, 1.3)
    ax2.set_xlabel(r'Jet $p_T$ [GeV/c]',fontsize=16)
    ax1.set_title(r'Jet Spectra: 30-50% Centrality Low $q_2$ vs High $q_2$ (In-Plane and Out-of-Plane)',fontsize=13)
    fig.tight_layout()
    fig.savefig('/home/dahamvin/3. Trajectum_Plots/Comparison_Plots/30_50_Q2/Jet_Comparison_30_50_All_Ori.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()

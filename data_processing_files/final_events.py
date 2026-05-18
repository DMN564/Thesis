import numpy as np
data_q = np.loadtxt("txt_files/combined_events.txt")
data_e = np.loadtxt("txt_files/combined_id_eps_phi.txt")

q_dict = {int(row[0]): row[1:] for row in data_q}
e_dict = {int(row[0]): row[1:] for row in data_e}

common_ids = sorted(set(q_dict.keys()) & set(e_dict.keys()))

merged = np.array([
    [eid, *q_dict[eid], *e_dict[eid]]
    for eid in common_ids
])

np.savetxt(
    "txt_files/final_events.txt",
    merged,
    fmt=["%d", "%.6f", "%.6f", "%.6f", "%.6f"],
    header="# Event_ID q2 Psi_EP epsilon2 phi2",
    comments=''
)

print(f"Combined file saved to final_events.txt")
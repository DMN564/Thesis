import numpy as np


def load_events(filename):
    events = []
    current_event_particles = []
    current_event_id = None

    with open(filename, 'r') as f:
        for line in f:
            if line.startswith("# event ") and " out " in line:
                if current_event_id is not None:
                    arr = np.array(current_event_particles)
                    reshaped_arr = arr.reshape(-1, 12) if arr.size > 0 else np.zeros((0, 12))
                    events.append((current_event_id, reshaped_arr))

                parts = line.split()
                current_event_id = int(parts[2])
                current_event_particles = []
                continue

            if line.startswith("#") or not line.strip():
                continue

            parts = line.split()
            if len(parts) >= 12:
                charge = float(parts[11])
                px, py, pz = float(parts[6]), float(parts[7]), float(parts[8])
                pt = np.sqrt(px ** 2 + py ** 2)
                energy = np.sqrt(pt ** 2 + pz ** 2)
                rapidity = np.log((energy + pz + 1e-9) / (pt + 1e-9))

                if charge != 0 and pt > 0.2 and np.abs(rapidity) < 1:
                    current_event_particles.append([float(x) for x in parts])

    if current_event_id is not None:
        arr = np.array(current_event_particles)
        reshaped_arr = arr.reshape(-1, 12) if arr.size > 0 else np.zeros((0, 12))
        events.append((current_event_id, reshaped_arr))

    return events

#Load 3000 final state events
data = load_events("PbPb.afterburned.3000")

#Load 1000 final state events
#data = load_events("PbPb.afterburned.1000")

all_mults = np.array([len(event[1]) for event in data])
upper_bound = np.percentile(all_mults, 70)  # 30% centrality threshold
lower_bound = np.percentile(all_mults, 50)  # 50% centrality threshold

phis, psi_eps, qs, multiplicities, p_t, pseudo_rap, output_results, filtered_results = [], [], [], [], [], [], [], []

for true_id, event_particles in data:
    n_particles = len(event_particles)

    if lower_bound <= n_particles <= upper_bound:
        x_event = event_particles[:, 2]
        y_event = event_particles[:, 3]
        px_event = event_particles[:, 6]
        py_event = event_particles[:, 7]
        pz_event = event_particles[:, 8]

        multiplicities.append(n_particles)

        # Centering
        X0, Y0 = np.mean(x_event), np.mean(y_event)
        x_centered, y_centered = x_event - X0, y_event - Y0

        # Transverse momentum and phi
        phi = np.arctan2(py_event, px_event)
        phis.append(phi)
        pt = np.sqrt(px_event ** 2 + py_event ** 2)
        p_t.append(pt)

        # Finding event plane angle
        x_comp = np.mean(np.cos(2 * phi))
        y_comp = np.mean(np.sin(2 * phi))
        psi_ep = 0.5 * np.arctan2(y_comp, x_comp)
        psi_eps.append(psi_ep)

        # Pseudo-rapidity
        ps_rap = np.log((np.sqrt(pt ** 2 + pz_event ** 2) + pz_event + 1e-9) / (pt + 1e-9))
        pseudo_rap.append(ps_rap)

        # Calculate Q-vector and q
        Q2x = np.sum(pt * np.cos(2 * phi))
        Q2y = np.sum(pt * np.sin(2 * phi))
        W = np.sum(pt)
        q = np.sqrt(Q2x ** 2 + Q2y ** 2) / np.sqrt(W)
        qs.append(q)

        # Save result for this event
        output_results.append([true_id, q, psi_ep])
    else:
        # Event is outside centrality range: save placeholder to keep file order
        output_results.append([true_id, np.nan, np.nan])

for row in output_results:
    if not np.isnan(row[1]):
        filtered_results.append(row)

header = "Event_ID    q2    Psi_EP"
np.savetxt("txt_files/event_analysis_more_3000.txt", output_results, header=header, fmt=['%d', '%.6f', '%.6f'])
np.savetxt("txt_files/event_analysis_filtered_more_3000.txt", filtered_results, header=header, fmt=['%d', '%.6f', '%.6f'])

#np.savetxt("event_analysis_more_1000.txt", output_results, header=header, fmt=['%d', '%.6f', '%.6f'])
#np.savetxt("event_analysis_filtered_more_1000.txt", filtered_results, header=header, fmt=['%d', '%.6f', '%.6f'])

psi2_values = [filtered_results[i][2] for i in range(len(filtered_results))]
event_numbers = [filtered_results[i][0] for i in range(len(filtered_results))]
with open("txt_files/event_numbers_more_3000.txt", "w") as f:
    f.write(str(event_numbers))

#with open("txt_files/event_numbers_more_1000.txt", "w") as f:
#    f.write(str(event_numbers))

print(f"Total events loaded: {len(data)}")
print(f"Filtered events: {len(event_numbers)}")

import numpy as np

def extract_physics_parameters(filename):
    event_numbers=[]
    epsilon2 = []
    phi2 = []
    phi_rp = []

    with open(filename, 'r') as f:
        lines = f.readlines()

        header_index = -1
        for i, line in enumerate(lines):
            if line.startswith("## event") and "epsilon2" in line:
                header_index = i
                break

        if header_index == -1:
            print("Could not find the physics data header.")
            return None

        header_cols = lines[header_index].strip().split('\t')

        header_cols[0] = header_cols[0].replace('## ', '')

        idx_e2 = header_cols.index("epsilon2")
        idx_p2 = header_cols.index("phi2")
        idx_rp = header_cols.index("phireactionplane")

        for line in lines[header_index + 1:]:
            if line.startswith("#") or not line.strip():
                continue

            parts = line.strip().split('\t')

            if len(parts) > max(idx_e2, idx_p2, idx_rp):
                event_numbers.append(int(parts[0]))
                epsilon2.append(float(parts[idx_e2]))
                phi2.append(float(parts[idx_p2]))
                phi_rp.append(float(parts[idx_rp]))

    return np.array(event_numbers), np.array(epsilon2), np.array(phi2), np.array(phi_rp)

filename1 = 'PbPb.extra.1000'
filename2 = 'PbPb.extra.3000'
event_num_1, eps2_1, phi2_1, phi_rp_1 = extract_physics_parameters(filename1)
event_num_2, eps2_2, phi2_2, phi_rp_2 = extract_physics_parameters(filename2)

with open("txt_files/event_numbers_more_1000.txt") as f:
    text1 = f.read()

selected_events1 = np.fromstring(text1.strip("[]"), sep=",", dtype=int)

mask1 = np.isin(event_num_1, selected_events1)

filtered_data1 = np.column_stack((
    event_num_1[mask1],
    eps2_1[mask1],
    phi2_1[mask1]
))

np.savetxt(
    "txt_files/events_eps2_1.txt",
    filtered_data1,
    fmt=["%d", "%.6f", "%.6f"],
    header="Event_ID epsilon2 phi2",
    comments=''
)

with open("txt_files/event_numbers_more_3000.txt") as f:
    text2 = f.read()

selected_events2 = np.fromstring(text2.strip("[]"), sep=",", dtype=int)

mask2 = np.isin(event_num_2, selected_events2)

filtered_data2 = np.column_stack((
    event_num_2[mask2],
    eps2_2[mask2],
    phi2_2[mask2]
))

np.savetxt(
    "txt_files/events_eps2_2.txt",
    filtered_data2,
    fmt=["%d", "%.6f", "%.6f"],
    header="# Event_ID epsilon2 phi2",
    comments=''
)


remove_events = np.array([
    27, 28, 40, 57, 105, 120, 135, 149, 162, 245, 247, 256, 292, 303,
    334, 341, 379, 381, 391, 420, 427, 493, 524, 534, 575, 578, 586,
    657, 665, 701, 714, 732, 743, 777, 817, 836, 851, 907, 924, 958
])

mask_rm1 = ~np.isin(event_num_1, remove_events)

necessary_data1 = np.column_stack((
    event_num_1[mask_rm1],
    eps2_1[mask_rm1],
    phi2_1[mask_rm1]
))

np.savetxt(
    "txt_files/filtered_removed_1.txt",
    necessary_data1,
    fmt=["%d", "%.6f", "%.6f"],
    header="# Event_ID epsilon2 phi2",
    comments=''
)

data1 = np.loadtxt("txt_files/filtered_removed_1.txt")
data2 = np.loadtxt("txt_files/events_eps2_2.txt")

combined = np.vstack((data1, data2))

np.savetxt(
    "txt_files/combined_id_eps_phi.txt",
    combined,
    fmt=["%d", "%.6f", "%.6f"],
    header="# Event_ID epsilon2 phi2",
    comments=''
)

print(f"Epsilon and phi extracted to combined_id_eps_phi.txt")


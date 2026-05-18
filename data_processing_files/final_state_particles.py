oscar_file = "PbPb.afterburned.3000"
#oscar_file = "PbPb.afterburned.1000"
event_file = "final_events.txt"

target_events = set()

with open(event_file, "r") as f:

    for line in f:

        line = line.strip()

        if not line or line.startswith("#"):
            continue

        cols = line.split()

        event_id = int(cols[0])

        target_events.add(event_id)

print(f"Loaded {len(target_events)} target events")

all_pdg_ids = []

current_event = None

with open(oscar_file, "r") as f:

    for line in f:

        line = line.strip()

        if not line:
            continue

        if line.startswith("# event"):

            cols = line.split()

            current_event = int(cols[2])

            continue

        if line.startswith("#"):
            continue

        if current_event not in target_events:
            continue

        cols = line.split()

        pdg_id = int(cols[9])
        all_pdg_ids.append(pdg_id)

unique_pdgs = sorted(set(all_pdg_ids))

print("\nUnique PDG IDs found:\n")

for pdg in unique_pdgs:
    count = all_pdg_ids.count(pdg)

    print(f"PDG ID = {pdg:8d}   Count = {count}")
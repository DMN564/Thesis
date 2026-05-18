import pandas as pd

file1 = 'txt_files/event_analysis_filtered_more_1000.txt'
file2 = 'txt_files/event_analysis_filtered_more_3000.txt'
output_file = 'txt_files/combined_events.txt'

def get_ids(filename):
    ids = set()
    with open(filename) as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                ids.add(int(line.split()[0]))
    return ids

ids1 = get_ids("txt_files/event_analysis_filtered_more_1000.txt")
ids2 = get_ids("txt_files/event_analysis_filtered_more_3000.txt")

overlap = sorted(ids1 & ids2)

df1 = pd.read_csv(file1, sep=r'\s+')
df2 = pd.read_csv(file2, sep=r'\s+')

combined_df = pd.concat([df1, df2])

combined_df = combined_df.sort_values(by='#')

combined_df.to_csv(output_file, sep=' ', index=False)

print(f"Combined file saved to {output_file}")
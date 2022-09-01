
# How to run the script:
# Download all block data from https://gz.blockchair.com/bitcoin/blocks/
# Extract all tsv files using gunzip *.gz under ./data/bitcoin/blocks/

import pandas as pd
import numpy as np
import glob
files = glob.glob("./data/bitcoin/blocks/*.tsv")

blocks_df = pd.DataFrame()
for f in files:
    csv = pd.read_csv(f, sep='\t')
    blocks_df = blocks_df.append(csv)
    #break

blocks_df['time'] = pd.to_datetime(blocks_df['time'])

# Convert datetime to timestamp (ns)
blocks_df['ts'] = blocks_df['time'].values.astype(np.int64)
# Convert timestamp (ns) to timestamp (s)
blocks_df['ts'] = blocks_df['ts'] // 10**9
blocks_df = blocks_df.sort_values(by=['time'])
print(blocks_df.head())

# Calculate elapsed time between two consecutive blocks
ts_diff = blocks_df['ts'].diff()

print(sum(ts_diff > 2 * 3600))
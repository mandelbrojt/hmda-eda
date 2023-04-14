#!/bin/bash

# --- STEP 1 ---:
# Start by skiping the first row (the header) of the original `.csv` file.
# Then, pipe the remaining rows to the `shuf` command to shuffle them.
# Finally, create a different `.csv` file with all of its rows shuffled.
tail -n +2 data/year_2021.csv | shuf > data/year_2021_shuffled.csv

# --- STEP 2 ---:
# First, open the shuffled file with the `ed` text editor and the `-s` option.
# This allows for running commands in batch mode. 
# Then, insert the first row (headers) of the non-shuffled file to the shuffled file.
ed -s data/year_2021_shuffled.csv <<EOF
1i
$(head -n 1 data/year_2021.csv)
.
wq
EOF

# --- STEP 3 ---:
# Overwrite the original file with the content of the shuffled `.csv` file.
mv data/year_2021_shuffled.csv data/year_2021.csv

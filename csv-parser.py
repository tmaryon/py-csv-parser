import csv
import os
from collections import OrderedDict

# Adjusted paths
input_dir = "input/"  # Assuming this is a sibling directory to where the script is located
output_dir = "output/"
output_file = output_dir + "output.csv"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# perform first iteration to store the values for the header row, based on all files parsed
all_keys = set()
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        with open(os.path.join(input_dir, filename), mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                all_keys.add(row[0])

# write headers to output/output.csv
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Lead_ID"] + sorted(list(all_keys)))

# perform 2nd iteration to add the rows
file_count = 0
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        file_count += 1
        lead_id = filename.split('_')[0]
        values_dict = OrderedDict.fromkeys(all_keys)
        
        with open(os.path.join(input_dir, filename), mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # skip the header row
            next(reader)  
            for row in reader:
                values_dict[row[0]] = row[1]
        # uses append mode so data isn't overwritten 
        with open(output_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([lead_id] + [values_dict[key] for key in sorted(values_dict.keys())])

# verify the number of rows matches the number of files
# NOTE: this output is for info only, and won't stop the parsing
with open(output_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)
    if len(rows) - 1 != file_count:  # Subtract 1 for header
        print(f"Warning: Mismatch in file count and row count. Files: {file_count}, Rows: {len(rows) - 1}")
    else:
        print("File count matches row count.")

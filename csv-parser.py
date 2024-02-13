#!/usr/bin/env python3

import csv
import os
import glob

def main():
    # define paths for input and output directories
    # also output.csv
    input_path = 'input/*.csv'
    output_path = 'output/output.csv'
    all_data = []

    # read/parse all .csv files
    for file_name in glob.glob(input_path):
        parsed_data = parse_csv(file_name)
        all_data.append(parsed_data)

    # combine all data into a single csv file (output.csv)
    if all_data:
        # grab all unique headers defined in horizontal rows on
        # row 1
        headers = sorted(set().union(*all_data))  

        # check for output.csv and see if it's empty (to avoid writing header again)
        file_exists = os.path.isfile(output_path) and os.path.getsize(output_path) > 0

        # open file in append mode so it doesn't overwrite w/ each file
        with open(output_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            
            # write headers if the file doesn't exist
            if not file_exists:
                writer.writeheader()
            # write rows 
            for data in all_data:
                writer.writerow(data)
# execute main()
if __name__ == "__main__":
    main()

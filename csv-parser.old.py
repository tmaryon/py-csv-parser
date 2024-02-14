#!/usr/bin/env python3

import csv
import os
import glob

def parse_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Assuming each row has exactly two columns: key and value
        data = {rows[0]: rows[1] for rows in reader if len(rows) == 2}
    return data

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

    # merge all data into a single CSV
    if all_data:
        # get all unique headers
        headers = sorted(set().union(*all_data))

        # check for output.csv and see if it's empty (to avoid writing header again)
        file_exists = os.path.isfile(output_path) and os.path.getsize(output_path) > 0

        # append data to output.csv
        with open(output_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            
            # only write headers if the file doesn't exist 
            if not file_exists:
                writer.writeheader()
            
            # iterator for writing each row of data
            for data in all_data:
                writer.writerow(data)

if __name__ == "__main__":
    main()

#!/usr/bin/python3
'''Module for CSV to JSON conversion.'''

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file.
    """
    try:
        data = []

        with open(csv_filename, 'r') as csv_file:

            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

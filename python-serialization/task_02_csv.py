#!/sur/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        data = []
        with open(filename, 'r') as file_c:
            reader = csv.DictReader(file_c)
            for row in reader:
                data.append(row)
        with open("data.json", 'w') as file:
            file.write(json.dumps(data, indent=4))
    except Exception:
        return False
    return True

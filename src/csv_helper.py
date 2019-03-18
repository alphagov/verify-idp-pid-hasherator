import csv
import os


def read(path):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return reader.fieldnames, [row for row in reader]


def write(path, headers, data):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers, lineterminator=os.linesep)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

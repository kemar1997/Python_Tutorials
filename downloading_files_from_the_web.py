import csv

with open('real_estate.csv', 'rU') as csvfile:
    real_estate_reader = csv.reader(csvfile, delimiter=",")
    for row in real_estate_reader:
        print(' ,'.join(row))

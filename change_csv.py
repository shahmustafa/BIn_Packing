import csv
import numpy as np
import os

dir_path = '/mnt/3442b777-9fb5-44db-a8bf-de8d6868897c/shah/data/TIMS/NS/sig_constr'
directory = '/APC_controller_1_malfunction_0/'
# filename = dir_path + directory + '02.csv'
for root, dirs, files in os.walk(dir_path):
    # if root.endswith(directory):
    for file in files:
        var = []
        # change the extension to
        # the one of your choice.
        if file.endswith('.csv'):
            print(file)
            # toAdd = ["String", "String", "String", "String"]
            # with open(filename, "r") as infile:
            #     reader = list(csv.reader(infile))
            #     reader.insert(121, reader.copy(120))
            #
            # with open(filename, "w") as outfile:
            #     writer = csv.writer(outfile)
            #     for line in reader:
            #         writer.writerow(line)
            filename = root + '/' + str(file)
            with open(filename, "r") as infile:
                reader = list(csv.reader(infile))
                lines = [line for line in reader]
                reader.insert(121, lines[120])

            with open(filename, "w") as outfile:
                writer = csv.writer(outfile)
                for line in reader:
                    writer.writerow(line)
from finders import rwl_finder
from readers import RwlReader

import tkFileDialog as fd
import csv

rwl_dir = fd.askdirectory(title="Choose directory with RWLs")
# rwl_dir = r"E:\gdp_temperature_project\results\treering_data_width"

with open("core_ids_normal.csv", "wb") as core_ids_normal, open("core_ids_weird.csv", "wb") as core_ids_weird:
    writer_normal = csv.writer(core_ids_normal, delimiter=",")
    writer_weird = csv.writer(core_ids_weird, delimiter=",")

    for package in rwl_finder(rwl_dir): 

        package_paleodata_files = package['paleodata']

        for paleodata_file in package_paleodata_files: 
            package_copy = {
                'correlation': package['correlation'], 
                'paleodata': [paleodata_file],
                'metadata': package['metadata']
            }

            reader = RwlReader(package_copy)

            for row in reader.get_data(test=1): 
                if row[7] == ' ' or row[7].isalpha():
                    writer_normal.writerow([paleodata_file, row[:12].strip()])
                else: 
                    writer_weird.writerow([paleodata_file, row[:12].strip()])
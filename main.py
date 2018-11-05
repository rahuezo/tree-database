from finders import rwl_finder
from readers import RwlReader

import tkFileDialog as fd
import csv

rwl_dir = fd.askdirectory(title="Choose directory with RWLs")
# rwl_dir = r"E:\gdp_temperature_project\results\treering_data_width"

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
            print row[:12].strip()
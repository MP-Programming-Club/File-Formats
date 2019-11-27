"""
Getting the actual data from a .json file is pretty straightforward once you know the file structure

This is unfortunately not always easy to sort out, especially if you aren't used to dealing with them.

Thankfully there are websites and viewers that solve the issue e.g. http://www.jsoneditoronline.org/

The Firefox browser can also natively open .json files and can highlight any issues with the file structure

"""

# This package has the modules needed to work with JSON files
import json

# For plotting the read in data
import matplotlib.pyplot as plt

# Reads in the file and stores all data in an accessible form
with open('FILEPATH.json') as data_file:
    jdata = json.load(data_file)

# Opening storage arrays for the desired variables e.g. magnitude and time
Variable1 = []
Variable2 = []

"""
Data is extracted from the overall structure by stepping through the tiers of data - referred to as keys

e.g.  Data = jdata[ 'keyname1' ][ 'keyname2' ]

You can also add an index to this call 
e.g. you only want data from set of observations corresponding to index 2 in keyname1:

Data = jdata[ 'keyname1' ][2][ 'keyname2' ]

You can also use loops to run through all such indexes see below

"""

i = 0

for item in jdata['key1']:
    # Extracts the desired data

    Variable1.append(jdata['key1'][i]['key2'])
    Variable2.append(jdata['key1'][i]['key3'])

    i = i + 1

# Generates and displays a basic plot of the extracted data

plt.scatter(Variable1, Variable2)
plt.show()

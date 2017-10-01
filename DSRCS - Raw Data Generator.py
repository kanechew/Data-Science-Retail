# Header ##########################
"""
Filename:       DSRCS - Raw Data Generator
Project:        Data Science Retail Case Generator
Repository:     https://github.com/kanechew/Data-Science-Retail

Author:         Kane Chew
Description:    This file will generate raw data and write them into a CSV File
"""

# Start of Program ################

# Libraries #######################
    import random
    import time
    import re
    import csv
    import numpy

# Functions #######################

# Generate Random Time
def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

# Generate Random Date
def randomDate(start, end, prop):

    date    = strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)
    date2   = re.match('[0-9/]+', date)
    return date2

# Main ###########################

# Write data into CSV File

f = open("transaction_records_2016.csv", 'wt', newline='') # newline='' takes away empty lines between each row

fieldnames = ['no','date', 'location']
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()

for i in range(0,100):

    # date object
    date = randomDate("1/1/2016 12:00 AM", "12/31/2016 12:59 PM", random.random())

    # Generate Random Location
    # postcode = random.randint(1, 2)  # each number represents a location
    postcode = numpy.random.choice(numpy.arange(1, 3), p=[0.6, 0.4]) # 1 and 2 but exlcuding 3

    if postcode == 1:
        location = 'IN'
    else:
        location = 'FL'

    writer.writerow({'no':i+1,'date': date[0], 'location': location})

f.close()

# Verify CSV File
print(open("transaction_records_2016.csv", 'rt').read())

# End of Program ###################
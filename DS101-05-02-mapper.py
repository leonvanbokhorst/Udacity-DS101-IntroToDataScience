import sys
import string
import logging


def mapper():
    # Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    # Each line will be a comma-separated list of values. The
    # header row WILL be included. Tokenize each row using the
    # commas, and emit (i.e. print) a key-value pair containing the
    # district (not state) and Aadhaar generated, separated by a tab.
    # Skip rows without the correct number of tokens and also skip
    # the header row.

    # You can see a copy of the the input Aadhaar data
    # in the link below:
    # https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    # Since you are printing the output of your program, printing a debug
    # statement will interfere with the operation of the grader. Instead,
    # use the logging module, which we've configured to log to a file printed
    # when you click "Test Run". For example:
    # logging.info("My debugging message")

    header = True
    colnum = 12
    col_district = 3    # col 4 District
    col_addhaargen = 8  # col 9 Aadhaar generated

    for line in sys.stdin:
        if header:
            header = False
            continue

        data = line.strip().split(",")
        
        if len(data) != colnum:
            continue
            
        result = '{0}\t{1}'.format(data[col_district], data[col_addhaargen])
        print result


mapper()

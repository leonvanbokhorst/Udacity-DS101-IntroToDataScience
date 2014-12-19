import sys
import logging


def reducer():
    # Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    # Each line will be a key-value pair separated by a tab character.
    # Print out each key once, along with the total number of Aadhaar
    # generated, separated by a tab. Make sure each key-value pair is
    # formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    # Since you are printing the output of your program, printing a debug
    # statement will interfere with the operation of the grader. Instead,
    # use the logging module, which we've configured to log to a file printed
    # when you click "Test Run". For example:
    # logging.info("My debugging message")

    current_key = None
    aadhaargen_count = 0

    for line in sys.stdin:
        data = line.strip().split('\t')
        
        key, value = data
        
        if key != current_key:
            if current_key:
                print '{0}\t{1}'.format(current_key, aadhaargen_count)
            aadhaargen_count = int(value)
            current_key = key
        else:
            aadhaargen_count += int(value)

    if current_key:
        print '{0}\t{1}'.format(current_key, aadhaargen_count)

reducer()

#!/usr/bin/python3
"""Script that reads stdin line by line and
computes metrics"""

import re
import sys

counter = 0
file_size = 0

status_codes = {200: 0, 301: 0, 400: 0,
                401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def printOut(c_dict, f_size):
    """Prints out the status codes and their number"""
    print("File size: {}".format(f_size))
    for key in sorted(c_dict.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, c_dict[key]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_string = re.split('- |"|"| " " ', str(line))
            stat_code_n_file_s = split_string[-1]
            if counter != 0 and counter % 10 == 0:
                printOut(status_codes, file_size)
            counter = counter + 1
            try:
                status_code = int(stat_code_n_file_s.split()[0])
                f_size = int(stat_code_n_file_s.split()[1])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                file_size = file_size + f_size
            except ValueError:
                pass
        printOut(status_codes, file_size)
    except KeyboardInterrupt:
        printOut(status_codes, file_size)
        raise

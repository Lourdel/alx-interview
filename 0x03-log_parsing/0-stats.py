#!/usr/bin/python3

"""script reads stdin line by line and computes metrics"""

import sys
import re


def main():
    """reads from stdin and computes metrics based on status codes"""
    status_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}

    file_size = 0
    count = 0
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break

            f_st = r'\[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
            pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ' + f_st

            match = re.match(pattern, line)
            if not match:
                continue

            status_code = match.group(3)

            if not int(status_code):
                continue

            if status_code in status_dict:
                count += 1
                status_dict[status_code] += 1
                file_size += int(match.group(4))

            if count == 10:
                print("File size: {}".format(file_size))
                sorted_dict = sorted(status_dict.items(),
                                     key=lambda x: x)
                for key, value in sorted_dict:
                    if value != 0:
                        print("{}: {}".format(key, value))
                count = 0
    except KeyboardInterrupt as e:
        sorted_dict = sorted(status_dict.items(),
                             key=lambda x: x)
        for key, value in sorted_dict:
            if value != 0:
                print("{}: {}".format(key, value))
        print(e)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""Log parsing Task"""
import sys
import re


if __name__ == "__main__":
    value_dict = {}
    file_size = 0
    count = 0

    def check_pattern(pattern):
        """Check that pattern matches"""
        status_list = [200, 301, 400, 401, 403, 404, 405, 500]
        split_list = pattern.split(" - ")
        ip = split_list[0]

        # Checks for IP address
        match = re.match(
                r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip)
        if (not bool(match)):
            return False

        # Check for date formating
        split_list = split_list[1].split("] ")
        date = split_list[0].replace('[', '')

        # Check if constant is available
        split_list = split_list[1].split('" ')
        if (split_list[0] != '"GET /projects/260 HTTP/1.1'):
            return False

        split_list = split_list[1].split(" ")
        code = split_list[0]
        size = split_list[1]

        # Check for integer value of code and in status list
        try:
            if (int(code) not in status_list or len(split_list) != 2):
                return False
        except ValueError:
            return False

        # Check for integer value of size
        try:
            size = int(size)
        except ValueError:
            return False

        return [code, int(size)]

    def print_result():
        """Print results"""
        print('File size: {}'.format(file_size))
        sort_data = dict(sorted(value_dict.items()))
        for key, value in sort_data.items():
            print('{}: {}'.format(key, value))

    try:
        for line in sys.stdin:
            result = check_pattern(line)
            if (result is not False):
                count = count + 1
                value_dict[result[0]] = value_dict.get(result[0], 0) + 1
                file_size = file_size + result[1]
                if (count == 10):
                    count = 0
                    print_result()
    except KeyboardInterrupt as e:
        print_result()
        raise

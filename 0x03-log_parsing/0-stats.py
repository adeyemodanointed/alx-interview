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
        split_list = pattern.split(" ")

        # Check if size and codes fit values
        try:
            size = split_list[-1]
            code = split_list[-2]
            if (int(code) not in status_list):
                code = 0
        except (ValueError, IndexError):
            code = 0

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
            if (result is not False and result[0] == 0):
                file_size += result[1]
            elif (result is not False and result[0] != 0):
                count = count + 1
                value_dict[result[0]] = value_dict.get(result[0], 0) + 1
                file_size += result[1]
                if (count == 10):
                    count = 0
                    print_result()
            else:
                pass
        print_result()
    except (KeyboardInterrupt, EOFError):
        print_result()

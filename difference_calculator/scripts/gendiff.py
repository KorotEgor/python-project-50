#!/usr/bin/env python3

import argparse
import json


def generate_diff(path1, path2):
    file1 = json.load(open(path1))
    file2 = json.load(open(path2))

    keys = sorted(list(file1 | file2))
    status = ['{']
    for el in keys:
        if el in file1 and el in file2 and file1[el] == file2[el]:
            status.append(f'    {el}: {json.dumps(file1[el])}')
        elif el in file1 and el in file2 and file1[el] != file2[el]:
            status.append(f'  - {el}: {json.dumps(file1[el])}')
            status.append(f'  + {el}: {json.dumps(file2[el])}')
        elif el in file1 and el not in file2:
            status.append(f'  - {el}: {json.dumps(file1[el])}')
        else:
            status.append(f'  + {el}: {json.dumps(file2[el])}')
    status.append('}')
    return '\n'.join(status)


def show_certificate():
    desc = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    show_certificate()

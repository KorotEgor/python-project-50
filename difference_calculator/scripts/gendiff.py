#!/usr/bin/env python3

import argparse
import json
import yaml


def formating(key, dictionary):
    value = dictionary[key]
    if isinstance(value, bool):
        dictionary[key] = str(value).lower()


def load(path):
    ext = path.split('.')[-1]
    match ext:
        case 'json':
            return json.load(open(path))
        case 'yml' | 'yaml':
            return yaml.safe_load(open(path))
        case _:
            raise ValueError(f'unknown ext - {ext}')


def generate_diff(path1, path2):
    file1 = load(path1)
    file2 = load(path2)
    keys = sorted(list(file1 | file2))
    status = ['{']
    for key in keys:
        if key in file1 and key in file2 and file1[key] == file2[key]:
            formating(key, file1)
            status.append(f'    {key}: {file1[key]}')
        elif key in file1 and key in file2 and file1[key] != file2[key]:
            formating(key, file1)
            formating(key, file2)
            status.append(f'  - {key}: {file1[key]}')
            status.append(f'  + {key}: {file2[key]}')
        elif key in file1 and key not in file2:
            formating(key, file1)
            status.append(f'  - {key}: {file1[key]}')
        else:
            formating(key, file2)
            status.append(f'  + {key}: {file2[key]}')
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

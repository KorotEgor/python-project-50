#!/usr/bin/env python3

import argparse
import json
import yaml


_SAME = 'same'
_SECOND = 'second'
_FIRST = 'first'


def formating(value, ind):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, list):
        return stylish(value, ind)
    return value


def load(path):
    ext = path.split('.')[-1]
    match ext:
        case 'json':
            return json.load(open(path))
        case 'yml' | 'yaml':
            return yaml.safe_load(open(path))
        case _:
            raise ValueError(f'unknown ext - {ext}')


def diff(file1, file2):
    keys = sorted(list(file1 | file2))
    status = []
    for key in keys:
        if key in file1 and key in file2 and file1[key] == file2[key]:
            if isinstance(file1[key], dict):
                value = diff(file1[key], file2[key])
            else:
                value = file1[key]
            status.append({"status": _SAME, "key": key, "value": value})
        elif key in file1 and key in file2 and file1[key] != file2[key]:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                value = diff(file1[key], file2[key])
                status.append({"status": _SAME, "key": key, "value": value})
            elif isinstance(file1[key], dict):
                value = diff(file1[key], file1[key])
                status.append({"status": _FIRST, "key": key, "value": value})
                status.append({"status": _SECOND, "key": key, "value": file2[key]})
            elif isinstance(file2[key], dict):
                value = diff(file2[key], file2[key])
                status.append({"status": _FIRST, "key": key, "value": file1[key]})
                status.append({"status": _SECOND, "key": key, "value": value})
            else:
                status.append({"status": _FIRST, "key": key, "value": file1[key]})
                status.append({"status": _SECOND, "key": key, "value": file2[key]})
        elif key in file1 and key not in file2:
            if isinstance(file1[key], dict):
                value = diff(file1[key], file1[key])
            else:
                value = file1[key]
            status.append({"status": _FIRST, "key": key, "value": value})
        else:
            if isinstance(file2[key], dict):
                value = diff(file2[key], file2[key])
            else:
                value = file2[key]
            status.append({"status": _SECOND, "key": key, "value": value})
    return status


def stylish(status, ind=0):
    draw = ['{']
    for row in status:
        match row['status']:
            case 'same':
                begin = '    '
            case 'second':
                begin = '  + '
            case 'first':
                begin = '  - '
        value = formating(row['value'], ind + 1)
        draw.append(f'{"    " * ind}{begin}{row["key"]}: {value}')
    draw.append('    ' * ind + '}')
    return '\n'.join(draw)


def generate_diff(path1, path2):
    file1 = load(path1)
    file2 = load(path2)
    status = diff(file1, file2)
    return stylish(status)


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

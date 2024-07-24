#!/usr/bin/env python3

import argparse
import json

import yaml

from difference_calculator.style import stylish, plain

_SAME = "same"
_SECOND = "second"
_FIRST = "first"


def load(path):
    ext = path.split(".")[-1]
    match ext:
        case "json":
            return json.load(open(path))
        case "yml" | "yaml":
            return yaml.safe_load(open(path))
        case _:
            raise ValueError(f"unknown ext - {ext}")


def value(value):
    if isinstance(value, dict):
        return diff(value, value)

    return value


def row(status, key, value):
    return {"status": status, "key": key, "value": value}


def diff(file1, file2):
    keys = sorted(list(file1 | file2))
    status = []

    for key in keys:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if key in file1 and key in file2 and value1 == value2:
            status.append(row(_SAME, key, value(value1)))
        elif key in file1 and key in file2 and value1 != value2:
            if isinstance(value1, dict) and isinstance(value2, dict):
                status.append(row(_SAME, key, diff(value1, value2)))
            else:
                status.append(row(_FIRST, key, value(value1)))
                status.append(row(_SECOND, key, value(value2)))
        elif key in file1 and key not in file2:
            status.append(row(_FIRST, key, value(value1)))
        else:
            status.append(row(_SECOND, key, value(value2)))

    return status


def draw(status, style):
    match style:
        case "plain":
            return plain.plain(status)
        case "stylish":
            return stylish.stylish(status)
        case _:
            raise ValueError(f"unknown style - {style}")


def generate_diff(path1, path2, style):
    file1 = load(path1)
    file2 = load(path2)
    status = diff(file1, file2)
    return draw(status, style)


def show_certificate():
    desc = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        dest="format",
        default="stylish",
        help="set format of output",
    )

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    show_certificate()

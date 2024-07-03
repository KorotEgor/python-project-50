#!/usr/bin/env python3

import argparse


def show_certificate():
    desc = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
            help='set format of output')

    args = parser.parse_args()
    print(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    show_certificate()

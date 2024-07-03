#!/usr/bin/env python3

import argparse


def show_certificate():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()
    print(args.filename, args.filename)


if __name__ == '__main__':
    show_certificate()

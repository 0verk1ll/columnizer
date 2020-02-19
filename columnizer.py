#!/usr/bin/env python3

import argparse
import os


def check_file(file_name):
    """Chekc file name and path"""
    if not check_path(file_name):
        quit()
    elif not check_filetype(file_name):
        quit()
    return


def check_filetype(file_name):
    """Check if file is plain text."""
    f = os.popen('file -bi %s', 'r' % file_name)
    return f.read().startswith('text/plain')


def check_path(path):
    """Check if file path exists."""
    return os.path.exists(path)


def process(args):
    """Process user's arguments."""
    file_name = args.read[0]
    check_file(file_name)
    with open(file_name, 'r') as target:
        print(target.read())
    col_width = args.read[1]


def backup_file(file_name):
    pass


def main():
    # Input file

    parser = argparse.ArgumentParser(
        description="Changes text files to fit in a given collumn width.")

    # --colwidth defaults to 80

    # Define arguments.
    parser.add_argument("file", type=str, dest='path',
                        required=True, help="Path to a file.")
    parser.add_argument("-cw", "--colwidth", default=80, type=int, dest='ColWidth',
                        help="Collumn width in characters. Default 80")

    # Read command

    args = parser.parse_args()

    if args.path is None:
        quit()
    else:
        check_file(args[0])

    # If collumn is text, exit
        # save copy of the file
        # If line is > 80, insert newline at 81
        # save file


if __name__ == "__main__":
    main()

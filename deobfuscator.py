#! /usr/bin/env python3

import argparse


def deobf(filename):
    code = eval(open(filename, 'r').read())  # Read the file and evaluate it
    print(code)  # Print the code


def main():
    parser = argparse.ArgumentParser(prog='Quantum Deobfuscator',
                                     description='Deobfuscates the code to reveal the original source')
    parser.add_argument('filename', help='Name of the file to obfuscate')
    args = parser.parse_args()

    deobf(args.filename)


if __name__ == '__main__':
    main()

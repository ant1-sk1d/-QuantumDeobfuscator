#! /usr/bin/env python3

import argparse


def deobf(filename):
    with open(filename, 'r') as f:
        f = f.read()
        
        #
        print("DAMN! I've hit a snag. If only there was a way to print the code instead of executing it?")
        #
        
        # I think after making it print instead of exec, I should run the code and it should print out the deobfuscated code.
        exec(f)

def main():
    parser = argparse.ArgumentParser(prog='Quantom Deobfuscator',
                                     description='Deobfuscates the code to reveal the original source')
    parser.add_argument('filename', help='Name of the file to obfuscate')
    args = parser.parse_args()

    deobf(args.filename)


if __name__ == '__main__':
    main()

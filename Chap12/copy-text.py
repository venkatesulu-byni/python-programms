#!/usr/bin/env python3


def main():
    infile = open('lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()

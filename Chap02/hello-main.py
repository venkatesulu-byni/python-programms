#!/usr/bin/env python3


import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('hi there')
    print('line12')
    
if __name__ == '__main__': main()

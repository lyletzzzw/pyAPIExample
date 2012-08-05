#!/usr/bin/env python
#coding=utf-8

import sys
import getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ho:", ["help", "output="])  
        print '--------opts:'
        for o,a in opts:
            if o in ('-h','--help'):
                print o,a
            if o in ('-o','--output'):  
                print o,a
        
        print '--------argv:'
        for elem in args:
            print elem
        
    except getopt.GetoptError:
        sys.exit(2)
    

if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/python

import sys
from main import IMESelector

if __name__=="__main__":
    selector = IMESelector()
    ime = selector.getIME(' '.join(sys.argv[1:]))
    ime.execute()

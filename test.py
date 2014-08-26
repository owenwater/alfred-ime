#!/usr/bin/python

import sys
import math
from main import IME

if __name__=="__main__":
    ime = IME(' '.join(sys.argv[1:]))
    ime.execute()

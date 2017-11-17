#!/usr/bin/env python

"""PEP8 check script for CotEditor

Check Python source code of the current document on CotEditor with pep8.
This is a CotEditor script.
"""

__version__ = '1.1.0'
__date__ = '2017-10-17'
__author__ = '1024jp <http://wolfrosch.com/>'
__license__ = 'Creative Commons Attribution-NonCommercial 3.0 Unported License'


import sys
import os
from subprocess import Popen, PIPE

# setting -----------------------------------------------------------

# path to pycodestyle
PEP8 = '/usr/local/bin/pycodestyle'


# main --------------------------------------------------------------

def main(filepath):
    # check pep8
    results = Popen([PEP8, filepath], stdout=PIPE).stdout

    # write results to CotEditor's Script Errors window
    sys.stderr.write('checked -> ' + os.path.basename(filepath) + '\n')
    for line in results:
        sys.stderr.write(line.split(':', 1)[-1])


if __name__ == "__main__":
    filepath = sys.argv[1]
    main(filepath)

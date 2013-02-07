#!/usr/bin/env python

"""PEP8 check script for CotEditor

Check Python source code of the current document on CotEditor with pep8.
This is a CotEditor script.
"""

__version__ = '1.0.1'
__date__ = '2013-02-07'
__author__ = '1024jp <http://wolfrosch.com/>'
__license__ = 'Creative Commons Attribution-NonCommercial 3.0 Unported License'


import sys
import os
from subprocess import Popen, PIPE

# setting -----------------------------------------------------------

# path to pep8
PEP8 = '/usr/local/bin/pep8'


# main --------------------------------------------------------------

def run_osascript(script):
    """Run osascript."""
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE)
    stdout, stderr = p.communicate(script)

    return stdout.rstrip()


def main():
    # get filepath of the front document on CotEditor
    filepath = run_osascript('tell application "CotEditor" to '
                             'return path of front document')

    # check pep8
    results = Popen([PEP8, filepath], stdout=PIPE).stdout

    # write results to CotEditor's Script Errors window
    sys.stderr.write('pep8-> ' + os.path.basename(filepath) + '\n')
    for line in results:
        sys.stderr.write(line.split(':', 1)[-1])


main()

#!/usr/bin/env python

"""PEP8 check script for CotEditor

Check Python source code of the current document on CotEditor with pep8.
This is a CotEditor script.
"""

__version__ = '1.0'
__date__ = '2012-12-27'
__author__ = '1024jp <http://wolfrosch.com/>'
__license__ = "Creative Commons Attribution-NonCommercial 3.0 Unported License"


import sys
import os
from subprocess import Popen, PIPE

# setting -----------------------------------------------------------

# path to pep8
pep8 = "/usr/local/bin/pep8"


# main --------------------------------------------------------------

# osascript to get filepath of CotEditor document
osascript = """
on run
    tell application "CotEditor"
        set thePath to ""
        if exists front document then
            set thePath to path of front document as Unicode text
        end if
    end tell

    return thePath
end run
"""


def main():
    # get filepath of the front document
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE)
    stdout, stderr = p.communicate(osascript)
    filepath = stdout.rstrip()
    sys.stderr.write('pep8-> ' + os.path.basename(filepath) + '\n')

    # check pep8
    p = Popen([pep8, filepath], stdout=PIPE)

    # write results to CotEditor's Script Errors window
    for line in p.stdout:
        sys.stderr.write(line.split(':', 1)[-1])


main()

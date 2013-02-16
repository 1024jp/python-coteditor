#!/usr/bin/env python

"""Open New Document on CotEditor with Python Template.

This is a CotEditor script.

%%%{CotEditorXInput=None}%%%
%%%{CotEditorXOutput=InsertAfterSelection}%%%
"""

from __future__ import print_function

__version__ = '1.0.1'
__date__ = '2013-02-16'
__author__ = '1024jp <http://wolfrosch.com/>'
__license__ = "Creative Commons Attribution-NonCommercial 3.0 Unported License"

from subprocess import Popen, PIPE
from datetime import date


# template ----------------------------------------------------------

AUTHOR = '1024jp <http://wolfrosch.com/>'

TEMPLATE = """#!/usr/bin/env python

from __future__ import division, print_function

__date__ = '{date}'
__author__ = '{author}'


main():
    pass


if __name__ == "__main__":
    main()
""".format(date=date.today(), author=AUTHOR)


# main --------------------------------------------------------------

def run_osascript(script):
    """Run osascript."""
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE)
    stdout, stderr = p.communicate(script)

    return stdout.rstrip()


def main():
    # open new document on CotEditor
    run_osascript('tell application "CotEditor" to make new document')
    
    # set coloring style to Python
    run_osascript('tell application "CotEditor" '
                  'to set coloring style of front document to "Python"')
    
    # insert template
    print(TEMPLATE, end='')


if __name__ == "__main__":
    main()

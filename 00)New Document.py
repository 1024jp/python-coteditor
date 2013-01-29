#!/usr/bin/env python

"""Open New Document with Python Template

%%%{CotEditorXInput=None}%%%
%%%{CotEditorXOutput=InsertAfterSelection}%%%
"""

from __future__ import print_function

__version__ = '1.0'
__date__ = '2012-12-29'
__author__ = '1024jp <http://wolfrosch.com/>'
__license__ = "Creative Commons Attribution-NonCommercial 3.0 Unported License"

from subprocess import Popen, PIPE
from datetime import date


# template ----------------------------------------------------------

author = '1024jp <http://wolfrosch.com/>'

template = """#!/usr/bin/env python

from __future__ import division, print_function

__date__ = '{}'
__author__ = '{}'


main():
    pass


if __name__ == "__main__":
    main()
""".format(date.today(), author)


# main --------------------------------------------------------------

# osascript to open new CotEditor document
open_new_document = """
on run
    tell application "CotEditor"
        make new document
        set coloring style of front document to "Python"
        set theEncoding to IANA charset of front document of application "CotEditor"
    end tell
end run
"""


# open new document on CotEditor
p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE)
p.communicate(open_new_document)

# insert template
print(template, end='')

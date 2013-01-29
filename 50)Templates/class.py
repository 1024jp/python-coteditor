#!/usr/bin/env python

"""Insert blank class

%%%{CotEditorXInput=None}%%%
%%%{CotEditorXOutput=InsertAfterSelection}%%%
"""

__version__ = '1.0'
__date__ = '2013-01-29'
__author__ = '1024jp <http://wolfrosch.com/>'
__license__ = "Creative Commons Attribution-NonCommercial 3.0 Unported License"


print("""class Foo(object):
    def __init__(self, arg):
        pass""")

#!/usr/bin/env python

"""Insert property accessor set

%%%{CotEditorXInput=None}%%%
%%%{CotEditorXOutput=InsertAfterSelection}%%%
"""

__version__ = '1.0'
__date__ = '2013-01-29'
__author__ = '1024jp <http://wolfrosch.com/>'
__license__ = "Creative Commons Attribution-NonCommercial 3.0 Unported License"


print("""def foo():
        doc = "short explanation for bar property"

        def fget(self):
            return self._foo

        def fset(self, value):
            self._foo = value

        def fdel(self):
            del self._foo

        return locals()

    foo = property(**foo())
""")

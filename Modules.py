"""Import modules """
import Module1
from Module1 import *
from Module1 import f
"""from .Module1 import f"""

f()


# When we have several modules with same function name, import using as

from Module1 import f as f1
from Module2 import f as f2
#from .Module1 import f

f1()
f2()

# A package is a directory which has file __init__.py. Inside this file we declare which modules are seen
# This file can also have code written
# An init file empty, means that all modules are seen outside
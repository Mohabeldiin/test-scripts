"""this file is to fix packaging and modeling in python 
    for more information read https://docs.python.org/3/tutorial/modules.html#packages"""
from locator import locator
import element
import page

"""the __all__ contains the moduls names
    NOTE: not that __all__ must be always updated
    USE: __all__ used to import all mudols from that package by using import *
    WHY: __all__ fix packaging error when use import *"""
__all__ =["page", "element", "locator"]
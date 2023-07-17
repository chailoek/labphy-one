"""An example magic"""
__version__ = '0.0.1'

from .labutils import LabUtils

def load_ipython_extension(ipython):
    ipython.register_magics(LabUtils)
import os
import xarray as xr

def load_1nc (filepath, filename):
    DIR = os.path.expanduser (filepath)
    PATH = os.path.join(DIR, filename)
    data = xr.open_dataset (PATH)
    return data

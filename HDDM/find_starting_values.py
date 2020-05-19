#!/usr/bin/python

from copy import copy
import pickle
import sys

import numpy as np
from scipy.optimize import minimize, basinhopping

from collections import OrderedDict, defaultdict

import pandas as pd
import pymc as pm
import warnings

from kabuki.utils import flatten
from . import analyze

def find_starting_values(self, *args, **kwargs, defineValues=False):
    """Find good starting values for the different parameters by
    optimization.
    For more options see approximate_map and map. Arguments are forwarded.
    DefineValues is a boolean that if set to false, we will define our own values.
    """
    if (defineValues == True):
        if self.is_group_model:
            self.approximate_map(*args, **kwargs)
        else:
            self.map(*args, **kwargs)
    elif (defineValues == False):
        
        

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:37:52 2023

@author: gabri
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# a figure with one axes on the left, and two on the right:
fig, axs = plt.subplot_mosaic([['left', 'right-top'], ['left', 'right_bottom']])

"""
Author: Jakidxav

This set of helper methods was used in the shallow_circ_composite_analysis_tstat Jupyter Notebook. Since many of them are being used again in another program, I am creating this file of helper methods.
"""

import numpy as np

"""
Enter in indices of months you want to subset for, and get out a subset of the data
where the months are both in a season (DJF, MAM, etc) AND they occur below some threshold value.
This method assumes that time is in the first axis (axis 0).
"""
def season_and_threshold(anom, season_pc_idx):
    
    return anom[season_pc_idx]




"""
Enter in an array, and get back that array averaged over dimension 'dim'. This method should not be used in the array contains NaN values, although it could be changed to use np.nanmean() instead of mean.
"""
def average_over_dim(anom, dim):
    
    return np.mean(anom, axis=dim)




"""
Given U- and V-wind matrices, subset for pressure to return the wind componenets at some pressure (or height if you have z-coordinates). This method assumes that pressure is the first dimension.
"""
def create_wind_vectors(u, v, pressure):
    windx = u[pressure]
    windy = v[pressure]

    return windx, windy



"""
This method finds the miniminum and maxiumum values for an array, and then constructs normalized contours from them.
"""
def get_min_max_contours(var):
    min_ = np.min(var)
    max_ = np.max(var)
    
    if np.abs(min_) > max_:
        step = np.abs(min_) / 100
        vmin = min_
        vmax = -vmin
        
    else:
        step = max_ / 100
        vmin = -max_
        vmax = max_
    
    contours = np.arange(vmin, vmax, step)
    
    return vmin, vmax, contours, step

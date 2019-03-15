import numpy as np

def monthly_means_annual(matrix, t):
    jan_avg = np.nanmean(matrix[t.month==1], axis=0)
    feb_avg = np.nanmean(matrix[t.month==2], axis=0)
    mar_avg = np.nanmean(matrix[t.month==3], axis=0)
    apr_avg = np.nanmean(matrix[t.month==4], axis=0)
    may_avg = np.nanmean(matrix[t.month==5], axis=0)
    jun_avg = np.nanmean(matrix[t.month==6], axis=0)
    jul_avg = np.nanmean(matrix[t.month==7], axis=0)
    aug_avg = np.nanmean(matrix[t.month==8], axis=0)
    sep_avg = np.nanmean(matrix[t.month==9], axis=0)
    oct_avg = np.nanmean(matrix[t.month==10], axis=0)
    nov_avg = np.nanmean(matrix[t.month==11], axis=0)
    dec_avg = np.nanmean(matrix[t.month==12], axis=0)
    
    monthly_means_allYear = [jan_avg, feb_avg, mar_avg, apr_avg, may_avg, jun_avg, jul_avg, aug_avg, sep_avg, oct_avg, nov_avg, dec_avg]
    
    return monthly_means_allYear



def monthly_std_annual(matrix, t):
    jan_std = np.nanstd(matrix[t.month==1], axis=0)
    feb_std = np.nanstd(matrix[t.month==2], axis=0)
    mar_std = np.nanstd(matrix[t.month==3], axis=0)
    apr_std = np.nanstd(matrix[t.month==4], axis=0)
    may_std = np.nanstd(matrix[t.month==5], axis=0)
    jun_std = np.nanstd(matrix[t.month==6], axis=0)
    jul_std = np.nanstd(matrix[t.month==7], axis=0)
    aug_std = np.nanstd(matrix[t.month==8], axis=0)
    sep_std = np.nanstd(matrix[t.month==9], axis=0)
    oct_std = np.nanstd(matrix[t.month==10], axis=0)
    nov_std = np.nanstd(matrix[t.month==11], axis=0)
    dec_std = np.nanstd(matrix[t.month==12], axis=0)
    
    monthly_std_allYear = [jan_std, feb_std, mar_std, apr_std, may_std, jun_std, jul_std, aug_std, sep_std, oct_std, nov_std, dec_std]
    
    return monthly_std_allYear
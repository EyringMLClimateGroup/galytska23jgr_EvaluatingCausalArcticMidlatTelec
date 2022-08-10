from scipy import stats
def detrending (timeseries): 
    reg = stats.linregress(range(0,len(timeseries)), timeseries)
    timeseries = timeseries - (reg[1] + (reg[0] * range(0,len(timeseries))))
    return timeseries

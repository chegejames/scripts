from pandas import *
import numpy as np
from nltk import *

def summarize(data):
    county = data.COUNTY.unique()[0]
    cols = ["COUNTY", "CONSTITUENCY", "CAW", "POLLING_STATION"]
    no_cols = map(lambda x: x+"_VOTERS", cols)
    all_cols = list(flatten(zip(cols, no_cols)))
    county_total = data.count()[cols[0]]
    Vals = []
    C_groups = data.groupby(cols[1])
    for c in C_groups.groups.keys():
        const = C_groups.get_group(c)
        const_total = const.count()[cols[1]]
        W_group = const.groupby(cols[2])
        for w in W_group.groups.keys():
            ward = W_group.get_group(w)
            ward_total = ward.count()[cols[2]]
            stations = FreqDist(ward[cols[3]]).items()
            for s,n in stations:
                Vals.append([county, county_total, c, const_total, w, ward_total, s,n])
             
    Data = DataFrame(Vals, columns=all_cols)
    Data.sort_index(by=no_cols, ascending=False, inplace=True)
    Final = DataFrame()
    UNIQUE = DataFrame()
    C = Data[[0,1]].duplicated()
    CN = Data[[2,3]].duplicated()
    WD = Data[[4,5]].duplicated()
    UNIQUE[0] = C; UNIQUE[1] = C; UNIQUE[2] = CN; UNIQUE[3] = CN; UNIQUE[4] = WD; UNIQUE[5] = WD
    Temp = list(Data.values)
    for x,y in zip(UNIQUE.values, Temp):
        for i in range(len(x+1)):
            if x[i] == True:
                y[i] = np.nan
    M = DataFrame(Temp, columns=all_cols)
    return M
    
        
        
        
    


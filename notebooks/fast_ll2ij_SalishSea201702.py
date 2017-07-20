import numpy as np
from salishsea_tools.geo_tools import haversine
# Magic numbers
Ci2 = np.array([  1.26921890e+04,   1.59279223e+02,   1.39650621e+02,
                  1.37597009e+00,   3.21769836e-01,   1.58488524e+00])
Cj2 = np.array([ -1.26067300e+04,   6.53817493e+00,   1.76514195e+02,
                  9.06976896e-01,   4.90478919e-01,   1.33030515e+00])

def fast_ll2ij_SalishSea201702(lon,lat,model_lons,model_lats):
    def useC(XX,YY,C):
        return C[0] + C[1]*XX + C[2]*YY + C[3]*XX*YY + C[4]*XX**2 + C[5]*YY**2
    # Use coefficients to get an estimate of i and j
    ie = int(useC(lon,lat,Ci2))
    je = int(useC(lon,lat,Cj2))
    # Define search box, +/- 3 and + 20/-12 is based on max error during fit
    i1 = max(0, ie - 3)
    i2 = min(ie + 3, model_lons.shape[1])
    j1 = max(0, je - 12)
    j2 = min(je + 20, model_lons.shape[0])
    # Prepare arrays for each point in search box
    lons = model_lons[j1:j2,i1:i2].flatten()
    lats = model_lats[j1:j2,i1:i2].flatten()

    # Slow way to get the indices
    #idx = np.indices(model_lons.shape)
    #i_list2 = idx[1,j1:j2,i1:i2].flatten()
    #j_list2 = idx[0,j1:j2,i1:i2].flatten()

    # Fast way to get the indices
    i_list = np.array([x for x in range(i1,i2)]*(j2-j1))
    j_list = j1 + np.array([x for x in range(0,(j2-j1)*(i2-i1))]) // (i2-i1)

    # Test all of these points, extract closest point
    dists = haversine(
        np.array([lon] * i_list.size), np.array([lat] * j_list.size),
        lons, lats)
    n = dists.argmin()
    j, i = map(np.asscalar, (j_list[n], i_list[n]))
    return j, i

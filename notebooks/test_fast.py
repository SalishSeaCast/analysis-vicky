from fast_ll2ij_SalishSea201702 import fast_ll2ij_SalishSea201702
import netCDF4 as nc
from salishsea_tools.geo_tools import find_closest_model_point

with nc.Dataset('/home/mdunphy/MEOPAR/NEMO-forcing/grid/coordinates_seagrid_SalishSea201702.nc') as nbl:
    glamt = nbl.variables['glamt'][0,...]
    gphit = nbl.variables['gphit'][0,...]

def go():
    #for j in range(glamt.shape[0]):
    #    for i in range(glamt.shape[1]):
    for j in range(380,450):
        for i in range(280,350):
            jfast, ifast = fast_ll2ij_SalishSea201702(glamt[j,i], gphit[j,i], glamt, gphit)
            jgeo, igeo = find_closest_model_point(glamt[j,i], gphit[j,i], glamt, gphit)
            if jfast != jgeo or ifast != igeo:
                print(ifast,jfast,igeo,jgeo)
go()
import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np
import matplotlib.patches as patches
from salishsea_tools import viz_tools, geo_tools, tidetools
from bathy_helpers import *

grid = nc.Dataset('/data/vdo/MEOPAR/NEMO-forcing/grid/bathy_meter_SalishSea2.nc')

result = nc.Dataset('/ocean/vdo/MEOPAR/ariane-runs/monthlong/ariane_trajectories_qualitative.nc')
latt = result.variables['traj_lat']
lont = result.variables['traj_lon']
bathy, lons, lats = tidetools.get_bathy_data(grid)
mask = lont[:].mask
with nc.Dataset('/home/mdunphy/MEOPAR/NEMO-forcing/grid/coordinates_seagrid_SalishSea201702.nc', 'r') as cnc:
    glamf = cnc.variables['glamf'][0,...]; gphif = cnc.variables['gphif'][0,...]
    glamt = cnc.variables['glamt'][0,...]; gphit = cnc.variables['gphit'][0,...]
NY, NX = glamt.shape[0], glamt.shape[1]
glamfe, gphife = expandf(glamf, gphif)

def still_inside(time, number):
    number_of_particles = np.zeros(time)
    for n in range(time):
        for m in range(number):
            if (mask[n,m]) == False: 
                y,x = geo_tools.find_closest_model_point(lont[n,m],latt[n,m],lons, lats, land_mask=bathy.mask)
                if (598<y<658) and (118<x<134):
                    number_of_particles[n] = number_of_particles[n] + 1
    return number_of_particles

def still_inside2(time):
    number_of_particles2=np.zeros(time)
    for l in range (time):
        xarray, yarray = getboxij(glamfe, gphife, lont[l,:], latt[l,:])
        a = np.array((xarray, yarray)).T
        a = a[ (608>a[:,1]) & (a[:,1]>598) ]
        a = a[ (133>a[:,0]) & (a[:,0]>120) ]
        p,q = a.shape
        number_of_particles2[l]=p
    return number_of_particles2
still_inside2(2)
index_deep_particles=[]
d = result.variables['init_z']
for n in range(2694):
    if d[n] > 6:
        index_deep_particles.append(n)
def deep_particles(lont,latt,init_z, il, ir, jl, jr):
    p = makebox(glamfe,gphife,il,ir,jl,jr)
    poly = path.Path(p, closed=True) 
    time, particles = lont.shape
    number_of_particles = np.zeros(time)
    index_deep_particles=[]
    for n in range(particles):
        if init_z[n] > 6:
            index_deep_particles.append(n)
    length_of_deep_particles = len(index_deep_particles)
    number_of_deep_particles = np.zeros(time)
    for n in range(time):
        deep_latt = [latt[n,m] for m in index_deep_particles]
        deep_lont = [lont[n,m] for m in index_deep_particles]
        pts = np.array([deep_lont,deep_latt]).T
        test = poly.contains_points(pts)
        number_of_deep_particles[n]= sum(test) #/ length_of_deep_particles
    return number_of_deep_particles

def deep_particles2(lont,latt,init_z, il, ir, jl, jr):
    mask = lont[:].mask
    p = makebox(glamfe,gphife,il,ir,jl,jr)
    poly = path.Path(p, closed=True) 
    time, particles = lont.shape
    number_of_particles = np.zeros(time)
    index_deep_particles=[]
    for n in range(particles):
        if init_z[n] > 6:
            index_deep_particles.append(n)
    length_of_deep_particles = len(index_deep_particles)
    number_of_deep_particles = np.zeros(time)
    for n in range(time):
        for m in index_deep_particles:
            if (mask[n,m]) == False: 
                tf = poly.contains_point(np.array((lont[n,m], latt[n,m])).T)
                if tf == True:
                    number_of_deep_particles[n] = number_of_deep_particles[n] + 1
    return number_of_deep_particles
@profile
def compare(lont, latt, init_z, il, ir, jl, jr):
    deep_particles(lont, latt, init_z, il, ir, jl, jr)
    deep_particles2(lont, latt, init_z, il, ir, jl, jr)
    return None  
compare(lont[:,:2], latt[:,:2], result.variables['init_z'][:2], 120, 130, 598, 608)

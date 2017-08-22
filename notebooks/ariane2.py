from matplotlib.path import Path
import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np
import matplotlib.patches as patches
from salishsea_tools import viz_tools, geo_tools, tidetools
from bathy_helpers import *

def still_inside(il, ir, jl, jr, lont, latt):
    p = makebox(glamfe,gphife,il,ir,jl,jr)
    poly = path.Path(p, closed=True) 
    time, particles = lont.shape
    number_of_particles = np.zeros(time)
    for l in range(time):
        cx = lont[l,:]
        cy = latt[l,:]
        pts = np.array([cx,cy]).T
        test = poly.contains_points(pts)
        number_of_particles[l]= sum(test) / particles
    return number_of_particles
def deep_particles(lont,latt,init_z, il, ir, jl, jr):
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
    return (number_of_deep_particles / length_of_deep_particles)
def shallow_particles(lont,latt,init_z, il, ir, jl, jr):
    mask = lont[:].mask
    p = makebox(glamfe,gphife,il,ir,jl,jr)
    poly = path.Path(p, closed=True) 
    time, particles = lont.shape
    number_of_particles = np.zeros(time)
    index_shallow_particles=[]
    for n in range(particles):
        if init_z[n] < 6:
            index_shallow_particles.append(n)
    length_of_shallow_particles = len(index_shallow_particles)
    number_of_shallow_particles = np.zeros(time)
    for n in range(time):
        for m in index_shallow_particles:
            if (mask[n,m]) == False: 
                tf = poly.contains_point(np.array((lont[n,m], latt[n,m])).T)
                if tf == True:
                    number_of_shallow_particles[n] = number_of_shallow_particles[n] + 1
    return (number_of_shallow_particles / length_of_shallow_particles)
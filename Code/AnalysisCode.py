import numpy as np
import math
from amuse.lab import units, constants
from operator import add

G = constants.G
sig_sb = constants.Stefan_hyphen_Boltzmann_constant
k_b = constants.kB
c = constants.c
pi = constants.pi
sig_T = constants.Thomson_cross_section
m_p = constants.proton_mass

def get_M(ri, A, i):
    A = A * 1e16 | units.m**2
    i = i/360 * 2 * pi
    M = c**2 / (ri * G) * np.sqrt((A / np.cos(i)))
    return M

def get_err_M(ri, A, i, err_ri, err_A, err_i):
    A = A * 1e16 | units.m**2
    i = i/360 * 2 * pi
    
    comp_A = list(map(lambda x: (x * (1e16 | units.m**2) 
                        * ((4 * A * np.cos(i))**(-1/2)))**2, err_A))
    comp_ri = list(map(lambda x: (x * np.sqrt(A/np.cos(i)) / ri)**2, err_ri))
    comp_i = list(map(lambda x: (x * 1/360 * 2 * pi 
                        * np.sqrt(A) / 2 * (np.sin(i))**(-3/2))**2, err_i))

    err_M = list(map(add, comp_A, comp_ri))
    err_M = list(map(add, err_M, comp_i))
    err_M = list(map(lambda x: np.sqrt(x) * c**2 / (ri * G), err_M))
    return err_M

def get_M_dot(ri, ti, M):
    ti = ti * 1e3 * 1.60218e-19 | units.J
    M_dot = (G * M / c**3)**2 * (8 * pi / 3 * sig_sb) * ri**3 * (ti/k_b)**4
    return M_dot

def get_err_M_dot(ri, ti, M, err_ri, err_ti, err_M):
    ti = ti * 1e3 * 1.60218e-19 | units.J
    alpha = (G / c**3)**2 * 8 * pi * sig_sb / 3
    
    err_ti = list(map(lambda x: x * 1e3 * (1.60218e-19 | units.J) / k_b, err_ti))
    comp_M = list(map(lambda x: (x * 2 * M * ri**3 * (ti/k_b)**4)**2, err_M))
    comp_ri = list(map(lambda x: (x * 3 * M**2 * ri**2 * (ti/k_b)**4)**2, err_ri))
    comp_ti = list(map(lambda x: (x * 4 * M**2 * ri**3 * (ti/k_b)**3)**2, err_ti))
    
    err_M_dot = list(map(add, comp_M, comp_ri))
    err_M_dot = list(map(add, err_M_dot, comp_ti))
    err_M_dot = list(map(lambda x: np.sqrt(x) * alpha, err_M_dot))
    return err_M_dot

def L_Edd(M):
    return (4 * pi * G * M * m_p * c / sig_T)

def err_L_Edd(err_M):
    err_L_Edd = list(map(lambda x: x * 4 * pi * G * m_p * c / sig_T, err_M))
    return err_L_Edd
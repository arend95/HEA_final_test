import AnalysisCode as ac
from amuse.lab import units

# declaration of parameters

ri = 6.058705
err_ri =[0.19319, 0.20877]

ro = 400
err_ro = [0, 38.323]

h = 0.0
err_h = [2.8714, 0]

q = 2.514695
err_q = [2.25501e-2, 2.34599e-2]

A = 6.81709e5
err_A = [25824, 32180]

i = 29.92278
err_i = [0.39825, 0.17187]

ti = 3.2453947e-2
err_ti = [2.09574e-4, 8.38861e-5]

xil = (10**1.401 * 1e-9) | units.W*units.m
err_xil = [10**(1.4e-3)*1e-9, 10**1.6e-3*1e-9] | units.W*units.m

vz = 2001.1 | units.kms
err_vz = [0.86, 0.91] | units.kms

#nh = 9.94e-4 * 1e28 | (units.m)**-2
#err_nh = [3.9e-6, 3.5e-6] * 1e28 | (units.m)**-2

M = ac.get_M(ri, A, i)
err_M = ac.get_err_M(ri, A, i, err_ri, err_A, err_i)

M_dot = ac.get_M_dot(ri, ti, M)
err_M_dot = ac.get_err_M_dot(ri, ti, M, err_ri, err_ti, err_M)

L_Edd = ac.L_Edd(M)
err_L_Edd = ac.err_L_Edd(err_M)

m_out_omega, omega_upper = ac.m_out_omega(xil, vz, M_dot)
err_m_out, err_omega = ac.err_m_out(xil, vz, M_dot, err_xil, err_vz,
              err_M_dot, m_out_omega)

P = ac.est_period(M)

print("Black hole mass is {} and the errors are {} and {}. \n \
The accretion rate is {} and the errors are {} and {}. \n \
Eddington luminosity is {} and the errors are {} and {}. \n \
Mass outflow per unit solid angle is {} and the errors are {} and {}. \n \
Upper estimate on solid angle is {} sr and the errors are {} sr and {} sr. \n \
Period estimate:{}.".format(M.in_(units.MSun),
      err_M[0].in_(units.MSun),
      -err_M[1].in_(units.MSun),
      M_dot.in_(units.MSun/units.yr),
                err_M_dot[0].in_(units.MSun/units.yr),
                -err_M_dot[1].in_(units.MSun/units.yr),
                L_Edd.in_(units.LSun),
                err_L_Edd[0].in_(units.LSun),
                -err_L_Edd[1].in_(units.LSun),
                m_out_omega.in_(units.MSun/units.yr),
                err_m_out[0].in_(units.MSun/units.yr),
                -err_m_out[1].in_(units.MSun/units.yr),
                omega_upper,
                err_omega[0],
                -err_omega[1],
                P.in_(units.hour)
      )
    )
ac.em_profile(ri, ro, h, q, M, M_dot)    
